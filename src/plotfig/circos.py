# 标准库
from typing import Literal, Any

# 第三方库
import numpy as np
from numpy.typing import NDArray
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.projections.polar import PolarAxes
from matplotlib.axes import Axes
from pycirclize import Circos
from loguru import logger

# 项目内模块
from plotfig.utils.matrix import (
    is_symmetric_square,
)
from plotfig.utils.color import (
    gen_hex_colors,
    gen_cmap,
    value_to_hex,
)


__all__ = ["plot_circos_figure"]


def _gen_node_name(connectome) -> list[str]:
    node_names = [f"Node_{i + 1}" for i in range(connectome.shape[0])]
    return node_names


def _gen_edges(connectome) -> list[tuple[Any, Any, Any]]:
    i, j = np.triu_indices_from(connectome, k=1)
    edges = [(u, v, connectome[u, v]) for u, v in zip(i, j) if connectome[u, v] != 0]
    return edges


def _gen_sym_sectors(node_names) -> dict[str, float]:
    node_num = len(node_names)
    sectors = {}
    # gap1
    sectors["_gap1"] = node_num / (35 * 2)
    # 左半球
    for name in node_names[: int(node_num / 2)]:
        sectors[name] = 1
    # gap2, gap3
    sectors["_gap2"] = node_num / (35 * 2)
    sectors["_gap3"] = node_num / (35 * 2)
    # 右半球
    for name in node_names[int(node_num / 2) :]:
        sectors[name] = 1
    # gap4
    sectors["_gap4"] = node_num / (35 * 2)
    return sectors


def _process_sym(
    connectome, node_names, node_colors
) -> tuple[NDArray[Any], list[str], list[str]]:
    """绘制对称图需做对称转换"""
    count = connectome.shape[0]
    count_half = int(count / 2)

    # connectome 处理
    # 分块
    data_upper_left = connectome[0:count_half, 0:count_half]
    data_down_right = connectome[count_half:count, count_half:count]
    data_down_left = connectome[count_half:count, 0:count_half]
    data_upper_right = connectome[0:count_half, count_half:count]
    # 翻转
    data_upper_left = data_upper_left[::-1][:, ::-1]
    data_upper_right = data_upper_right[::-1]
    data_down_left = data_down_left[:, ::-1]
    # 组合
    connectome_upper = np.concatenate((data_upper_left, data_upper_right), axis=1)
    connectome_lower = np.concatenate((data_down_left, data_down_right), axis=1)
    connectome = np.concatenate((connectome_upper, connectome_lower), axis=0)

    # node_names 处理
    node_names = node_names[:count_half][::-1] + node_names[count_half:]

    # node_colors 处理
    node_colors = node_colors[:count_half][::-1] + node_colors[count_half:]

    return connectome, node_names, node_colors


def plot_circos_figure(
    connectome: NDArray,
    ax: Axes | None = None,
    symmetric: bool = True,
    node_names: list[str] | None = None,
    node_colors: list[str] | None = None,
    node_space: float = 0.0,
    node_label_fontsize: int = 10,
    node_label_orientation: Literal["vertical", "horizontal"] = "horizontal",
    vmin: float | None = None,
    vmax: float | None = None,
    cmap: str | None = None,
    edge_color: str = "red",
    edge_alpha: float = 1.0,
    colorbar: bool = True,
    colorbar_orientation: Literal["vertical", "horizontal"] = "vertical",
    colorbar_label: str = "",
) -> Figure | PolarAxes:
    """绘制脑连接组的环形图（Circos plot）。

    Args:
        connectome (NDArray): 脑连接矩阵，必须为对称方阵。形状为(n, n)，其中n为脑区数量
        ax (Axes | None, optional): matplotlib的极坐标轴对象，如果提供则在此轴上绘图。默认为None
        symmetric (bool, optional): 是否为对称布局（用于左右脑半球数据）。默认为True
        node_names (list[str] | None, optional): 脑区名称列表，长度应与connectome的维度一致。默认为None时自动生成"Node_1", "Node_2"...格式的名称
        node_colors (list[str] | None, optional): 脑区颜色列表，长度应与脑区数量一致。默认为None时自动生成颜色
        node_space (float, optional): 脑区间间隔角度（度）。默认为0.0
        node_label_fontsize (int, optional): 脑区标签字体大小。默认为10
        node_label_orientation (Literal["vertical", "horizontal"], optional): 脑区标签方向。默认为"horizontal"
        vmin (float | None, optional): 连接强度颜色映射的最小值。默认为None时根据数据自动确定
        vmax (float | None, optional): 连接强度颜色映射的最大值。默认为None时根据数据自动确定
        cmap (str | None, optional): 颜色映射表名称。默认为None时根据edge_color生成
        edge_color (str, optional): 连线颜色，当cmap为None时使用此颜色生成颜色映射。默认为"red"
        edge_alpha (float, optional): 连线透明度，范围0-1。默认为1.0（不透明）
        colorbar (bool, optional): 是否显示颜色条。默认为True
        colorbar_orientation (Literal["vertical", "horizontal"], optional): 颜色条方向。默认为"vertical"
        colorbar_label (str, optional): 颜色条标签文本。默认为空字符串

    Raises:
        ValueError: 当connectome不是对称矩阵时抛出
        ValueError: 当vmin大于vmax时抛出
        TypeError: 当提供的ax不是PolarAxes类型时抛出

    Returns:
        Figure | Axes: 如果ax为None则返回Figure对象，否则返回Axes对象
    """

    # 检查输入矩阵，指定cmap
    if not is_symmetric_square(connectome):
        raise ValueError("connectome 不是对称矩阵")
    if np.all(connectome == 0):
        logger.warning("connectome 矩阵所有元素均为0，可能没有有效连接数据")
        vmax = float(0 if vmax is None else vmax)
        vmin = float(0 if vmin is None else vmin)
        colormap = gen_cmap(edge_color) if cmap is None else plt.get_cmap(cmap)
    elif np.any(connectome < 0):
        logger.warning(
            "由于 connectome 存在负值，连线颜色无法自定义，只能正值显示红色，负值显示蓝色"
        )
        max_strength = np.abs(connectome[connectome != 0]).max()
        vmax = float(max_strength if vmax is None else vmax)
        vmin = float(-max_strength if vmin is None else vmin)
        colormap = plt.get_cmap("bwr")
    else:
        vmin = float(connectome.min() if vmin is None else vmin)
        vmax = float(connectome.max() if vmax is None else vmax)
        colormap = gen_cmap(edge_color) if cmap is None else plt.get_cmap(cmap)
    if vmin > vmax:
        raise ValueError(f"目前{vmin=}，而{vmax=}。但是vmin不得大于vmax，请检查数据")
    norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

    # 获取数据信息
    node_num = connectome.shape[0]
    node_names = _gen_node_name(connectome) if node_names is None else node_names

    # 由于pycirclize的特性，sector顺序只能为顺时针，因此需要将数据进行翻转
    connectome = np.flip(connectome)
    node_names = node_names[::-1]
    if symmetric:
        # 画对称图需额外做半球翻转处理
        node_colors = (
            gen_hex_colors(int(node_num / 2)) * 2
            if node_colors is None
            else node_colors[::-1]
        )
        connectome, node_names, node_colors = _process_sym(
            connectome, node_names, node_colors
        )
        sectors = _gen_sym_sectors(node_names)
    else:
        node_colors = (
            gen_hex_colors(node_num) if node_colors is None else node_colors[::-1]
        )
        sectors = {node_name: 1 for node_name in node_names}

    edges = _gen_edges(connectome)
    name2color = {
        node_name: node_color for node_name, node_color in zip(node_names, node_colors)
    }
    circos = Circos(sectors, space=node_space)

    # 设置扇区
    for sector in circos.sectors:
        if sector.name.startswith("_gap"):
            continue
        sector.text(sector.name, size=node_label_fontsize, orientation=node_label_orientation)
        track = sector.add_track((95, 100))
        track.axis(fc=name2color[sector.name])

    # 设置连接
    for edge in edges:
        color = value_to_hex(edge[2], colormap, norm)
        circos.link(
            (node_names[edge[0]], 0.45, 0.55),
            (node_names[edge[1]], 0.55, 0.45),
            color=color,
            alpha=edge_alpha,
        )

    # colorbar
    if colorbar:
        if colorbar_orientation == "vertical":
            orientation = "vertical"
            bounds = (1.1, 0.29, 0.02, 0.4)
            label_kws = dict(size=12, rotation=270, labelpad=20)
        else:
            orientation = "horizontal"
            bounds = (0.3, -0.1, 0.4, 0.03)
            label_kws = dict(size=12)
        circos.colorbar(
            bounds=bounds,
            orientation=orientation,
            vmin=vmin,
            vmax=vmax,
            cmap=colormap,
            label=colorbar_label,
            label_kws=label_kws,
            tick_kws=dict(labelsize=12),
        )

    # 画图
    if ax is None:
        fig = circos.plotfig()
        return fig
    else:
        if isinstance(ax, PolarAxes):
            circos.plotfig(ax=ax)
            return ax
        else:
            raise ValueError("ax 不是 PolarAxes 类型")
