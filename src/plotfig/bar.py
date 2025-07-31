import warnings
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from matplotlib.axes import Axes
from matplotlib.ticker import FuncFormatter, ScalarFormatter
from matplotlib.colors import LinearSegmentedColormap, to_rgba
from matplotlib.patches import Polygon
from scipy import stats

# 设置警告过滤器，显示所有警告
warnings.simplefilter("always")

# 类型别名
Num = int | float  # 可同时接受int和float的类型
NumArray = list[Num] | npt.NDArray[np.float64]  # 数字数组类型

__all__ = [
    "plot_one_group_bar_figure",
    "plot_one_group_violin_figure",
    "plot_one_group_violin_figure_old",
    "plot_multi_group_bar_figure",
]

# 创建随机数生成器
RNG = np.random.default_rng(seed=1998)


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
    if options.get("y_lim"):
        ax.set_ylim(*options["y_lim"])
    else:
        y_min, y_max = np.min(data), np.max(data)
        y_range = y_max - y_min
        golden_ratio = 5**0.5 - 1
        ax_min = (
            0
            if options.get("ax_bottom_is_0")
            else y_min - (y_range / golden_ratio - y_range / 2)
        )
        ax_max = y_max + (y_range / golden_ratio - y_range / 2)
        ax.set_ylim(ax_min, ax_max)

    if options.get("y_max_tick_is_1"):
        ticks = [
            tick
            for tick in ax.get_yticks()
            if tick <= options.get("y_max_tick_is_1", 1)
        ]
        ax.set_yticks(ticks)

    if options.get("math_text", True) and (np.min(data) < 0.1 or np.max(data) > 100):
        formatter = ScalarFormatter(useMathText=True)
        formatter.set_powerlimits((-2, 2))
        ax.yaxis.set_major_formatter(formatter)

    if options.get("one_decimal_place"):
        if options.get("math_text", True):
            warnings.warn(
                "“one_decimal_place”会与“math_text”冲突，请关闭“math_text”后再开启！",
                UserWarning,
                stacklevel=2,
            )
        else:
            ax.yaxis.set_major_formatter(plt.FormatStrFormatter("%.1f"))

    if options.get("percentage"):
        if options.get("math_text", True):
            warnings.warn(
                "“percentage”会与“math_text”冲突，请关闭“math_text”后再开启！",
                UserWarning,
                stacklevel=2,
            )
        else:
            ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x:.0%}"))


# 统计相关
def perform_stat_test(
    data1: NumArray | None = None,
    data2: NumArray | None = None,
    popmean: NumArray | None = None,
    method: str = "ttest_ind",
) -> tuple[float, float]:
    """执行统计检验"""
    # 使用字典映射替代多个elif分支，提高可读性和可扩展性
    test_methods = {
        "ttest_ind": lambda: stats.ttest_ind(data1, data2),
        "ttest_rel": lambda: stats.ttest_rel(data1, data2),
        "ttest_1samp": lambda: stats.ttest_1samp(data1, popmean),
        "mannwhitneyu": lambda: stats.mannwhitneyu(
            data1, data2, alternative="two-sided"
        ),
    }

    if method in test_methods:
        stat, p = test_methods[method]()
    else:
        raise ValueError(f"未知统计方法: {method}")
    return stat, p


def determine_test_modle(data, method, p_list=None, popmean=0):
    comparisons = []
    idx = 0
    if method != "ttest_1samp":
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if method == "external":
                    p = p_list[idx]
                    idx += 1
                else:
                    _, p = perform_stat_test(
                        data1=data[i], data2=data[j], method=method
                    )
                if p <= 0.05:
                    comparisons.append((i, j, p))
    else:
        for i in range(len(data)):
            _, p = perform_stat_test(data1=data[i], popmean=popmean, method=method)
            if p <= 0.05:
                comparisons.append((i, p))
    return comparisons


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

    def _stars(pval, i, y, color, fontsize):
        stars = "*" if pval > 0.01 else "**" if pval > 0.001 else "***"
        ax.text(
            i,
            y,
            stars,
            ha="center",
            va="center",
            color=color,
            fontsize=fontsize,
        )

    if len(comparisons[0]) == 3:
        for (i, j, pval), count in zip(comparisons, range(1, len(comparisons) + 1)):
            y = y_base + count * interval
            ax.annotate(
                "",
                xy=(i, y),
                xytext=(j, y),
                arrowprops=dict(
                    edgecolor=line_color, width=0.5, headwidth=0.1, headlength=0.1
                ),
            )
            _stars(pval, (i + j) / 2, y + star_offset, color, fontsize)
    elif len(comparisons[0]) == 2:
        for i, pval in comparisons:
            y = y_base
            _stars(pval, i, y + star_offset, color, fontsize)


def statistics(
    data,
    test_method,
    p_list,
    popmean,
    ax,
    all_values,
    statistical_line_color,
    asterisk_fontsize,
    asterisk_color,
):
    if isinstance(test_method, list):
        if len(test_method) > 2 or (
            len(test_method) == 2 and "ttest_1samp" not in test_method
        ):
            raise ValueError(
                "test_method 最多只能有2个元素。且当元素数量为2时，其中之一必须是 'ttest_1samp'。"
            )

        for method in test_method:
            comparisons = determine_test_modle(data, method, p_list, popmean)
            if not comparisons:
                return

            y_max = ax.get_ylim()[1]
            interval = (y_max - np.max(all_values)) / (len(comparisons) + 1)

            color = (
                "b"
                if len(test_method) > 1 and method == "ttest_1samp"
                else asterisk_color
            )

            annotate_significance(
                ax,
                comparisons,
                np.max(all_values),
                interval,
                line_color=statistical_line_color,
                star_offset=interval / 5,
                fontsize=asterisk_fontsize,
                color=color,
            )
    else:
        warnings.warn(
            "请使用列表形式传递 test_method 参数，例如 test_method=['ttest_ind']。字符串形式 test_method='ttest_ind' 将在后续版本中弃用。",
            DeprecationWarning,
            stacklevel=1,
        )
        comparisons = determine_test_modle(data, test_method, p_list, popmean)
        if not comparisons:
            return

        y_max = ax.get_ylim()[1]
        interval = (y_max - np.max(all_values)) / (len(comparisons) + 1)
        annotate_significance(
            ax,
            comparisons,
            np.max(all_values),
            interval,
            line_color=statistical_line_color,
            star_offset=interval / 5,
            fontsize=asterisk_fontsize,
            color=asterisk_color,
        )


# 可调用接口函数
def plot_one_group_bar_figure(
    data: list[NumArray],
    ax: Axes | None = None,
    labels_name: list[str] | None = None,
    width: Num = 0.5,
    colors: list[str] | None = None,
    color_alpha: Num = 1,
    edgecolor: str | None = None,
    gradient_color: bool = False,
    colors_start=None,
    colors_end=None,
    dots_size: Num = 35,
    dots_color: list[list[str]] | None = None,
    title_name: str = "",
    x_label_name: str = "",
    y_label_name: str = "",
    errorbar_type: str = "sd",
    statistic: bool = False,
    test_method: str = "ttest_ind",
    popmean: Num = 0,
    p_list: list[float] | None = None,
    statistical_line_color: str = "0.5",
    asterisk_fontsize: Num = 10,
    asterisk_color: str = "k",
    **kwargs: Any,
) -> None:
    """绘制单组柱状图，包含散点、误差条和统计显著性标记。

    Args:
        data (list[NumArray]): 包含多个数据集的列表，每个数据集是一个数字数组。
        ax (Axes | None, optional): matplotlib 的 Axes 对象，用于绘图。默认为 None，使用当前 Axes。
        labels_name (list[str] | None, optional): 每个数据集对应的标签。默认为 None，使用索引作为标签。
        width (Num, optional): 柱子的宽度。默认为 0.5。
        colors (list[str] | None, optional): 每个柱子的颜色列表。若为 None，使用默认灰色。
        color_alpha (Num, optional): 颜色透明度，取值范围为 0（完全透明）到 1（完全不透明）。使用 gradient_color 时该参数无效。默认为 1。
        edgecolor (str | None, optional): 柱子的边缘颜色。默认为 None，即不特别设置。
        gradient_color (bool, optional): 是否为柱子启用渐变色填充。默认为 False。
        colors_start (list[str] | None, optional): 渐变色的起始颜色列表。用于 gradient_color=True。
        colors_end (list[str] | None, optional): 渐变色的结束颜色列表。用于 gradient_color=True。
        dots_size (Num, optional): 每个散点的大小。默认为 35。
        dots_color (list[list[str]] | None, optional): 每组数据中每个散点的颜色（二维列表）。默认为 None，使用灰色。
        title_name (str, optional): 图表的标题文字。默认为空字符串。
        x_label_name (str, optional): X 轴的标签。默认为空字符串。
        y_label_name (str, optional): Y 轴的标签。默认为空字符串。
        errorbar_type (str, optional): 误差条类型。支持 "sd"（标准差）或 "se"（标准误）。默认为 "sd"。
        statistic (bool, optional): 是否进行统计检验并在柱状图上标记显著性。默认为 False。
        test_method (str, optional): 统计检验方法。支持 "ttest_ind"、"ttest_rel"、"ttest_1samp"、"mannwhitneyu" 或 "external"。默认为 "ttest_ind"。
        popmean (Num): 总体均值假设值，用于单样本t检验(ttest_1samp)。默认为 0。
        p_list (list[float] | None, optional): 提供的 p 值列表，用于 "external" 检验。默认为None。
        statistical_line_color (str, optional): 统计显著性标记连线的颜色。默认为 "0.5"（灰色）。
        asterisk_fontsize (Num, optional): 显著性星号的字体大小。默认为 10。
        asterisk_color (str, optional): 显著性星号的颜色。默认为 "k"（黑色）。
        **kwargs (Any): 其他 matplotlib 参数，用于进一步定制图表样式。

    Returns:
        None
    """

    if ax is None:
        ax = plt.gca()
    if labels_name is None:
        labels_name = [str(i) for i in range(len(data))]
    if colors is None:
        colors = ["gray"] * len(data)

    means, sds, ses = [], [], []
    x_positions = np.arange(len(labels_name))
    scatter_positions = []

    for i, d in enumerate(data):
        mean, sd, se = compute_summary(d)
        means.append(mean)
        sds.append(sd)
        ses.append(se)
        scatter_x = RNG.normal(i, 0.1, len(d))
        scatter_positions.append(scatter_x)

    if errorbar_type == "sd":
        error_values = sds
    elif errorbar_type == "se":
        error_values = ses

    # 绘制柱子
    if gradient_color:
        if colors_start is None:  # 默认颜色
            colors_start = ["#e38a48"] * len(x_positions)  # 左边颜色
        if colors_end is None:  # 默认颜色
            colors_end = ["#4573a5"] * len(x_positions)  # 右边颜色
        for x, h, c1, c2 in zip(x_positions, means, colors_start, colors_end):
            # 生成线性渐变 colormap
            cmap = LinearSegmentedColormap.from_list("grad_cmap", [c1, "white", c2])
            gradient = np.linspace(0, 1, 100).reshape(1, -1)  # 横向渐变
            # 计算渐变矩形位置：跟bar完全对齐
            extent = [x - width / 2, x + width / 2, 0, h]
            # 叠加渐变矩形（imshow）
            ax.imshow(gradient, aspect="auto", cmap=cmap, extent=extent, zorder=0)
    else:
        ax.bar(
            x_positions,
            means,
            width=width,
            color=colors,
            alpha=color_alpha,
            edgecolor=edgecolor,
        )

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
        if dots_color is None:
            add_scatter(ax, scatter_positions[i], d, ["gray"] * len(d), dots_size)
        else:
            add_scatter(ax, scatter_positions[i], d, dots_color[i], dots_size)

    # 美化
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(
        title_name,
        fontsize=kwargs.get("title_fontsize", 10),
        pad=kwargs.get("title_pad", 10),
    )
    # x轴
    ax.set_xlim(min(x_positions) - 0.5, max(x_positions) + 0.5)
    ax.set_xlabel(x_label_name, fontsize=kwargs.get("x_label_fontsize", 10))
    ax.set_xticks(x_positions)
    ax.set_xticklabels(
        labels_name,
        ha=kwargs.get("x_label_ha", "center"),
        rotation_mode="anchor",
        fontsize=kwargs.get("x_tick_fontsize", 10),
        rotation=kwargs.get("x_tick_rotation", 0),
    )
    # y轴
    ax.tick_params(
        axis="y",
        labelsize=kwargs.get("y_tick_fontsize", 10),
        rotation=kwargs.get("y_tick_rotation", 0),
    )
    ax.set_ylabel(y_label_name, fontsize=kwargs.get("y_label_fontsize", 10))
    all_values = np.concatenate(data)
    set_yaxis(ax, all_values, kwargs)

    # 添加统计显著性标记
    if statistic:
        statistics(
            data,
            test_method,
            p_list,
            popmean,
            ax,
            all_values,
            statistical_line_color,
            asterisk_fontsize,
            asterisk_color,
        )


def plot_one_group_violin_figure(
    data: list[NumArray],
    ax: Axes | None = None,
    width: Num = 0.8,
    colors: list[str] | None = None,
    color_alpha: Num = 1,
    gradient_color: bool = False,
    colors_start: list[str] | None = None,
    colors_end: list[str] | None = None,
    labels_name: list[str] | None = None,
    x_label_name: str = "",
    y_label_name: str = "",
    title_name: str = "",
    title_pad: Num = 10,
    show_dots: bool = False,
    dots_size: Num = 35,
    statistic: bool = False,
    test_method: str = "ttest_ind",
    popmean: Num = 0,
    p_list: list[float] | None = None,
    statistical_line_color: str = "0.5",
    asterisk_fontsize: Num = 10,
    asterisk_color: str = "k",
    **kwargs: Any,
) -> None:
    """绘制单组小提琴图，可选散点叠加、渐变填色和统计显著性标注。

    Args:
        data (list[NumArray]): 包含多个数据集的列表，每个数据集是一个数值数组。
        ax (Axes | None, optional): matplotlib 的 Axes 对象，用于绘图。默认为 None，使用当前 Axes。
        width (Num, optional): 小提琴图的总宽度。默认为 0.8。
        colors (list[str] | None, optional): 每个小提琴的颜色。若为 None，使用默认灰色。
        color_alpha (Num, optional): 颜色透明度，取值范围为 0（完全透明）到 1（完全不透明）。使用 gradient_color 时该参数无效。默认为 1。
        gradient_color (bool, optional): 是否启用渐变色填充。默认为 False。
        colors_start (list[str] | None, optional): 渐变起始颜色列表，对应每组数据。
        colors_end (list[str] | None, optional): 渐变结束颜色列表，对应每组数据。
        labels_name (list[str] | None, optional): 每个数据集的标签名称。默认为 None，使用索引作为标签。
        x_label_name (str, optional): X 轴的标签。默认为空字符串。
        y_label_name (str, optional): Y 轴的标签。默认为空字符串。
        title_name (str, optional): 图表标题。默认为空字符串。
        title_pad (Num, optional): 标题与图之间的垂直距离。默认为 10。
        show_dots (bool, optional): 是否在小提琴图上叠加散点。默认为 False。
        dots_size (Num, optional): 散点大小。默认为 35。
        statistic (bool, optional): 是否进行统计检验并标注显著性。默认为 False。
        test_method (str, optional): 统计检验方法。支持 "ttest_ind"、"ttest_rel"、"mannwhitneyu" 或 "external"。默认为 "ttest_ind"。
        popmean (Num): 总体均值假设值，用于单样本t检验(ttest_1samp)。默认为 0。
        p_list (list[float] | None, optional): 外部提供的 p 值列表。默认为 None。
        statistical_line_color (str, optional): 统计显著性标记连线的颜色。默认为 "0.5"（灰色）。
        asterisk_fontsize (Num, optional): 显著性星号的字体大小。默认为 10。
        asterisk_color (str, optional): 显著性星号的颜色。默认为 "k"（黑色）。
        **kwargs (Any): 其他 matplotlib 参数，用于进一步定制图表样式。

    Returns:
        None
    """

    ax = ax or plt.gca()
    labels_name = labels_name or [str(i) for i in range(len(data))]
    colors = colors or ["gray"] * len(data)

    def _draw_gradient_violin(
        ax, data, pos, width=width, c1="red", c2="blue", color_alpha=1
    ):
        # KDE估计
        kde = stats.gaussian_kde(data)
        buffer = (max(data) - min(data)) / 5
        y = np.linspace(min(data) - buffer, max(data) + buffer, 300)
        ymax = max(data) + buffer
        ymin = min(data) - buffer
        density = kde(y)
        density = density / density.max() * (width / 2)  # 控制violin宽度
        # violin左右边界
        x_left = pos - density
        x_right = pos + density
        # 组合封闭边界
        verts = np.concatenate(
            [np.stack([x_left, y], axis=1), np.stack([x_right[::-1], y[::-1]], axis=1)]
        )
        # 构建渐变图像
        grad_width = 200
        grad_height = 300
        gradient = np.linspace(0, 1, grad_width)
        if c1 == c2:
            rgba = to_rgba(c1, alpha=color_alpha)
            cmap = LinearSegmentedColormap.from_list("cmap", [rgba, rgba])
            gradient_rgb = plt.get_cmap(cmap)(gradient)
        else:
            cmap = LinearSegmentedColormap.from_list("cmap", [c1, "white", c2])
            gradient_rgb = plt.get_cmap(cmap)(gradient)[..., :3]
        gradient_img = np.tile(gradient_rgb, (grad_height, 1, 1))
        # 显示图像并裁剪成violin形状
        im = ax.imshow(
            gradient_img,
            extent=[pos - width / 2, pos + width / 2, y.min(), y.max()],
            origin="lower",
            aspect="auto",
            zorder=1,
        )
        # 添加边界线并作为clip
        poly = Polygon(
            verts,
            closed=True,
            facecolor="none",
            edgecolor="black",
            linewidth=1.2,
            zorder=2,
        )
        ax.add_patch(poly)
        im.set_clip_path(poly)
        # 添加 box 元素
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        median = np.median(data)
        # 添加 IQR box（黑色矩形）
        ax.add_patch(
            plt.Rectangle(
                (pos - width / 16, q1),  # 左下角坐标
                width / 8,  # 宽度
                q3 - q1,  # 高度
                facecolor="black",
                alpha=0.7,
            )
        )
        # 添加白色中位数点
        ax.plot(pos, median, "o", color="white", markersize=5, zorder=3)
        return ymax, ymin

    ymax_lst, ymin_lst = [], []
    for i, d in enumerate(data):
        if gradient_color:
            c1 = colors_start[i]
            c2 = colors_end[i]
        else:
            c1 = c2 = colors[i]
        ymax, ymin = _draw_gradient_violin(
            ax, d, pos=i, c1=c1, c2=c2, color_alpha=color_alpha
        )
        ymax_lst.append(ymax)
        ymin_lst.append(ymin)
    ymax = max(ymax_lst)
    ymin = min(ymin_lst)

    # 绘制散点（复用现有函数）
    if show_dots:
        scatter_positions = [RNG.normal(i, 0.1, len(d)) for i, d in enumerate(data)]
        for i, d in enumerate(data):
            add_scatter(ax, scatter_positions[i], d, colors[i], dots_size)

    # 美化
    ax.set_title(title_name, fontsize=kwargs.get("title_fontsize", 10), pad=title_pad)
    ax.spines[["top", "right"]].set_visible(False)
    # x轴
    ax.set_xlim(-0.5, len(data) - 0.5)
    ax.set_xlabel(x_label_name, fontsize=kwargs.get("x_label_fontsize", 10))
    ax.set_xticks(np.arange(len(data)))
    ax.set_xticklabels(
        labels_name,
        fontsize=kwargs.get("x_tick_fontsize", 10),
        rotation=kwargs.get("x_tick_rotation", 0),
    )
    # y轴
    ax.tick_params(
        axis="y",
        labelsize=kwargs.get("y_tick_fontsize", 10),
        rotation=kwargs.get("y_tick_rotation", 0),
    )
    ax.set_ylabel(y_label_name, fontsize=kwargs.get("y_label_fontsize", 10))
    all_values = [ymin, ymax]
    set_yaxis(ax, all_values, kwargs)

    # 添加统计标记（复用现有函数）
    if statistic:
        statistics(
            data,
            test_method,
            p_list,
            popmean,
            ax,
            all_values,
            statistical_line_color,
            asterisk_fontsize,
            asterisk_color,
        )

    return


def plot_one_group_violin_figure_old(
    data: list[NumArray],
    ax: Axes | None = None,
    width: Num = 0.8,
    show_extrema: bool = True,
    colors: list[str] | None = None,
    labels_name: list[str] | None = None,
    x_label_name: str = "",
    y_label_name: str = "",
    title_name: str = "",
    title_pad: Num = 10,
    show_dots: bool = False,
    dots_size: Num = 35,
    statistic: bool = False,
    test_method: str = "ttest_ind",
    p_list: list[float] | None = None,
    **kwargs: Any,
) -> None:
    warnings.warn(
        "plot_one_group_violin_figure_old 即将弃用，请使用 plot_one_group_violin_figure 替代。未来版本将移除本函数。",
        DeprecationWarning,
        stacklevel=2,
    )
    """绘制单组小提琴图，包含散点和统计显著性标记。

    Args:
        data (list[NumArray]): 包含多个数据集的列表，每个数据集是一个数字数组。
        ax (Axes | None, optional): matplotlib 的 Axes 对象，用于绘图。默认为 None，使用当前的 Axes。
        width (Num, optional): 小提琴图的宽度。默认为 0.8。
        show_extrema (bool, optional): 是否显示极值线。默认为 True。
        colors (list[str] | None, optional): 每个小提琴图的颜色。默认为 None，使用灰色。
        labels_name (list[str] | None, optional): 每个数据集的标签名称。默认为 None，使用索引作为标签。
        x_label_name (str, optional): X 轴的标签。默认为空字符串。
        y_label_name (str, optional): Y 轴的标签。默认为空字符串。
        title_name (str, optional): 图表的标题。默认为空字符串。
        title_pad (Num, optional): 标题与图之间的垂直距离。默认为 10。
        show_dots (bool, optional): 是否显示散点。默认为 False。
        dots_size (Num, optional): 散点的大小。默认为 35。
        statistic (bool, optional): 是否进行统计检验并标注显著性标记。默认为 False。
        test_method (str, optional): 统计检验的方法，支持 "ttest_ind"、"ttest_rel" 和 "mannwhitneyu"。默认为 "ttest_ind"。
        p_list (list[float] | None, optional): 外部提供的 p 值列表，用于统计检验。默认为 None。
        **kwargs (Any): 其他可选参数，用于进一步定制图表样式。

    Returns:
        None
    """

    ax = ax or plt.gca()
    labels_name = labels_name or [str(i) for i in range(len(data))]
    colors = colors or ["gray"] * len(data)

    # 绘制小提琴图
    parts = ax.violinplot(
        dataset=list(data),
        positions=np.arange(len(data)),
        widths=width,
        showextrema=show_extrema,
    )
    # 添加 box 元素
    for i, d in enumerate(data):
        # 计算统计量
        q1 = np.percentile(d, 25)
        q3 = np.percentile(d, 75)
        median = np.median(d)
        # 添加 IQR box（黑色矩形）
        ax.add_patch(
            plt.Rectangle(
                (i - width / 16, q1),  # 左下角坐标
                width / 8,  # 宽度
                q3 - q1,  # 高度
                facecolor="black",
                alpha=0.7,
            )
        )
        # 添加白色中位数点
        ax.plot(i, median, "o", color="white", markersize=3, zorder=3)

    # 设置小提琴颜色（修改默认样式）
    for pc, color in zip(parts["bodies"], colors):
        pc.set_facecolor(color)
        pc.set_edgecolor("black")
        pc.set_alpha(1)

    # 修改内部线条颜色
    if show_extrema:
        parts["cmins"].set_color("black")  # 最小值线
        parts["cmaxes"].set_color("black")  # 最大值线
        parts["cbars"].set_color("black")  # 中线（median）

    # 绘制散点（复用现有函数）
    if show_dots:
        scatter_positions = [RNG.normal(i, 0.1, len(d)) for i, d in enumerate(data)]
        for i, d in enumerate(data):
            add_scatter(ax, scatter_positions[i], d, colors[i], dots_size)

    # 美化坐标轴（复用现有函数）
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(title_name, fontsize=kwargs.get("title_fontsize", 10), pad=title_pad)
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


def plot_multi_group_bar_figure(
    data: list[list[NumArray]],
    ax: plt.Axes | None = None,
    group_labels: list[str] | None = None,
    bar_labels: list[str] | None = None,
    bar_width: Num = 0.2,
    bar_gap: Num = 0.1,
    bar_color: list[str] | None = None,
    errorbar_type: str = "sd",
    dots_color: str = "gray",
    dots_size: int = 35,
    title_name: str = "",
    x_label_name: str = "",
    y_label_name: str = "",
    statistic: bool = False,
    test_method: str = "external",
    p_list: list[list[Num]] | None = None,
    legend: bool = True,
    legend_position: tuple[Num, Num] = (1.2, 1),
    **kwargs: Any,
) -> None:
    """
    绘制多组柱状图，包含散点、误差条、显著性标注和图例等。

    Args:
        data (list[list[NumArray]]): 多组数据，每组是一个包含若干数值数组的列表。
        ax (plt.Axes | None, optional): matplotlib 的 Axes 对象。默认为 None，自动使用当前的 Axes。
        group_labels (list[str] | None, optional): 每组的标签名。默认为 None，使用 "Group i"。
        bar_labels (list[str] | None, optional): 每组内每个柱子的标签。默认为 None，使用 "Bar i"。
        bar_width (Num, optional): 单个柱子的宽度。默认为 0.2。
        bar_gap (Num, optional): 每组柱子之间的间距。默认为 0.1。
        bar_color (list[str] | None, optional): 每个柱子的颜色列表。默认为 None，使用灰色。
        errorbar_type (str, optional): 误差条类型，支持 "sd"（标准差）或 "se"（标准误）。默认为 "sd"。
        dots_color (str, optional): 散点的颜色。默认为 "gray"。
        dots_size (int, optional): 散点的大小。默认为 35。
        title_name (str, optional): 图标题。默认为空字符串。
        x_label_name (str, optional): X 轴标签。默认为空字符串。
        y_label_name (str, optional): Y 轴标签。默认为空字符串。
        statistic (bool, optional): 是否执行统计检验并显示显著性标注。默认为 False。
        test_method (str, optional): 统计检验方法。支持 "external"（外部 p 值）或其他方法。默认为 "external"。
        p_list (list[list[Num]] | None, optional): 外部提供的显著性 p 值列表。默认为 None。
        legend (bool, optional): 是否显示图例。默认为 True。
        legend_position (tuple[Num, Num], optional): 图例在坐标系中的位置。默认为 (1.2, 1)。
        **kwargs (Any): 其他可选参数，用于进一步定制图表样式。

    Returns:
        None
    """

    # 动态参数
    ax = ax or plt.gca()
    group_labels = group_labels or [f"Group {i + 1}" for i in range(len(data))]
    n_groups = len(data)

    # 把所有子列表展开成一个大列表
    all_values = [x for sublist1 in data for sublist2 in sublist1 for x in sublist2]

    x_positions_all = []
    for index_group, group_data in enumerate(data):
        n_bars = len(group_data)
        if bar_labels is None:
            bar_labels = [f"Bar {i + 1}" for i in range(n_bars)]
        if bar_color is None:
            bar_color = ["gray"] * n_bars

        x_positions = (
            np.arange(n_bars) * (bar_width + bar_gap)
            + bar_width / 2
            + index_group
            - (n_bars * bar_width + (n_bars - 1) * bar_gap) / 2
        )
        x_positions_all.append(x_positions)

        # 计算均值、标准差、标准误
        means = [compute_summary(group_data[i])[0] for i in range(n_bars)]
        sds = [compute_summary(group_data[i])[1] for i in range(n_bars)]
        ses = [compute_summary(group_data[i])[2] for i in range(n_bars)]
        if errorbar_type == "sd":
            error_values = sds
        elif errorbar_type == "se":
            error_values = ses
        # 绘制柱子
        bars = ax.bar(
            x_positions, means, width=bar_width, color=bar_color, alpha=1, edgecolor="k"
        )
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
        for index_bar, dot in enumerate(group_data):
            dot_x_pos = RNG.normal(
                x_positions[index_bar], scale=bar_width / 7, size=len(dot)
            )
            add_scatter(ax, dot_x_pos, dot, dots_color, dots_size=dots_size)
    if legend:
        ax.legend(bars, bar_labels, bbox_to_anchor=legend_position)

    # 美化
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(
        title_name,
        fontsize=kwargs.get("title_fontsize", 15),
        pad=kwargs.get("title_pad", 10),
    )
    # x轴
    ax.set_xlabel(x_label_name, fontsize=kwargs.get("x_label_fontsize", 10))
    ax.set_xticks(np.arange(n_groups))
    ax.set_xticklabels(
        group_labels,
        ha=kwargs.get("x_label_ha", "center"),
        rotation_mode="anchor",
        fontsize=kwargs.get("x_tick_fontsize", 10),
        rotation=kwargs.get("x_tick_rotation", 0),
    )
    # y轴
    ax.tick_params(
        axis="y",
        labelsize=kwargs.get("y_tick_fontsize", 10),
        rotation=kwargs.get("y_tick_rotation", 0),
    )
    ax.set_ylabel(y_label_name, fontsize=kwargs.get("y_label_fontsize", 10))
    set_yaxis(ax, all_values, kwargs)

    # 添加统计显著性标记
    if statistic:
        for index_group, group_data in enumerate(data):
            x_positions = x_positions_all[index_group]
            comparisons = []
            idx = 0
            for i in range(len(group_data)):
                for j in range(i + 1, len(group_data)):
                    if test_method == "external":
                        p = p_list[index_group][idx]
                        idx += 1
                    if p <= 0.05:
                        comparisons.append((x_positions[i], x_positions[j], p))
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
    pass


if __name__ == "__main__":
    main()
