import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, ScalarFormatter
from scipy import stats

from typing import Any
import numpy.typing as npt
from matplotlib.axes import Axes

# 类型别名
Num = int | float  # 可同时接受int和float的类型
NumArray = list[Num] | npt.NDArray[np.float64]  # 数字数组类型


def compute_summary(data: NumArray) -> tuple[float, float, float]:
    """计算均值、标准差、标准误"""
    mean = np.mean(data)
    sd = np.std(data, ddof=1)
    se = sd / np.sqrt(len(data))
    return mean, sd, se


def add_scatter(
    ax: Axes,
    x_pos: Num,
    data: NumArray,
    color: str,
    dots_size: Num = 35,
) -> None:
    """添加散点"""
    ax.scatter(
        x_pos,
        data,
        c=color,
        s=dots_size,
        edgecolors="white",
        linewidths=1,
        alpha=0.5,
    )


def set_yaxis(
    ax: Axes,
    data: NumArray,
    options: dict[str, Any] | None,
) -> None:
    """设置Y轴格式"""
    if options.get("y_lim_range"):
        ax.set_ylim(*options["y_lim_range"])
    else:
        y_min, y_max = np.min(data), np.max(data)
        y_range = y_max - y_min
        golden_ratio = 5**0.5 - 1
        ax_min = (
            0
            if options.get("ax_min_is_0")
            else y_min - (y_range / golden_ratio - y_range / 2)
        )
        ax_max = y_max + (y_range / golden_ratio - y_range / 2)
        ax.set_ylim(ax_min, ax_max)

    if options.get("y_max_tick_to_one"):
        ticks = [
            tick
            for tick in ax.get_yticks()
            if tick <= options.get("y_max_tick_to_value", 1)
        ]
        ax.set_yticks(ticks)

    if options.get("math_text", True) and (np.min(data) < 0.1 or np.max(data) > 100):
        formatter = ScalarFormatter(useMathText=True)
        formatter.set_powerlimits((-2, 2))
        ax.yaxis.set_major_formatter(formatter)

    if options.get("one_decimal_place"):
        if options.get("math_text", True):
            print("“one_decimal_place”会与“math_text”冲突，请关闭“math_text”后再开启！")
        else:
            ax.yaxis.set_major_formatter(plt.FormatStrFormatter("%.1f"))

    if options.get("percentage"):
        if options.get("math_text", True):
            print("“percentage”会与“math_text”冲突，请关闭“math_text”后再开启！")
        else:
            ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x:.0%}"))


def perform_stat_test(
    data1: NumArray,
    data2: NumArray,
    method: str,
) -> tuple[float, float]:
    """执行统计检验"""
    if method == "ttest_ind":
        stat, p = stats.ttest_ind(data1, data2)
    elif method == "ttest_rel":
        stat, p = stats.ttest_rel(data1, data2)
    elif method == "mannwhitneyu":
        stat, p = stats.mannwhitneyu(data1, data2, alternative="two-sided")
    else:
        raise ValueError(f"未知统计方法: {method}")
    return stat, p


def annotate_significance(
    ax: Axes,
    comparisons: list[tuple[int, int, float]],
    y_base: Num,
    interval: Num,
    line_color: str,
    star_offset: Num,
    fontsize: Num,
    color: str,
) -> None:
    """添加显著性星号和连线"""
    for (i, j, pval), count in zip(comparisons, range(1, len(comparisons) + 1)):
        y = y_base + count * interval
        ax.annotate(
            "",
            xy=(i + 0.05, y),
            xytext=(j - 0.05, y),
            arrowprops=dict(
                edgecolor=line_color, width=0.5, headwidth=0.1, headlength=0.1
            ),
        )
        stars = "*" if pval > 0.01 else "**" if pval > 0.001 else "***"
        ax.text(
            (i + j) / 2,
            y + star_offset,
            stars,
            ha="center",
            va="center",
            color=color,
            fontsize=fontsize,
        )


def plot_one_group_bar_figure(
    data: list[NumArray],
    ax: Axes | None = None,
    labels_name: list[str] | None = None,
    width: Num = 0.5,
    colors: list[str] | None = None,
    dots_size: Num = 35,
    title_name: str = "",
    x_label_name: str = "",
    y_label_name: str = "",
    statistic: bool = False,
    test_method: str = "ttest_ind",
    p_list: list[float] | None = None,
    errorbar_type: str = "se",
    **kwargs: Any,
) -> None:
    """绘制单组柱状图

    Args:
        data: 数据列表，每个元素是一个数据组
        ax: matplotlib轴对象(可选)
        labels_name: x轴标签列表(可选)
        width: 柱状图宽度(默认0.5)
        colors: 颜色列表(可选)
        dots_size: 点图大小(默认35)
        title_name: 图表标题(默认"")
        x_label_name: x轴标签(默认"")
        y_label_name: y轴标签(默认"")
        statistic: 是否进行统计检验(默认False)
        test_method: 统计方法('ttest_ind','ttest_rel','mannwhitneyu'或'external')(默认'ttest_ind')
        p_list: 外部提供的p值列表(当test_method='external'时使用)
        errorbar_type: 误差线类型('se'或'sd')(默认'se')
        **kwargs: 其他可选参数:
            - title_fontsize: 标题字体大小
            - title_pad: 标题与图的间距
            - x_label_fontsize: x轴标签字体大小
            - y_label_fontsize: y轴标签字体大小
            - x_label_ha: x轴标签水平对齐方式
            - x_tick_fontsize: x轴刻度标签字体大小
            - x_tick_rotation: x轴刻度标签旋转角度
            - y_tick_fontsize: y轴刻度标签字体大小
            - y_tick_rotation: y轴刻度标签旋转角度
            - line_color: 显著性连线颜色
            - asterisk_fontsize: 星号字体大小
            - asterisk_color: 星号颜色
            - 以及其他y轴设置选项(参见set_yaxis函数)
    """
    if ax is None:
        ax = plt.gca()
    if labels_name is None:
        labels_name = [str(i) for i in range(len(data))]
    if colors is None:
        colors = ["gray"] * len(data)

    np.random.seed(1998)

    means, sds, ses = [], [], []
    x_positions = np.arange(len(labels_name))
    scatter_positions = []

    for i, d in enumerate(data):
        mean, sd, se = compute_summary(d)
        means.append(mean)
        sds.append(sd)
        ses.append(se)
        scatter_x = np.random.normal(i, 0.1, len(d))
        scatter_positions.append(scatter_x)

    if errorbar_type == "sd":
        error_values = sds
    elif errorbar_type == "se":
        error_values = ses

    # 绘制柱子
    ax.bar(x_positions, means, width=width, color=colors, alpha=1, edgecolor="k")
    ax.errorbar(
        x_positions,
        means,
        error_values,
        fmt="none",
        linewidth=1,
        capsize=3,
        color="black",
    )

    # 绘制散点
    for i, d in enumerate(data):
        add_scatter(ax, scatter_positions[i], d, colors[i], dots_size)

    # 美化
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(
        title_name,
        fontsize=kwargs.get("title_fontsize", 10),
        pad=kwargs.get("title_pad", 20),
    )
    ax.set_xlabel(x_label_name, fontsize=kwargs.get("x_label_fontsize", 10))
    ax.set_ylabel(y_label_name, fontsize=kwargs.get("y_label_fontsize", 10))
    ax.set_xticks(x_positions)
    ax.set_xticklabels(
        labels_name,
        ha=kwargs.get("x_label_ha", "center"),
        rotation_mode="anchor",
        fontsize=kwargs.get("x_tick_fontsize", 10),
        rotation=kwargs.get("x_tick_rotation", 0),
    )
    ax.tick_params(
        axis="y",
        labelsize=kwargs.get("y_tick_fontsize", 10),
        rotation=kwargs.get("y_tick_rotation", 0),
    )

    all_values = np.concatenate(data)
    set_yaxis(ax, all_values, kwargs)

    # 添加统计显著性标记
    if statistic:
        comparisons = []
        idx = 0
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if test_method == "external":
                    p = p_list[idx]
                    idx += 1
                else:
                    _, p = perform_stat_test(data[i], data[j], test_method)
                if p <= 0.05:
                    comparisons.append((i, j, p))

        y_max = ax.get_ylim()[1]
        interval = (y_max - np.max(all_values)) / (len(comparisons) + 1)
        annotate_significance(
            ax,
            comparisons,
            np.max(all_values),
            interval,
            line_color=kwargs.get("line_color", "0.5"),
            star_offset=interval / 5,
            fontsize=kwargs.get("asterisk_fontsize", 10),
            color=kwargs.get("asterisk_color", "k"),
        )


def plot_one_group_violin_figure(
    data: list[NumArray],
    ax: Axes | None = None,
    labels_name: list[str] | None = None,
    width: Num = 0.8,
    colors: list[str] | None = None,
    show_dots: bool = False,
    dots_size: Num = 35,
    title_name: str = "",
    x_label_name: str = "",
    y_label_name: str = "",
    statistic: bool = False,
    test_method: str = "ttest_ind",
    p_list: list[float] | None = None,
    show_means: bool = False,
    show_extrema: bool = True,
    **kwargs: Any,
) -> None:
    """绘制单组小提琴图

    Args:
        data: 数据列表，每个元素是一个数据组
        ax: matplotlib轴对象(可选)
        labels_name: x轴标签列表(可选)
        width: 柱状图宽度(默认0.5)
        colors: 颜色列表(可选)
        dots_size: 点图大小(默认35)
        title_name: 图表标题(默认"")
        x_label_name: x轴标签(默认"")
        y_label_name: y轴标签(默认"")
        statistic: 是否进行统计检验(默认False)
        test_method: 统计方法('ttest_ind','ttest_rel','mannwhitneyu'或'external')(默认'ttest_ind')
        p_list: 外部提供的p值列表(当test_method='external'时使用)
        errorbar_type: 误差线类型('se'或'sd')(默认'se')
        **kwargs: 其他可选参数:
            - title_fontsize: 标题字体大小
            - title_pad: 标题与图的间距
            - x_label_fontsize: x轴标签字体大小
            - y_label_fontsize: y轴标签字体大小
            - x_label_ha: x轴标签水平对齐方式
            - x_tick_fontsize: x轴刻度标签字体大小
            - x_tick_rotation: x轴刻度标签旋转角度
            - y_tick_fontsize: y轴刻度标签字体大小
            - y_tick_rotation: y轴刻度标签旋转角度
            - line_color: 显著性连线颜色
            - asterisk_fontsize: 星号字体大小
            - asterisk_color: 星号颜色
            - 以及其他y轴设置选项(参见set_yaxis函数)
    """
    ax = ax or plt.gca()
    labels_name = labels_name or [str(i) for i in range(len(data))]
    colors = colors or ["gray"] * len(data)

    np.random.seed(1998)  # 固定随机种子保证散点位置可复现

    # 绘制小提琴图
    parts = ax.violinplot(
        dataset=list(data),
        positions=np.arange(len(data)),
        widths=width,
        showmeans=show_means,
        showextrema=show_extrema,
    )

    # 设置小提琴颜色（修改默认样式）
    for pc, color in zip(parts["bodies"], colors):
        pc.set_facecolor(color)
        pc.set_edgecolor("black")
        pc.set_alpha(0.7)

    # 修改内部线条颜色
    if show_extrema:
        parts["cmins"].set_color("black")  # 最小值线
        parts["cmaxes"].set_color("black")  # 最大值线
        parts["cbars"].set_color("black")  # 中线（median）
    if show_means:
        parts["cmeans"].set_color("black")  # 均值线

    # 绘制散点（复用现有函数）
    if show_dots:
        scatter_positions = [
            np.random.normal(i, 0.1, len(d)) for i, d in enumerate(data)
        ]
        for i, d in enumerate(data):
            add_scatter(ax, scatter_positions[i], d, colors[i], dots_size)

    # 美化坐标轴（复用现有函数）
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(title_name, fontsize=kwargs.get("title_fontsize", 10), pad=20)
    ax.set_xlabel(x_label_name, fontsize=kwargs.get("x_label_fontsize", 10))
    ax.set_ylabel(y_label_name, fontsize=kwargs.get("y_label_fontsize", 10))
    ax.set_xticks(np.arange(len(data)))
    ax.set_xticklabels(
        labels_name,
        fontsize=kwargs.get("x_tick_fontsize", 10),
        rotation=kwargs.get("x_tick_rotation", 0),
    )

    # 设置Y轴（复用现有函数）
    all_values = np.concatenate(data)
    set_yaxis(ax, all_values, kwargs)

    # 添加统计标记（复用现有函数）
    if statistic:
        comparisons = []
        idx = 0
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if test_method == "external":
                    p = p_list[idx] if p_list else 1.0
                    idx += 1
                else:
                    _, p = perform_stat_test(data[i], data[j], test_method)
                if p <= 0.05:
                    comparisons.append((i, j, p))

        if comparisons:
            y_max = ax.get_ylim()[1]
            interval = (y_max - np.max(all_values)) / (len(comparisons) + 1)
            annotate_significance(
                ax,
                comparisons,
                np.max(all_values),
                interval,
                line_color=kwargs.get("line_color", "0.5"),
                star_offset=interval / 5,
                fontsize=kwargs.get("asterisk_fontsize", 10),
                color=kwargs.get("asterisk_color", "k"),
            )


def main():
    """测试绘图函数的功能"""
    from pathlib import Path

    # 测试数据
    np.random.seed(42)
    data = np.array(
        [
            0.00001 * np.random.normal(0, 1, 100),
            0.00001 * np.random.normal(0, 1, 100),
            0.00001 * np.random.normal(0, 1, 100),
        ]
    )
    # 测试函数
    fig, ax = plt.subplots(1, 1, figsize=(3, 3))
    plot_one_group_violin_figure(
        data,
        ax=ax,
        labels_name=["AAA", "BBB", "CCC"],
        width=0.3,
        colors=["red", "blue", "green"],
        show_dots=True,
        dots_size=10,
        title_name="this is a title_name",
        x_label_name="x_label_name",
        y_label_name="y_label_name",
        statistic=True,
        test_method="external",
        p_list=[1, 0.01, 0.001],
        errorbar_type="sd",
        title_fontsize=7,
        title_pad=2,
        x_label_fontsize=7,
        y_label_fontsize=7,
        x_label_ha="right",
        x_tick_fontsize=7,
        x_tick_rotation=30,
        y_tick_fontsize=7,
        y_tick_rotation=30,
        line_color="red",
        asterisk_fontsize=7,
        asterisk_color="red",
    )
    # 测试输出
    save_dir = Path(__file__).parent / "tests_output"
    save_dir.mkdir(exist_ok=True)  # 自动创建这个目录（如果没有）
    save_path = save_dir / "test.png"
    fig.savefig(save_path, dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
