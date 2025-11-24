import datetime
import warnings
from collections.abc import Sequence
from pathlib import Path
from typing import Literal

import imageio
from PIL import Image
import nibabel as nib
import numpy as np
import numpy.typing as npt
from scipy.ndimage import center_of_mass
from tqdm import tqdm
import plotly.graph_objects as go
import plotly.io as pio
from matplotlib.colors import LinearSegmentedColormap, to_hex
from loguru import logger

warnings.filterwarnings("ignore", category=DeprecationWarning)

Num = int | float

__all__ = [
    "plot_brain_connection_figure",
    "save_brain_connection_frames",
    "batch_crop_images",
    "create_gif_from_images",
]


def _validate_connectome(connectome):
    """检测数据是否为有效的对称且对角线为0的连接矩阵"""
    # 1. 判断是否二维方阵
    if connectome.ndim != 2 or connectome.shape[0] != connectome.shape[1]:
        raise ValueError("connectome 必须是二维方阵")
    # 2. 判断是否对称矩阵
    if not np.allclose(connectome, connectome.T, atol=1e-8):
        raise ValueError("connectome 必须是对称矩阵")
    # 3. 判断对角线是否全为0
    if not np.allclose(np.diag(connectome), 0, atol=1e-8):
        raise ValueError("connectome 对角线必须全部为0")
    # 4. 判断是否全0矩阵，警告但不抛异常
    if np.allclose(connectome, 0, atol=1e-8):
        logger.warning("connectome 矩阵所有元素均为0，可能没有有效连接数据")


def _load_surface(file):
    """加载 .surf.gii 文件，提取顶点和面"""
    return nib.load(file).darrays[0].data, nib.load(file).darrays[1].data


def _create_mesh(vertices, faces, name):
    """创建 plotly 的 Mesh3d 图层"""
    return go.Mesh3d(
        x=vertices[:, 0],
        y=vertices[:, 1],
        z=vertices[:, 2],
        i=faces[:, 0],
        j=faces[:, 1],
        k=faces[:, 2],
        color="white",
        opacity=0.1,
        flatshading=True,
        lighting={"ambient": 0.7, "diffuse": 0.3},
        name=name,
    )


def _get_node_indices(connectome, show_all_nodes):
    """判断是否显示无任何连接的节点"""
    if not show_all_nodes:
        row_is_zero = np.any(connectome != 0, axis=1)
        return np.where(row_is_zero)[0]
    else:
        return np.arange(connectome.shape[0])


def _get_centroids_real(niigz_file):
    """读取 NIfTI 图集并计算ROI质心"""
    atlas_data = nib.load(niigz_file).get_fdata()
    affine = nib.load(niigz_file).affine
    roi_labels = np.unique(atlas_data)
    roi_labels = roi_labels[roi_labels != 0]
    centroids_voxel = [
        center_of_mass((atlas_data == label).astype(int)) for label in roi_labels
    ]
    centroids_real = [np.dot(affine, [*coord, 1])[:3] for coord in centroids_voxel]
    return np.array(centroids_real)


def _add_nodes_to_fig(
    fig, centroids_real, node_indices, nodes_name, nodes_size, nodes_color
):
    """将节点（球）添加到图中"""
    for i in node_indices:
        fig.add_trace(
            go.Scatter3d(
                x=[centroids_real[i, 0]],
                y=[centroids_real[i, 1]],
                z=[centroids_real[i, 2]],
                mode="markers+text",
                marker={
                    "size": nodes_size[i],
                    "color": nodes_color[i],
                    "colorscale": "Rainbow",
                    "opacity": 0.8,
                    "line": {"width": 2, "color": "black"},
                },
                text=[nodes_name[i]],
                hoverinfo="text+x+y+z",
                showlegend=False,
            )
        )


def _add_edges_to_fig(
    fig,
    connectome,
    centroids_real,
    nodes_name,
    scale_method,
    line_width,
    line_color,
):
    """将连接线绘制到图中"""

    def _get_gradient_color(value, color):
        """获取渐变色"""
        assert 0 <= value <= 1, "value 必须在0和1之间"
        cmap = LinearSegmentedColormap.from_list("grad_cmap", ["white", color])
        rgba = cmap(float(value))  # 坑，必须要用浮点数
        return to_hex(rgba[:3])

    nodes_num = connectome.shape[0]
    if np.all(connectome == 0):
        return

    max_strength = np.abs(connectome[connectome != 0]).max()

    for i in range(nodes_num):
        for j in range(i + 1, nodes_num):
            value = connectome[i, j]
            if value == 0:
                continue

            match scale_method:
                case "":
                    each_line_color = line_color if value > 0 else "#0000ff"
                    each_line_width = line_width
                case "width":
                    each_line_color = line_color if value > 0 else "#0000ff"
                    each_line_width = abs(value / max_strength) * line_width
                case "color":
                    norm_value = value / max_strength
                    each_line_color = _get_gradient_color(norm_value, line_color)
                    each_line_width = line_width
                case "width_color" | "color_width":
                    norm_value = value / max_strength
                    each_line_width = abs(norm_value) * line_width
                    each_line_color = _get_gradient_color(norm_value, line_color)
                case _:
                    raise ValueError(
                        "scale_method 必须为 '', 'width', 'color', 'width_color', or 'color_width'中的一种"
                    )

            connection_line = np.array(
                [centroids_real[i], centroids_real[j], [None] * 3]
            )
            fig.add_trace(
                go.Scatter3d(
                    x=connection_line[:, 0],
                    y=connection_line[:, 1],
                    z=connection_line[:, 2],
                    mode="lines",
                    line={"color": each_line_color, "width": each_line_width},
                    hoverinfo="name",
                    name=f"{nodes_name[i]}-{nodes_name[j]}",
                )
            )


def _finalize_figure(fig):
    """调整图形布局与视觉样式"""
    fig.update_traces(
        selector={"mode": "markers"},
        marker={
            "size": 10,
            "colorscale": "Viridis",
            "line": {"width": 3, "color": "black"},
        },
    )
    fig.update_layout(
        title="Connection",
        scene={
            "xaxis": {"showbackground": False, "visible": False},
            "yaxis": {"showbackground": False, "visible": False},
            "zaxis": {"showbackground": False, "visible": False},
            "aspectmode": "data",
        },
        margin={"l": 0, "r": 0, "b": 0, "t": 30},
    )


def plot_brain_connection_figure(
    connectome: npt.NDArray,
    lh_surfgii_file: str | Path,
    rh_surfgii_file: str | Path,
    niigz_file: str | Path,
    output_file: str | Path | None = None,
    show_all_nodes: bool = False,
    nodes_size: Sequence[Num] | npt.NDArray | None = None,
    nodes_name: list[str] | None = None,
    nodes_color: list[str] | None = None,
    scale_method: Literal["", "width", "color", "width_color", "color_width"] = "",
    line_width: Num = 10,
    line_color: str = "red",
) -> go.Figure:
    """绘制大脑连接图，保存在指定的html文件中。

    Args:
        connectome (npt.NDArray):
            大脑连接矩阵，形状为 (n, n)，其中 n 是脑区数量。
            矩阵中的值表示脑区之间的连接强度，正值表示正相关连接，负值表示负相关连接，0表示无连接。
        lh_surfgii_file (str | Path):
            左半脑表面几何文件路径 (.surf.gii 格式)，用于绘制左半脑表面
        rh_surfgii_file (str | Path):
            右半脑表面几何文件路径 (.surf.gii 格式)，用于绘制右半脑表面
        niigz_file (str | Path):
            NIfTI格式的脑区图谱文件路径 (.nii.gz 格式)，用于定位脑区节点的三维坐标
        output_file (str | Path | None, optional):
            输出HTML文件路径。如果未指定，则使用当前时间戳生成文件名。默认为None
        show_all_nodes (bool, optional):
            是否显示所有脑区节点。如果为False，则只显示有连接的节点。默认为False
        nodes_size (Sequence[Num] | npt.NDArray | None, optional):
            每个节点的大小，长度应与脑区数量一致。默认为None，即所有节点大小为5
        nodes_name (list[str] | None, optional):
            每个节点的名称标签，长度应与脑区数量一致。默认为None，即不显示名称
        nodes_color (list[str] | None, optional):
            每个节点的颜色，长度应与脑区数量一致。默认为None，即所有节点为白色
        scale_method (Literal["", "width", "color", "width_color", "color_width"], optional):
            连接线的缩放方法:
            - "" : 所有连接线宽度和颜色固定
            - "width" : 根据连接强度调整线宽，正连接为红色，负连接为蓝色
            - "color" : 根据连接强度调整颜色(使用蓝白红颜色映射)，线宽固定
            - "width_color" or "color_width" : 同时根据连接强度调整线宽和颜色
            默认为 ""
        line_width (Num, optional):
            连接线的基本宽度。当scale_method包含"width"时，此值作为最大宽度参考。默认为10
        line_color (str, optional):
            连接线的基本颜色。当scale_method不包含"color"时生效。默认为"#ff0000"(红色)

    Returns:
        go.Figure: Plotly图形对象，包含绘制的大脑连接图
    """
    _validate_connectome(connectome)

    if np.any(connectome < 0):
        logger.warning(
            "由于 connectome 存在负值，连线颜色无法自定义，只能正值显示红色，负值显示蓝色"
        )
        line_color = "#ff0000"

    nodes_num = connectome.shape[0]
    nodes_name = nodes_name or [""] * nodes_num
    nodes_color = nodes_color or ["white"] * nodes_num
    nodes_size = nodes_size or [5] * nodes_num

    if output_file is None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = Path(f"{timestamp}.html")
        logger.info(f"未指定保存路径，默认保存在当前文件夹下的{output_file}中。")

    node_indices = _get_node_indices(connectome, show_all_nodes)
    vertices_L, faces_L = _load_surface(lh_surfgii_file)
    vertices_R, faces_R = _load_surface(rh_surfgii_file)

    mesh_L = _create_mesh(vertices_L, faces_L, "Left Hemisphere")
    mesh_R = _create_mesh(vertices_R, faces_R, "Right Hemisphere")

    fig = go.Figure(data=[mesh_L, mesh_R])

    centroids_real = _get_centroids_real(niigz_file)
    _add_nodes_to_fig(
        fig, centroids_real, node_indices, nodes_name, nodes_size, nodes_color
    )
    _add_edges_to_fig(
        fig,
        connectome,
        centroids_real,
        nodes_name,
        scale_method,
        line_width,
        line_color,
    )
    _finalize_figure(fig)

    fig.write_html(output_file)
    return fig


def save_brain_connection_frames(
    fig: go.Figure, output_dir: str | Path, n_frames: int = 36
) -> None:
    """
    生成不同角度的静态图片帧，可用于制作旋转大脑连接图的 GIF。

    Args:
        fig (go.Figure): Plotly 的 Figure 对象，包含大脑表面和连接图。
        output_dir (str): 图片保存的文件夹路径，若文件夹不存在则自动创建。
        n_frames (int, optional): 旋转帧的数量。默认 36，即每 10 度一帧。
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    angles = np.linspace(0, 360, n_frames, endpoint=False)
    for i, angle in tqdm(enumerate(angles), total=len(angles)):
        camera = dict(
            eye=dict(
                x=2 * np.cos(np.radians(angle)), y=2 * np.sin(np.radians(angle)), z=0.7
            )
        )
        fig.update_layout(scene_camera=camera)
        pio.write_image(fig, f"{output_dir}/frame_{i:03d}.png", width=800, height=800)
    logger.info(f"保存了 {n_frames} 张图片在 {output_dir}")


def batch_crop_images(
    directory_path: Path,
    suffix: str = "_cropped",
    left_frac: float = 0.25,
    top_frac: float = 0.25,
    right_frac: float = 0.25,
    bottom_frac: float = 0.25,
):
    """
    批量裁剪指定目录下的图像文件。

    Args:
        directory_path (Path): 图像文件所在的目录路径。
        suffix (str, optional): 新文件名后缀。默认为 "_cropped"。
        left_frac (float, optional): 左侧裁剪比例（0-1）。默认为 0.2。
        top_frac (float, optional): 上侧裁剪比例（0-1）。默认为 0.15。
        right_frac (float, optional): 右侧裁剪比例（0-1）。默认为 0.2。
        bottom_frac (float, optional): 下侧裁剪比例（0-1）。默认为 0.15。

    Notes:
        支持常见图像格式 (PNG, JPG, JPEG, BMP, TIFF)。
        裁剪后的图像将保存在原目录中，并添加指定后缀，原图像保持不变。
        所有裁剪均基于图像尺寸的百分比计算，无绝对像素值。
    """
    supported_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif"}

    for image_path in directory_path.rglob("*"):
        if (
            not image_path.is_file()
            or image_path.suffix.lower() not in supported_extensions
        ):
            continue

        new_file_name = image_path.stem + suffix + image_path.suffix

        try:
            figure = Image.open(image_path)
            width, height = figure.size
            print(f"图像宽度：{width}，高度：{height}")

            left = int(width * left_frac)
            right = int(width * (1 - right_frac))
            top = int(height * top_frac)
            bottom = int(height * (1 - bottom_frac))

            # 裁切图像
            cropped_fig = figure.crop((left, top, right, bottom))
            # 保存裁切后的图像
            cropped_fig.save(image_path.parent / new_file_name)

            figure.close()
            cropped_fig.close()
        except Exception as e:
            print(f"处理文件 {image_path.name} 时出错: {e}")


def create_gif_from_images(
    folder_path: str | Path,
    output_name: str = "output.gif",
    fps: int = 10,
) -> None:
    """
    从指定文件夹中的图片生成 GIF 文件。

    Args:
        folder_path (str | Path): 图片所在文件夹路径
        output_name (str, optional): 输出 GIF 文件名，默认为 "output.gif"
        fps (int, optional): GIF 帧率，默认为 10
    """
    folder = Path(folder_path)
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"{folder} 不是有效的文件夹路径。")

    # 获取文件夹下指定扩展名的文件，并排序
    extensions = (".png", ".jpg", ".jpeg")
    figures_path = sorted(
        [f for f in folder.iterdir() if f.suffix.lower() in extensions]
    )

    if not figures_path:
        raise ValueError(f"文件夹 {folder} 中没有找到符合 {extensions} 的图片文件。")

    figures = [Image.open(f) for f in figures_path]

    # 输出 GIF 路径
    output_path = folder / output_name

    # 创建 GIF
    with imageio.get_writer(output_path, mode="I", fps=fps, loop=0) as writer:
        for figure in figures:
            writer.append_data(figure.convert("RGB"))

    logger.info(f"GIF 已保存到: {output_path}")
