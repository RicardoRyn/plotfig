from typing import Literal, Sequence, TypeAlias

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import PolyCollection
from matplotlib.colors import Colormap, LinearSegmentedColormap
from matplotlib.ticker import (
    FormatStrFormatter,
    FuncFormatter,
    MultipleLocator,
    ScalarFormatter,
)
from scipy import stats

Num: TypeAlias = int | float | np.integer | np.floating
StatsMethod: TypeAlias = Literal["spearman", "pearson"]
AxisFormat: TypeAlias = Literal["normal", "sci", "1f", "percent"]

__all__ = ["plot_correlation_figure"]


def plot_correlation_figure(
    data1: Sequence[Num] | np.ndarray,
    data2: Sequence[Num] | np.ndarray,
    ax: Axes | None = None,
    stats_method: StatsMethod = "spearman",
    ci: bool = False,
    ci_color: str = "gray",
    dots_color: str | list[str] = "steelblue",
    dots_size: int | list[int] = 10,
    dots_edgecolor: str | list[str] = "gray",
    line_color: str = "r",
    title_name: str = "",
    title_fontsize: int = 12,
    title_pad: int = 10,
    x_label_name: str = "",
    x_label_fontsize: int = 10,
    x_tick_fontsize: int = 8,
    x_tick_rotation: int = 0,
    x_major_locator: float | None = None,
    x_max_tick_to_value: float | None = None,
    x_format: AxisFormat = "normal",
    y_label_name: str = "",
    y_label_fontsize: int = 10,
    y_tick_fontsize: int = 8,
    y_tick_rotation: int = 0,
    y_major_locator: float | None = None,
    y_max_tick_to_value: float | None = None,
    y_format: AxisFormat = "sci",
    asterisk_fontsize: int = 10,
    show_p_value: bool = False,
    hexbin: bool = False,
    hexbin_cmap: Colormap | None = None,
    hexbin_gridsize: int = 50,
    xlim: list[Num] | tuple[Num, Num] | None = None,
    ylim: list[Num] | tuple[Num, Num] | None = None,
) -> Axes | PolyCollection:
    """
    绘制两个数据集之间的相关性图，支持线性回归、置信区间和统计方法（Spearman 或 Pearson）。

    Args:
        data1 (Sequence[Num] | np.ndarray): 第一个数据集。
        data2 (Sequence[Num] | np.ndarray): 第二个数据集。
        ax (Axes | None, optional): matplotlib 的 Axes 对象。默认为 None（使用当前 Axes）。
        stats_method (StatsMethod, optional): 相关性统计方法，支持 "spearman" 和 "pearson"。默认为 "spearman"。
        ci (bool, optional): 是否绘制置信区间带。默认为 False。
        ci_color (str, optional): 置信区间带颜色。默认为 "gray"。
        dots_color (str | list[str], optional): 散点颜色。默认为 "steelblue"。
        dots_size (int | list[int], optional): 散点大小。默认为 10。
        dots_edgecolor (str | list[str], optional): 散点边框颜色。默认为 "gray"。
        line_color (str, optional): 回归线颜色。默认为 "r"（红色）。
        title_name (str, optional): 图形标题。默认为空字符串。
        title_fontsize (int, optional): 标题字体大小。默认为 12。
        title_pad (int, optional): 标题与图形之间的间距。默认为 10。
        x_label_name (str, optional): X 轴标签名称。默认为空字符串。
        x_label_fontsize (int, optional): X 轴标签字体大小。默认为 10。
        x_tick_fontsize (int, optional): X 轴刻度标签字体大小。默认为 8。
        x_tick_rotation (int, optional): X 轴刻度标签旋转角度。默认为 0。
        x_major_locator (float | None, optional): X 轴主刻度间隔。默认为 None。
        x_max_tick_to_value (float | None, optional): X 轴最大显示刻度值。默认为 None。
        x_format (AxisFormat, optional): X 轴格式化方式，支持 "normal"、"sci"、"1f"、"percent"。默认为 "normal"。
        y_label_name (str, optional): Y 轴标签名称。默认为空字符串。
        y_label_fontsize (int, optional): Y 轴标签字体大小。默认为 10。
        y_tick_fontsize (int, optional): Y 轴刻度标签字体大小。默认为 8。
        y_tick_rotation (int, optional): Y 轴刻度标签旋转角度。默认为 0。
        y_major_locator (float | None, optional): Y 轴主刻度间隔。默认为 None。
        y_max_tick_to_value (float | None, optional): Y 轴最大显示刻度值。默认为 None。
        y_format (AxisFormat, optional): Y 轴格式化方式，支持 "normal"、"sci"、"1f"、"percent"。默认为 "sci"。
        asterisk_fontsize (int, optional): 显著性星号字体大小。默认为 10。
        show_p_value (bool, optional): 是否显示 p 值；否则显示显著性星号。默认为 False。
        hexbin (bool, optional): 是否使用六边形箱图。默认为 False。
        hexbin_cmap (Colormap | None, optional): 六边形箱图的颜色映射。默认为 None。
        hexbin_gridsize (int, optional): 六边形箱图网格大小。默认为 50。
        xlim (list[Num] | tuple[Num, Num] | None, optional): X 轴范围限制。默认为 None。
        ylim (list[Num] | tuple[Num, Num] | None, optional): Y 轴范围限制。默认为 None。

    Returns:
        Axes | PolyCollection: 默认返回 Axes；当 hexbin=True 时返回 hexbin 对象。
    """

    def set_axis(
        ax: Axes,
        axis: Literal["x", "y"],
        label: str,
        labelsize: Num,
        ticksize: Num,
        rotation: Num,
        locator: float | None,
        max_tick_value: float | None,
        fmt: AxisFormat,
        lim: list[Num] | tuple[Num, Num] | None,
    ) -> None:
        if axis == "x":
            set_label = ax.set_xlabel
            get_ticks = ax.get_xticks
            set_ticks = ax.set_xticks
            axis_formatter = ax.xaxis.set_major_formatter
            axis_major_locator = ax.xaxis.set_major_locator
        else:
            set_label = ax.set_ylabel
            get_ticks = ax.get_yticks
            set_ticks = ax.set_yticks
            axis_formatter = ax.yaxis.set_major_formatter
            axis_major_locator = ax.yaxis.set_major_locator

        # 设置轴范围
        if lim is not None:
            if axis == "x":
                ax.set_xlim(lim)
            else:
                ax.set_ylim(lim)

        set_label(label, fontsize=labelsize)
        ax.tick_params(axis=axis, which="major", labelsize=ticksize, rotation=rotation)
        if locator is not None:
            axis_major_locator(MultipleLocator(locator))
        if max_tick_value is not None:
            set_ticks([i for i in get_ticks() if i <= max_tick_value])

        if fmt == "sci":
            formatter = ScalarFormatter(useMathText=True)
            formatter.set_powerlimits((-2, 2))
            axis_formatter(formatter)
        elif fmt == "1f":
            axis_formatter(FormatStrFormatter("%.1f"))
        elif fmt == "percent":
            axis_formatter(FuncFormatter(lambda x, pos: f"{x:.0%}"))

    if ax is None:
        ax = plt.gca()

    A = np.asarray(data1)
    B = np.asarray(data2)

    slope, intercept, r_value, p_value, _ = stats.linregress(A, B)
    x_seq = np.linspace(A.min(), A.max(), 100)
    y_pred = slope * x_seq + intercept

    if hexbin:
        if hexbin_cmap is None:
            hexbin_cmap = LinearSegmentedColormap.from_list(
                "custom", ["#ffffff", "#4573a5"]
            )
        hb = ax.hexbin(A, B, gridsize=hexbin_gridsize, cmap=hexbin_cmap)
    else:
        ax.scatter(A, B, c=dots_color, s=dots_size, edgecolors=dots_edgecolor)
    ax.plot(x_seq, y_pred, line_color, lw=1)

    if ci:
        n = len(A)
        dof = n - 2
        t_val = stats.t.ppf(0.975, dof)
        x_mean = A.mean()
        residuals = B - (slope * A + intercept)
        s_err = np.sqrt(np.sum(residuals**2) / dof)
        SSxx = np.sum((A - x_mean) ** 2)
        conf_interval = t_val * s_err * np.sqrt(1 / n + (x_seq - x_mean) ** 2 / SSxx)
        ax.fill_between(
            x_seq,
            y_pred - conf_interval,
            y_pred + conf_interval,
            color=ci_color,
            alpha=0.3,
        )

    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(title_name, fontsize=title_fontsize, pad=title_pad)

    set_axis(
        ax,
        "x",
        x_label_name,
        x_label_fontsize,
        x_tick_fontsize,
        x_tick_rotation,
        x_major_locator,
        x_max_tick_to_value,
        x_format,
        xlim,
    )
    set_axis(
        ax,
        "y",
        y_label_name,
        y_label_fontsize,
        y_tick_fontsize,
        y_tick_rotation,
        y_major_locator,
        y_max_tick_to_value,
        y_format,
        ylim,
    )

    # 标注r值或rho值
    method = str(stats_method).strip().lower()
    if method == "spearman":
        s, p = stats.spearmanr(A, B)
        label = r"$\rho$"
    elif method == "pearson":
        s, p = stats.pearsonr(A, B)
        label = "r"
    else:
        raise ValueError(
            f"不支持的 stats_method: {stats_method!r}。请使用 'spearman' 或 'pearson'。"
        )

    if show_p_value:
        asterisk = f" p={p:.3f}"
    else:
        asterisk = (
            " ***" if p < 0.001 else " **" if p < 0.01 else " *" if p < 0.05 else ""
        )
    x_start, x_end = ax.get_xlim()
    y_start, y_end = ax.get_ylim()
    ax.text(
        x_start + (x_end - x_start) * 0.1,
        y_start + (y_end - y_start) * 0.9,
        f"{label}={s:.3f}{asterisk}",
        va="center",
        fontsize=asterisk_fontsize,
    )
    if hexbin:
        return hb
    return ax
