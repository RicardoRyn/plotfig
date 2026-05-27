from typing import Any, Sequence

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from mpl_toolkits.axes_grid1 import make_axes_locatable

__all__ = ["plot_matrix_figure"]


def plot_matrix_figure(
    data: np.ndarray,
    ax: Axes | None = None,
    row_labels_name: Sequence[str] | None = None,
    col_labels_name: Sequence[str] | None = None,
    cmap: str = "bwr",
    vmin: int | float | None = None,
    vmax: int | float | None = None,
    aspect: str = "equal",
    colorbar: bool = True,
    colorbar_label_name: str = "",
    colorbar_pad: int | float = 0.1,
    colorbar_label_fontsize: int | float = 10,
    colorbar_tick_fontsize: int | float = 10,
    colorbar_tick_rotation: int | float = 0,
    row_labels_fontsize: int | float = 10,
    col_labels_fontsize: int | float = 10,
    x_rotation: int | float = 60,
    title_name: str = "",
    title_fontsize: int | float = 15,
    title_pad: int | float = 20,
    diag_border: bool = False,
    xlabel: str | None = None,
    ylabel: str | None = None,
    **imshow_kwargs: Any,
) -> Axes:
    """
    将矩阵绘制为热图，可选显示标签、颜色条和标题。

    Args:
        data (np.ndarray): 形状为 (N, M) 的二维数组，用于显示矩阵。
        ax (Axes | None): 要绘图的 Matplotlib 坐标轴。如果为 None，则使用当前坐标轴。
        row_labels_name (Sequence[str] | None): 行标签列表。
        col_labels_name (Sequence[str] | None): 列标签列表。
        cmap (str): 矩阵使用的颜色映射。
        vmin (int | float | None): 颜色缩放的最小值，默认使用 data.min()。
        vmax (int | float | None): 颜色缩放的最大值，默认使用 data.max()。
        aspect (str): 图像的纵横比，通常为 "equal" 或 "auto"。
        colorbar (bool): 是否显示颜色条。
        colorbar_label_name (str): 颜色条的标签。
        colorbar_pad (int | float): 颜色条与矩阵之间的间距。
        colorbar_label_fontsize (int | float): 颜色条标签的字体大小。
        colorbar_tick_fontsize (int | float): 颜色条刻度的字体大小。
        colorbar_tick_rotation (int | float): 颜色条刻度标签的旋转角度。
        row_labels_fontsize (int | float): 行标签的字体大小。
        col_labels_fontsize (int | float): 列标签的字体大小。
        x_rotation (int | float): x 轴（列）标签的旋转角度。
        title_name (str): 图表标题。
        title_fontsize (int | float): 标题的字体大小。
        title_pad (int | float): 标题上方的间距。
        diag_border (bool): 是否绘制对角线单元格边框。
        xlabel (str | None): X轴的整体标签名称。
        ylabel (str | None): Y轴的整体标签名称。
        **imshow_kwargs (Any): 传递给 `imshow()` 的其他关键字参数。

    Returns:
        Axes: 绘图的坐标轴对象。
    """

    ax = ax or plt.gca()
    vmin = vmin if vmin is not None else np.min(data)
    vmax = vmax if vmax is not None else np.max(data)

    im = ax.imshow(
        data, cmap=cmap, vmin=vmin, vmax=vmax, aspect=aspect, **imshow_kwargs
    )
    ax.set_title(title_name, fontsize=title_fontsize, pad=title_pad)

    # 设置X轴和Y轴标签
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    if diag_border:
        for i in range(data.shape[0]):
            ax.add_patch(
                plt.Rectangle(
                    (i - 0.5, i - 0.5), 1, 1, fill=False, edgecolor="black", lw=0.5
                )
            )

    if col_labels_name is not None:
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_xticklabels(
            col_labels_name,
            fontsize=col_labels_fontsize,
            rotation=x_rotation,
            ha="right",
            rotation_mode="anchor",
        )

    if row_labels_name is not None:
        ax.set_yticks(np.arange(data.shape[0]))
        ax.set_yticklabels(row_labels_name, fontsize=row_labels_fontsize)

    if colorbar:
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=colorbar_pad)
        cbar = ax.figure.colorbar(im, cax=cax)
        cbar.ax.set_ylabel(
            colorbar_label_name,
            rotation=-90,
            va="bottom",
            fontsize=colorbar_label_fontsize,
        )
        cbar.ax.tick_params(
            labelsize=colorbar_tick_fontsize, rotation=colorbar_tick_rotation
        )
        # Match colorbar height to the main plot
        ax_pos = ax.get_position()
        cax.set_position(
            [cax.get_position().x0, ax_pos.y0, cax.get_position().width, ax_pos.height]
        )

    return ax
