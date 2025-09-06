import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (
    ScalarFormatter,
    FuncFormatter,
    MultipleLocator,
    FormatStrFormatter,
)
from matplotlib.colors import LinearSegmentedColormap
from scipy import stats

from typing import TypeAlias

# 类型别名定义
Num: TypeAlias = float | int  # 可同时接受int和float的类型

__all__ = ["plot_correlation_figure"]


def plot_correlation_figure(
    data1: list[Num] | np.ndarray,
    data2: list[Num] | np.ndarray,
    ax: plt.Axes | None = None,
    stats_method: str = "spearman",
    ci: bool = False,
    dots_color: str = "steelblue",
    dots_size: int | float = 1,
    line_color: str = "r",
    title_name: str = "",
    title_fontsize: int = 12,
    title_pad: int = 10,
    x_label_name: str = "",
    x_label_fontsize: int = 10,
    x_tick_fontsize: int = 10,
    x_tick_rotation: int = 0,
    x_major_locator: float | None = None,
    x_max_tick_to_value: float | None = None,
    x_format: str = "normal",  # 支持 "normal", "sci", "1f", "percent"
    y_label_name: str = "",
    y_label_fontsize: int = 10,
    y_tick_fontsize: int = 10,
    y_tick_rotation: int = 0,
    y_major_locator: float | None = None,
    y_max_tick_to_value: float | None = None,
    y_format: str = "normal",  # 支持 "normal", "sci", "1f", "percent"
    asterisk_fontsize: int = 10,
    show_p_value: bool = False,
    hexbin: bool = False,
    hexbin_cmap: bool = None,
    hexbin_gridsize: int = 50,
) -> None:
    """
    绘制两个数据集之间的相关性图，支持线性回归、置信区间和统计方法（Spearman 或 Pearson）。

    Args:
        data1 (list[Num] | np.ndarray): 第一个数据集，可以是整数或浮点数列表或数组。
        data2 (list[Num] | np.ndarray): 第二个数据集，可以是整数或浮点数列表或数组。
        ax (plt.Axes | None, optional): matplotlib 的 Axes 对象，用于绘图。默认为 None，使用当前 Axes。
        stats_method (str, optional): 相关性统计方法，支持 "spearman" 和 "pearson"。默认为 "spearman"。
        ci (bool, optional): 是否绘制置信区间带。默认为 False。
        dots_color (str, optional): 散点的颜色。默认为 "steelblue"。
        dots_size (int | float, optional): 散点的大小。默认为 1。
        line_color (str, optional): 回归线的颜色。默认为 "r"（红色）。
        title_name (str, optional): 图形标题。默认为空字符串。
        title_fontsize (int, optional): 标题字体大小。默认为 10。
        title_pad (int, optional): 标题与图形之间的间距。默认为 10。
        x_label_name (str, optional): X 轴标签名称。默认为空字符串。
        x_label_fontsize (int, optional): X 轴标签字体大小。默认为 10。
        x_tick_fontsize (int, optional): X 轴刻度标签字体大小。默认为 10。
        x_tick_rotation (int, optional): X 轴刻度标签旋转角度。默认为 0。
        x_major_locator (float | None, optional): 设置 X 轴主刻度间隔。默认为 None。
        x_max_tick_to_value (float | None, optional): 设置 X 轴最大显示刻度值。默认为 None。
        x_format (str, optional): X 轴格式化方式，支持 "normal", "sci", "1f", "percent"。默认为 "normal"。
        y_label_name (str, optional): Y 轴标签名称。默认为空字符串。
        y_label_fontsize (int, optional): Y 轴标签字体大小。默认为 10。
        y_tick_fontsize (int, optional): Y 轴刻度标签字体大小。默认为 10。
        y_tick_rotation (int, optional): Y 轴刻度标签旋转角度。默认为 0。
        y_major_locator (float | None, optional): 设置 Y 轴主刻度间隔。默认为 None。
        y_max_tick_to_value (float | None, optional): 设置 Y 轴最大显示刻度值。默认为 None。
        y_format (str, optional): Y 轴格式化方式，支持 "normal", "sci", "1f", "percent"。默认为 "normal"。
        asterisk_fontsize (int, optional): 显著性星号字体大小。默认为 10。
        show_p_value (bool, optional): 是否显示 p 值。默认为 True。

    Returns:
        None
    """

    def set_axis(
        ax, axis, label, labelsize, ticksize, rotation, locator, max_tick_value, fmt
    ):
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
        ax.scatter(A, B, c=dots_color, s=dots_size, alpha=0.8)
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
            color="salmon",
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
    )

    # 标注r值或rho值
    if stats_method == "spearman":
        s, p = stats.spearmanr(A, B)
        label = r"$\rho$"
    elif stats_method == "pearson":
        s, p = stats.pearsonr(A, B)
        label = "r"
    else:
        print(f"没有统计方法 {stats_method}，请检查拼写。更换为默认的 spearman 方法。")
        s, p = stats.spearmanr(A, B)
        label = r"$\rho$"

    if show_p_value:
        asterisk = f" p={p:.4f}"
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
