import os.path as op
import datetime
import numpy as np
import pandas as pd
import nibabel as nib
from scipy.ndimage import center_of_mass
import plotly.graph_objects as go
import matplotlib.colors as mcolors
import matplotlib.cm as cm

from pathlib import Path
import numpy.typing as npt

Num = int | float


def plot_brain_connection_figure(
    connectome: npt.NDArray,
    lh_surfgii_file: str | Path | None = None,
    rh_surfgii_file: str | Path | None = None,
    niigz_file: str | Path | None = None,
    nodes_name: list[str] | None = None,
    nodes_size: Num = 5,
    nodes_color: list[str] | None = None,
    output_file: str | Path | None = None,
    scale_method: str = "",
    line_width: Num = 10,
) -> None:
    """绘制大脑连接图，保存在指定的html文件中

    Args:
        connectome (npt.NDArray): 连接矩阵
        lh_surfgii_file (str | Path | None, optional): 左脑surf.gii文件. Defaults to None.
        rh_surfgii_file (str | Path | None, optional): 右脑surf.gii文件. Defaults to None.
        niigz_file (str | Path | None, optional): 图集nii文件. Defaults to None.
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
    # 默认参数
    current_dir = op.dirname(__file__)
    neuromaps_data_dir = op.join(current_dir, "data/neurodata")

    if lh_surfgii_file is None:
        lh_surfgii_file = op.join(
            neuromaps_data_dir, "surfaces/macaque_NMT2/L.mid_surface.surf.gii"
        )
    if rh_surfgii_file is None:
        rh_surfgii_file = op.join(
            neuromaps_data_dir, "surfaces/macaque_NMT2/R.mid_surface.surf.gii"
        )
    if niigz_file is None:
        niigz_file = op.join(
            neuromaps_data_dir,
            "volumes/macaque_NMT2/CHARM5_add_13_sgms_asym.nii.gz",
        )
        df = pd.read_csv(
            op.join(current_dir, "data/atlas_tables/macaque_charm5_add_13_sgms.csv")
        )
        nodes_name = df["ROIs_name"].values
    else:
        if nodes_name is None:
            nodes_name = [f"ROI-{i}" for i in range(nodes_num)]
    if nodes_color is None:
        nodes_color = ["white"] * len(nodes_name)
    if output_file is None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = op.join(f"./{timestamp}.html")
        print(f"由于没有指定保存路径，将默认保存为当前目录下 {timestamp}.html 文件中")

    # 加载suface文件
    vertices_L = nib.load(lh_surfgii_file).darrays[0].data
    faces_L = nib.load(lh_surfgii_file).darrays[1].data
    vertices_R = nib.load(rh_surfgii_file).darrays[0].data
    faces_R = nib.load(rh_surfgii_file).darrays[1].data
    # 左半球
    mesh_L = go.Mesh3d(
        x=vertices_L[:, 0],
        y=vertices_L[:, 1],
        z=vertices_L[:, 2],
        i=faces_L[:, 0],
        j=faces_L[:, 1],
        k=faces_L[:, 2],
        color="white",
        opacity=0.1,
        flatshading=True,
        lighting={"ambient": 0.7, "diffuse": 0.3},
        name="Left Hemisphere",
    )
    # 右半球
    mesh_R = go.Mesh3d(
        x=vertices_R[:, 0],
        y=vertices_R[:, 1],
        z=vertices_R[:, 2],
        i=faces_R[:, 0],
        j=faces_R[:, 1],
        k=faces_R[:, 2],
        color="white",
        opacity=0.1,
        flatshading=True,
        lighting={"ambient": 0.7, "diffuse": 0.3},
        name="Right Hemisphere",
    )
    fig = go.Figure(data=[mesh_L, mesh_R])  # 同时添加两个Mesh

    # 读取图集文件并提取ROI质心
    atlas_data = nib.load(niigz_file).get_fdata()
    affine = nib.load(niigz_file).affine
    # 获取所有ROI标签（排除背景0）
    roi_labels = np.unique(atlas_data)
    roi_labels = roi_labels[roi_labels != 0]
    # 计算每个ROI的质心（体素坐标系）
    centroids_voxel = []
    for label in roi_labels:
        mask = (atlas_data == label).astype(int)
        com = center_of_mass(mask)  # 这是一个xyz坐标
        centroids_voxel.append(com)
    # 将质心从体素坐标转换为真实空间坐标
    centroids_real = []
    for coord in centroids_voxel:
        # 转换为齐次坐标并应用仿射变换
        voxel_homogeneous = np.array([coord[0], coord[1], coord[2], 1])
        real_coord = np.dot(affine, voxel_homogeneous)[:3]
        centroids_real.append(real_coord)
    centroids_real = np.array(centroids_real)

    # 绘制节点
    fig.add_trace(
        go.Scatter3d(
            x=centroids_real[:, 0],
            y=centroids_real[:, 1],
            z=centroids_real[:, 2],
            mode="markers+text",
            marker={
                "size": nodes_size,  # 球体大小
                "color": nodes_color,  # 根据ROI标签分配颜色
                "colorscale": "Rainbow",  # 颜色映射方案
                "opacity": 0.8,
                "line": {"width": 2, "color": "black"},  # 球体边框
            },
            text=[f"{name}" for name in nodes_name],  # 悬停显示标签
            hoverinfo="text+x+y+z",
            showlegend=False,  # 显示在图例中
        )
    )

    # 计算最大连接强度
    if np.all(connectome == 0):
        pass
    else:
        connectome_without_0 = connectome.ravel()[(connectome.ravel() != 0)]
        max_strength = np.abs(connectome_without_0).max()
        # min_strength = np.abs(connectome_without_0).min()

        for i in range(nodes_num):
            for j in range(i + 1, nodes_num):
                value = connectome[i, j]
                if value == 0:
                    continue

                match scale_method:
                    case "width":
                        if value > 0:
                            each_line_color = "#ff0000"
                            each_line_width = (value / max_strength) * line_width
                        elif value < 0:
                            each_line_color = "#0000ff"
                            each_line_width = (-value / max_strength) * line_width
                    case "color":
                        value = value / max_strength  # 缩放到[-1, 1]
                        each_line_width = line_width
                        each_line_color = mcolors.to_hex(
                            cm.bwr(mcolors.Normalize(vmin=-1, vmax=1)(value))
                        )
                        # each_line_color = eval(f"mcolors.to_hex(cm.{cmap}(mcolors.Normalize(vmin=-1, vmax=1)(value)))")
                    case "width_color" | "color_width":
                        value = value / max_strength  # 缩放到[-1, 1]
                        if value > 0:
                            each_line_width = value * line_width
                        elif value < 0:
                            each_line_width = -value * line_width
                        each_line_color = mcolors.to_hex(
                            cm.bwr(mcolors.Normalize(vmin=-1, vmax=1)(value))
                        )
                        # each_line_color = eval(f"mcolors.to_hex(cm.{cmap}(mcolors.Normalize(vmin=-1, vmax=1)(value)))")
                    case "":
                        each_line_width = line_width
                        if value > 0:
                            each_line_color = "#ff0000"
                        elif value < 0:
                            each_line_color = "#0000ff"
                    case _:
                        raise ValueError(
                            "参数 scale_method 必须是 '', 'width', 'color', 'width_color' 或 'color_width'"
                        )

                # 创建单个线段的坐标数据（包含None分隔符）
                connection_line = np.array(
                    [
                        centroids_real[i],
                        centroids_real[j],
                        [None] * 3,  # 添加分隔符确保线段独立
                    ]
                )
                # 添加单独trace
                fig.add_trace(
                    go.Scatter3d(
                        x=connection_line[:, 0],
                        y=connection_line[:, 1],
                        z=connection_line[:, 2],
                        mode="lines",
                        line={
                            "color": each_line_color,
                            "width": each_line_width,  # 动态设置线宽
                        },
                        hoverinfo="none",
                        name=f"{nodes_name[i]}-{nodes_name[j]}",
                    )
                )

    # 原质心球体代码保持不变（建议调整颜色增强对比度）
    fig.update_traces(
        selector={"mode": "markers"},  # 仅更新质心球体
        marker={
            "size": 10,  # 增大球体尺寸
            "colorscale": "Viridis",  # 改用高对比度色阶
            "line": {"width": 3, "color": "black"},
        },
    )
    # 设置布局
    fig.update_layout(
        title="Connection",
        scene={
            "xaxis": {"showbackground": False, "visible": False},
            "yaxis": {"showbackground": False, "visible": False},
            "zaxis": {"showbackground": False, "visible": False},
            "aspectmode": "data",  # 保持坐标轴比例一致
        },
        margin={"l": 0, "r": 0, "b": 0, "t": 30},
    )
    # 显示或保存为HTML
    fig.write_html(output_file)  # 导出为交互式网页

    return


def main():
    connectome = pd.read_csv(r"d:/desktop/BG.csv", header=None, index_col=None).values
    lh_surfgii_file = r"D:\Desktop\BG.L.midthickness.32k_fs_LR.surf.gii"
    rh_surfgii_file = r"D:\Desktop\BG.R.midthickness.32k_fs_LR.surf.gii"
    niigz_file = r"D:\Desktop\macaque_Interoceptive_processing_network.nii.gz"
    output_file = "d:/desktop/rm_rjx.html"
    plot_brain_connection_figure(
        connectome,
        lh_surfgii_file=lh_surfgii_file,
        rh_surfgii_file=rh_surfgii_file,
        niigz_file=niigz_file,
        output_file=output_file,
        scale_method="color_width",
        line_width=20,
    )


if __name__ == "__main__":
    main()
