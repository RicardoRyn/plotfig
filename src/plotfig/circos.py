import numpy as np
import matplotlib.pyplot as plt
import mne
from mne_connectivity.viz import plot_connectivity_circle

import numpy.typing as npt
from typing import Tuple

Num = int | float

__all__ = ["plot_symmetric_circle_figure", "plot_asymmetric_circle_figure"]


def plot_symmetric_circle_figure(
    connectome: npt.NDArray,
    labels: list[str] | None = None,
    node_colors: list[str] | None = None,
    vmin: Num | None = None,
    vmax: Num | None = None,
    figsize: Tuple[Num, Num] = (10, 10),
    labels_fontsize: Num = 15,
    face_color: str = "w",
    nodeedge_color: str = "w",
    text_color: str = "k",
    cmap: str = "bwr",
    linewidth: Num = 1,
    title_name: str = "",
    title_fontsize: Num = 20,
    colorbar: bool = False,
    colorbar_size: Num = 0.2,
    colorbar_fontsize: Num = 10,
    colorbar_pos: Tuple[Num, Num] = (0, 0),
    manual_colorbar: bool = False,
    manual_colorbar_pos: Tuple[Num, Num, Num, Num] = (1, 0.4, 0.01, 0.2),
    manual_cmap: str = "bwr",
    manual_colorbar_name: str = "",
    manual_colorbar_label_fontsize: Num = 10,
    manual_colorbar_fontsize: Num = 10,
    manual_colorbar_rotation: Num = -90,
    manual_colorbar_pad: Num = 20,
    manual_colorbar_draw_border: bool = True,
    manual_colorbar_tickline: bool = False,
    manual_colorbar_nticks: bool = False,
) -> plt.Figure:
    """绘制类circos连接图

    Args:
        connectome (npt.NDArray): 连接矩阵.
        labels (list[str] | None, optional): 节点名称. Defaults to None.
        node_colors (list[str] | None, optional): 节点颜色. Defaults to None.
        vmin (Num | None, optional): 最小值. Defaults to None.
        vmax (Num | None, optional): 最大值. Defaults to None.
        figsize (Tuple[Num, Num], optional): 图大小. Defaults to (10, 10).
        labels_fontsize (Num, optional): 节点名字大小. Defaults to 15.
        face_color (str, optional): 图背景颜色. Defaults to "w".
        nodeedge_color (str, optional): 节点轮廓颜色. Defaults to "w".
        text_color (str, optional): 文本颜色. Defaults to "k".
        cmap (str, optional): colorbar颜色. Defaults to "bwr".
        linewidth (Num, optional): 连接线宽度. Defaults to 1.
        title_name (str, optional): 图标题名称. Defaults to "".
        title_fontsize (Num, optional): 图标题字体大小. Defaults to 20.
        colorbar (bool, optional): 是否绘制colorbar. Defaults to False.
        colorbar_size (Num, optional): colorbar大小. Defaults to 0.2.
        colorbar_fontsize (Num, optional): colorbar字体大小. Defaults to 10.
        colorbar_pos (Tuple[Num, Num], optional): colorbar位置. Defaults to (0, 0).
        manual_colorbar (bool, optional): 高级colorbar. Defaults to False.
        manual_colorbar_pos (Tuple[Num, Num, Num, Num], optional): 高级colorbar位置. Defaults to (1, 0.4, 0.01, 0.2).
        manual_cmap (str, optional): 高级colorbar cmap. Defaults to "bwr".
        manual_colorbar_name (str, optional): 高级colorbar名字. Defaults to "".
        manual_colorbar_label_fontsize (Num, optional): 高级colorbar label字体大小. Defaults to 10.
        manual_colorbar_fontsize (Num, optional): 高级colorbar字体大小. Defaults to 10.
        manual_colorbar_rotation (Num, optional): 高级colorbar旋转. Defaults to -90.
        manual_colorbar_pad (Num, optional): 高级colorbar标题间隔距离. Defaults to 20.
        manual_colorbar_draw_border (bool, optional): 高级colorbar轮廓. Defaults to True.
        manual_colorbar_tickline (bool, optional): 高级colorbar tick线. Defaults to False.
        manual_colorbar_nticks (bool, optional): 高级colorbar tick数量. Defaults to False.

    Returns:
        plt.Figure: _description_
    """
    # 设置默认值
    if vmax is None:
        vmax = np.max((np.max(connectome), -np.min(connectome)))
    if vmin is None:
        vmin = np.min((np.min(connectome), -np.max(connectome)))
    count = connectome.shape[0]
    count_half = int(count / 2)
    if labels is None:
        labels = [str(i) for i in range(count_half)]
    if node_colors is None:
        node_colors = ["#ff8f8f"] * count_half
    labels = labels + [i + " " for i in labels[::-1]]
    node_colors = node_colors + list(node_colors[::-1])
    node_angles = mne.viz.circular_layout(
        labels, labels, group_boundaries=[0, len(labels) / 2]
    )
    # 常规矩阵需要做对称转换
    data_upper_left = connectome[0:count_half, 0:count_half]
    data_down_right = connectome[count_half:count, count_half:count]
    data_down_left = connectome[count_half:count, 0:count_half]
    data_upper_right = connectome[0:count_half, count_half:count]
    data_down_right = data_down_right[::-1][:, ::-1]
    data_down_left = data_down_left[::-1]
    data_upper_right = data_upper_right[:, ::-1]
    connectome_upper = np.concatenate((data_upper_left, data_upper_right), axis=1)
    connectome_lower = np.concatenate((data_down_left, data_down_right), axis=1)
    connectome = np.concatenate((connectome_upper, connectome_lower), axis=0)
    # 画图
    fig, ax = plt.subplots(figsize=figsize, subplot_kw={"polar": True})
    fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plot_connectivity_circle(
        connectome,
        labels,
        node_angles=node_angles,
        node_colors=node_colors,
        fontsize_names=labels_fontsize,
        facecolor=face_color,
        node_edgecolor=nodeedge_color,
        textcolor=text_color,
        colormap=cmap,
        vmin=vmin,
        vmax=vmax,
        linewidth=linewidth,
        title=title_name,
        fontsize_title=title_fontsize,
        colorbar=colorbar,
        colorbar_size=colorbar_size,
        colorbar_pos=colorbar_pos,
        fontsize_colorbar=colorbar_fontsize,
        fig=fig,
        ax=ax,
        interactive=False,
        show=False,
    )
    # 如有需要，禁用自动colorbar，手动生成colorbar
    if manual_colorbar:
        # 手动创建colorbar，拥有更多的设置
        cax = fig.add_axes(manual_colorbar_pos)
        norm = plt.Normalize(vmin=vmin, vmax=vmax)
        sm = plt.cm.ScalarMappable(cmap=manual_cmap, norm=norm)
        sm.set_array([])
        cbar = fig.colorbar(sm, cax=cax)
        cbar.outline.set_visible(manual_colorbar_draw_border)
        cbar.ax.set_ylabel(
            manual_colorbar_name,
            fontsize=manual_colorbar_label_fontsize,
            rotation=manual_colorbar_rotation,
            labelpad=manual_colorbar_pad,
        )
        if not manual_colorbar_tickline:
            cbar.ax.tick_params(length=0)  # 不显示竖线
        cbar.ax.yaxis.set_ticks_position("left")
        cbar.ax.tick_params(labelsize=manual_colorbar_fontsize)
        if manual_colorbar_nticks:
            ticks = np.linspace(vmin, vmax, manual_colorbar_nticks)
            cbar.set_ticks(ticks)
    return fig


def plot_asymmetric_circle_figure(
    connectome: npt.NDArray,
    labels: list[str] | None = None,
    node_colors: list[str] | None = None,
    vmin: Num | None = None,
    vmax: Num | None = None,
    figsize: Tuple[Num, Num] = (10, 10),
    labels_fontsize: Num = 15,
    face_color: str = "w",
    nodeedge_color: str = "w",
    text_color: str = "k",
    cmap: str = "bwr",
    linewidth: Num = 1,
    title_name: str = "",
    title_fontsize: Num = 20,
    colorbar: bool = False,
    colorbar_size: Num = 0.2,
    colorbar_fontsize: Num = 10,
    colorbar_pos: Tuple[Num, Num] = (0, 0),
    manual_colorbar: bool = False,
    manual_colorbar_pos: Tuple[Num, Num, Num, Num] = (1, 0.4, 0.01, 0.2),
    manual_cmap: str = "bwr",
    manual_colorbar_name: str = "",
    manual_colorbar_label_fontsize: Num = 10,
    manual_colorbar_fontsize: Num = 10,
    manual_colorbar_rotation: Num = -90,
    manual_colorbar_pad: Num = 20,
    manual_colorbar_draw_border: bool = True,
    manual_colorbar_tickline: bool = False,
    manual_colorbar_nticks: bool = False,
) -> plt.Figure:
    """绘制类circos连接图

    Args:
        connectome (npt.NDArray): 连接矩阵.
        labels (list[str] | None, optional): 节点名称. Defaults to None.
        node_colors (list[str] | None, optional): 节点颜色. Defaults to None.
        vmin (Num | None, optional): 最小值. Defaults to None.
        vmax (Num | None, optional): 最大值. Defaults to None.
        figsize (Tuple[Num, Num], optional): 图大小. Defaults to (10, 10).
        labels_fontsize (Num, optional): 节点名字大小. Defaults to 15.
        face_color (str, optional): 图背景颜色. Defaults to "w".
        nodeedge_color (str, optional): 节点轮廓颜色. Defaults to "w".
        text_color (str, optional): 文本颜色. Defaults to "k".
        cmap (str, optional): colorbar颜色. Defaults to "bwr".
        linewidth (Num, optional): 连接线宽度. Defaults to 1.
        title_name (str, optional): 图标题名称. Defaults to "".
        title_fontsize (Num, optional): 图标题字体大小. Defaults to 20.
        colorbar (bool, optional): 是否绘制colorbar. Defaults to False.
        colorbar_size (Num, optional): colorbar大小. Defaults to 0.2.
        colorbar_fontsize (Num, optional): colorbar字体大小. Defaults to 10.
        colorbar_pos (Tuple[Num, Num], optional): colorbar位置. Defaults to (0, 0).
        manual_colorbar (bool, optional): 高级colorbar. Defaults to False.
        manual_colorbar_pos (Tuple[Num, Num, Num, Num], optional): 高级colorbar位置. Defaults to (1, 0.4, 0.01, 0.2).
        manual_cmap (str, optional): 高级colorbar cmap. Defaults to "bwr".
        manual_colorbar_name (str, optional): 高级colorbar名字. Defaults to "".
        manual_colorbar_label_fontsize (Num, optional): 高级colorbar label字体大小. Defaults to 10.
        manual_colorbar_fontsize (Num, optional): 高级colorbar字体大小. Defaults to 10.
        manual_colorbar_rotation (Num, optional): 高级colorbar旋转. Defaults to -90.
        manual_colorbar_pad (Num, optional): 高级colorbar标题间隔距离. Defaults to 20.
        manual_colorbar_draw_border (bool, optional): 高级colorbar轮廓. Defaults to True.
        manual_colorbar_tickline (bool, optional): 高级colorbar tick线. Defaults to False.
        manual_colorbar_nticks (bool, optional): 高级colorbar tick数量. Defaults to False.

    Returns:
        plt.Figure: _description_
    """
    # 设置默认值
    if vmax is None:
        vmax = np.max((np.max(connectome), -np.min(connectome)))
    if vmin is None:
        vmin = np.min((np.min(connectome), -np.max(connectome)))
    count = connectome.shape[0]
    if labels is None:
        labels = [str(i) for i in range(count)]
    if node_colors is None:
        node_colors = ["#ff8f8f"] * count
    node_angles = mne.viz.circular_layout(labels, labels)
    # 画图
    fig, ax = plt.subplots(figsize=figsize, subplot_kw={"polar": True})
    fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plot_connectivity_circle(
        connectome,
        labels,
        node_angles=node_angles,
        node_colors=node_colors,
        fontsize_names=labels_fontsize,
        facecolor=face_color,
        node_edgecolor=nodeedge_color,
        textcolor=text_color,
        colormap=cmap,
        vmin=vmin,
        vmax=vmax,
        linewidth=linewidth,
        title=title_name,
        fontsize_title=title_fontsize,
        colorbar=colorbar,
        colorbar_size=colorbar_size,
        colorbar_pos=colorbar_pos,
        fontsize_colorbar=colorbar_fontsize,
        fig=fig,
        ax=ax,
        interactive=False,
        show=False,
    )
    # 如有需要，禁用自动colorbar，手动生成colorbar
    if manual_colorbar:
        # 手动创建colorbar，拥有更多的设置
        cax = fig.add_axes(manual_colorbar_pos)
        norm = plt.Normalize(vmin=vmin, vmax=vmax)
        sm = plt.cm.ScalarMappable(cmap=manual_cmap, norm=norm)
        sm.set_array([])
        cbar = fig.colorbar(sm, cax=cax)
        cbar.outline.set_visible(manual_colorbar_draw_border)
        cbar.ax.set_ylabel(
            manual_colorbar_name,
            fontsize=manual_colorbar_label_fontsize,
            rotation=manual_colorbar_rotation,
            labelpad=manual_colorbar_pad,
        )
        if not manual_colorbar_tickline:
            cbar.ax.tick_params(length=0)  # 不显示竖线
        cbar.ax.yaxis.set_ticks_position("left")
        cbar.ax.tick_params(labelsize=manual_colorbar_fontsize)
        if manual_colorbar_nticks:
            ticks = np.linspace(vmin, vmax, manual_colorbar_nticks)
            cbar.set_ticks(ticks)
    return fig
