import os
import os.path as op
import datetime
import numpy as np
import nibabel as nib
from scipy.ndimage import center_of_mass
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from tqdm import tqdm
from pathlib import Path
import numpy.typing as npt

Num = int | float

__all__ = [
    "plot_brain_connection_figure",
    "save_brain_connection_frames",
]

def _load_surface(file: str | Path):
    '''加载 .surf.gii 文件，提取顶点和面'''
    gii = nib.load(file)
    vertices = gii.darrays[0].data
    faces = gii.darrays[1].data
    return vertices, faces

def _create_mesh(vertices, faces, name):
    '''	创建 plotly 的 Mesh3d 图层'''
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
    '''	判断哪些节点需要显示'''
    if not show_all_nodes:
        row_is_zero = np.any(connectome != 0, axis=1)
        return np.where(row_is_zero)[0]
    else:
        return np.arange(connectome.shape[0])

def _get_centroids_real(niigz_file: str | Path):
    '''读取 NIfTI 图集并计算ROI质心'''
    img = nib.load(niigz_file)
    atlas_data = img.get_fdata()
    affine = img.affine

    roi_labels = np.unique(atlas_data)
    roi_labels = roi_labels[roi_labels != 0]

    centroids_voxel = [center_of_mass((atlas_data == label).astype(int)) for label in roi_labels]
    centroids_real = [np.dot(affine, [*coord, 1])[:3] for coord in centroids_voxel]
    return np.array(centroids_real)

def _add_nodes_to_fig(fig, centroids_real, node_indices, nodes_name, nodes_size, nodes_color):
    '''将节点（球）添加到图中'''
    for i in node_indices:
        fig.add_trace(
            go.Scatter3d(
                x=[centroids_real[i, 0]],
                y=[centroids_real[i, 1]],
                z=[centroids_real[i, 2]],
                mode="markers+text",
                marker={
                    "size": nodes_size[i],
                    "color": nodes_color,
                    "colorscale": "Rainbow",
                    "opacity": 0.8,
                    "line": {"width": 2, "color": "black"},
                },
                text=[nodes_name[i]],
                hoverinfo="text+x+y+z",
                showlegend=False,
            )
        )

def _add_edges_to_fig(fig, connectome, centroids_real, nodes_name, scale_method, line_width, line_color="#ff0000"):
    '''将连接线绘制到图中'''
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
                case "width":
                    each_line_color = line_color if value > 0 else "#0000ff"
                    each_line_width = abs(value / max_strength) * line_width
                case "color":
                    norm_value = value / max_strength
                    each_line_color = mcolors.to_hex(cm.bwr(mcolors.Normalize(vmin=-1, vmax=1)(norm_value)))
                    each_line_width = line_width
                case "width_color" | "color_width":
                    norm_value = value / max_strength
                    each_line_width = abs(norm_value) * line_width
                    each_line_color = mcolors.to_hex(cm.bwr(mcolors.Normalize(vmin=-1, vmax=1)(norm_value)))
                case "":
                    each_line_color = "#ff0000" if value > 0 else "#0000ff"
                    each_line_width = line_width
                case _:
                    raise ValueError("scale_method must be '', 'width', 'color', 'width_color', or 'color_width'")

            connection_line = np.array([centroids_real[i], centroids_real[j], [None] * 3])
            fig.add_trace(
                go.Scatter3d(
                    x=connection_line[:, 0],
                    y=connection_line[:, 1],
                    z=connection_line[:, 2],
                    mode="lines",
                    line={"color": each_line_color, "width": each_line_width},
                    hoverinfo="none",
                    name=f"{nodes_name[i]}-{nodes_name[j]}",
                )
            )

def _finalize_figure(fig):
    '''调整图形布局与视觉样式'''
    fig.update_traces(
        selector={"mode": "markers"},
        marker={"size": 10, "colorscale": "Viridis", "line": {"width": 3, "color": "black"}},
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
    nodes_name: list[str] | None = None,
    nodes_size=None,
    nodes_color: list[str] | None = None,
    output_file: str | Path | None = None,
    scale_method: str = "",
    line_width: Num = 10,
    show_all_nodes: bool = False,
    line_color: str = "#ff0000",
) -> None:
    """绘制大脑连接图，保存在指定的html文件中

    Args:
        connectome (npt.NDArray): 连接矩阵
        lh_surfgii_file (str | Path): 左脑surf.gii文件.
        rh_surfgii_file (str | Path): 右脑surf.gii文件.
        niigz_file (str | Path): 图集nii文件.
        nodes_name (List[str] | None, optional): 节点名称. Defaults to None.
        nodes_size (Num, optional): 节点大小. Defaults to 5.
        nodes_color (List[str] | None, optional): 节点颜色. Defaults to None.
        output_file (str | Path | None, optional): 保存的完整路径及文件名. Defaults to None.
        scale_method (str, optional): 连接scale的形式. Defaults to "".
        line_width (Num, optional): 连接粗细. Defaults to 10.

    Raises:
        ValueError: 参数参数取值不合法时抛出.
    """
    nodes_num = connectome.shape[0]
    if nodes_name is None:
        nodes_name = [f"ROI-{i}" for i in range(nodes_num)]
    if nodes_color is None:
        nodes_color = ["white"] * nodes_num
    if nodes_size is None:
        nodes_size = [5] * nodes_num
    if output_file is None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = op.join(f"./{timestamp}.html")
        print(f"未指定保存路径，默认保存为：{output_file}")

    node_indices = _get_node_indices(connectome, show_all_nodes)
    vertices_L, faces_L = _load_surface(lh_surfgii_file)
    vertices_R, faces_R = _load_surface(rh_surfgii_file)

    mesh_L = _create_mesh(vertices_L, faces_L, "Left Hemisphere")
    mesh_R = _create_mesh(vertices_R, faces_R, "Right Hemisphere")
    fig = go.Figure(data=[mesh_L, mesh_R])

    centroids_real = _get_centroids_real(niigz_file)
    _add_nodes_to_fig(fig, centroids_real, node_indices, nodes_name, nodes_size, nodes_color)
    _add_edges_to_fig(fig, connectome, centroids_real, nodes_name, scale_method, line_width, line_color)
    _finalize_figure(fig)

    fig.write_html(output_file)
    return fig


def save_brain_connection_frames(
    fig: go.Figure,
    output_dir: str,
    n_frames: int = 36
) -> None:
    """
    生成不同角度的静态图片帧，用于制作旋转大脑连接图的 GIF 或视频。

    Args:
        fig (go.Figure): Plotly 的 Figure 对象，包含大脑表面和连接图。
        output_dir (str): 图片保存的文件夹路径，会自动创建文件夹。
        n_frames (int, optional): 旋转帧的数量。默认 36，即每 10 度一帧。
    """
    os.makedirs(output_dir, exist_ok=True)
    angles = np.linspace(0, 360, n_frames, endpoint=False)
    for i, angle in tqdm(enumerate(angles), total=len(angles)):
        camera = dict(
            eye=dict(
                x=2 * np.cos(np.radians(angle)), y=2 * np.sin(np.radians(angle)), z=0.7
            )
        )
        fig.update_layout(scene_camera=camera)
        pio.write_image(fig, f"{output_dir}/frame_{i:03d}.png", width=800, height=800)
    print(f"保存了 {n_frames} 张图片在 {output_dir}")


def main():
    pass


if __name__ == "__main__":
    main()