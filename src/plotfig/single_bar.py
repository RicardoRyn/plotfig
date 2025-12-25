import warnings
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.colors import LinearSegmentedColormap, to_rgba
from matplotlib.patches import Polygon, Rectangle
from numpy.typing import NDArray
from scipy import stats

from .utils.bar import (
    annotate_significance,
    compute_summary,
    set_yaxis,
)

warnings.simplefilter("always")

Num = int | float | np.integer | np.floating
DataType = (
    np.ndarray  # 三维 ndarray
    | Sequence[np.ndarray]  # list[二维 ndarray]
    | Sequence[Sequence[Sequence[Num] | np.ndarray]]  # 纯 list 嵌套数字
)

__all__ = [
    "plot_one_group_bar_figure",
    "plot_one_group_violin_figure",
]


def _is_valid_data(data):
    if isinstance(data, np.ndarray):
        return data.ndim == 2
    if isinstance(data, (list, tuple)):
        for x in data:
            if isinstance(x, np.ndarray):
                if x.ndim != 1:
                    return False
            elif isinstance(x, (list, tuple)):
                if not all(isinstance(i, (int, float, np.floating)) for i in x):
                    return False
            else:
                return False
        return True
    return False


def _add_scatter(
    ax,
    x_pos,
    data,
    color,
    dots_size,
):
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


def _perform_stat_test(
    data1=None,
    data2=None,
    popmean=None,
    method="ttest_ind",
):
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


def _determine_test_modle(data, method, p_list=None, popmean=0):
    comparisons = []
    idx = 0
    if method != "ttest_1samp":
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if method == "external":
                    if p_list is None:
                        raise ValueError("p_list参数不能为空")
                    p = p_list[idx]
                    idx += 1
                else:
                    _, p = _perform_stat_test(
                        data1=data[i], data2=data[j], method=method
                    )
                if p <= 0.05:
                    comparisons.append((i, j, p))
    else:
        for i in range(len(data)):
            _, p = _perform_stat_test(data1=data[i], popmean=popmean, method=method)
            if p <= 0.05:
                comparisons.append((i, p))
    return comparisons


def _statistics(
    data,
    test_method,
    p_list,
    popmean,
    ax,
    all_values,
    statistical_line_color,
    asterisk_fontsize,
    asterisk_color,
    y_base,
    interval,
):
    if isinstance(test_method, list):
        if len(test_method) > 2 or (
            len(test_method) == 2 and "ttest_1samp" not in test_method
        ):
            raise ValueError(
                "test_method 最多只能有2个元素。且当元素数量为2时，其中之一必须是 'ttest_1samp'。"
            )

        for method in test_method:
            comparisons = _determine_test_modle(data, method, p_list, popmean)
            if not comparisons:
                return

            y_max = ax.get_ylim()[1]
            y_base = y_base or np.max(all_values)
            interval = interval or (y_max - np.max(all_values)) / (len(comparisons) + 1)

            color = (
                "b"
                if len(test_method) > 1 and method == "ttest_1samp"
                else asterisk_color
            )

            annotate_significance(
                ax,
                comparisons,
                y_base,
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
        comparisons = _determine_test_modle(data, test_method, p_list, popmean)
        if not comparisons:
            return

        y_max = ax.get_ylim()[1]
        y_base = y_base or np.max(all_values)
        interval = interval or (y_max - np.max(all_values)) / (len(comparisons) + 1)

        annotate_significance(
            ax,
            comparisons,
            y_base,
            interval,
            line_color=statistical_line_color,
            star_offset=interval / 5,
            fontsize=asterisk_fontsize,
            color=asterisk_color,
        )


def plot_one_group_bar_figure(
    data: Sequence[Sequence[Num] | np.ndarray],
    ax: Axes | None = None,
    labels_name: list[str] | None = None,
    colors: list[str] | None = None,
    edgecolor: str | None = None,
    gradient_color: bool = False,
    colors_start: list[str] | None = None,
    colors_end: list[str] | None = None,
    show_dots: bool = True,
    dots_color: list[list[str]] | None = None,
    width: Num = 0.5,
    color_alpha: Num = 1,
    dots_size: Num = 35,
    errorbar_type: str = "sd",
    title_name: str = "",
    title_fontsize: Num = 12,
    title_pad: Num = 10,
    x_label_name: str = "",
    x_label_ha: str = "center",
    x_label_fontsize: Num = 12,
    x_tick_fontsize: Num = 12,
    x_tick_rotation: Num = 0,
    y_label_name: str = "",
    y_label_fontsize: Num = 12,
    y_tick_fontsize: Num = 8,
    y_tick_rotation: Num = 0,
    y_lim: tuple[float, float] | None = None,
    statistic: bool = False,
    test_method: list[str] = ["ttest_ind"],
    p_list: list[float] | None = None,
    popmean: Num = 0,
    statistical_line_color: str = "0.5",
    asterisk_fontsize: Num = 10,
    asterisk_color: str = "k",
    y_base: float | None = None,
    interval: float | None = None,
    ax_bottom_is_0: bool = False,
    y_max_tick_is_1: bool = False,
    math_text: bool = True,
    one_decimal_place: bool = False,
    percentage: bool = False,
) -> Axes | None:
    """绘制单组柱状图，包含散点、误差条和统计显著性标记。

    Args:
        data (np.ndarray | Sequence[Sequence[Num] | np.ndarray]):
            输入数据，可以是二维numpy数组或嵌套序列，每个子序列代表一个柱状图的数据点
        ax (Axes | None, optional):
            matplotlib的坐标轴对象，如果为None则使用当前坐标轴. Defaults to None.
        labels_name (list[str] | None, optional):
            柱状图的标签名称列表. Defaults to None.
        colors (list[str] | None, optional):
            柱状图的颜色列表. Defaults to None.
        edgecolor (str | None, optional):
            柱状图边缘颜色. Defaults to None.
        gradient_color (bool, optional):
            是否使用渐变颜色填充柱状图. Defaults to False.
        colors_start (list[str] | None, optional):
            渐变色的起始颜色列表. Defaults to None.
        colors_end (list[str] | None, optional):
            渐变色的结束颜色列表. Defaults to None.
        show_dots (bool, optional):
            是否显示散点. Defaults to True.
        dots_color (list[list[str]] | None, optional):
            散点的颜色列表. Defaults to None.
        width (Num, optional):
            柱状图的宽度. Defaults to 0.5.
        color_alpha (Num, optional):
            柱状图颜色的透明度. Defaults to 1.
        dots_size (Num, optional):
            散点的大小. Defaults to 35.
        errorbar_type (str, optional):
            误差条类型，可选 "sd"(标准差) 或 "se"(标准误). Defaults to "sd".
        title_name (str, optional):
            图表标题. Defaults to "".
        title_fontsize (Num, optional):
            标题字体大小. Defaults to 12.
        title_pad (Num, optional):
            标题与图表的间距. Defaults to 10.
        x_label_name (str, optional):
            X轴标签名称. Defaults to "".
        x_label_ha (str, optional):
            X轴标签的水平对齐方式. Defaults to "center".
        x_label_fontsize (Num, optional):
            X轴标签字体大小. Defaults to 12.
        x_tick_fontsize (Num, optional):
            X轴刻度字体大小. Defaults to 12.
        x_tick_rotation (Num, optional):
            X轴刻度旋转角度. Defaults to 0.
        y_label_name (str, optional):
            Y轴标签名称. Defaults to "".
        y_label_fontsize (Num, optional):
            Y轴标签字体大小. Defaults to 12.
        y_tick_fontsize (Num, optional):
            Y轴刻度字体大小. Defaults to 8.
        y_tick_rotation (Num, optional):
            Y轴刻度旋转角度. Defaults to 0.
        y_lim (tuple[Num, Num] | None, optional):
            Y轴的范围限制. Defaults to None.
        statistic (bool, optional):
            是否进行统计显著性分析. Defaults to False.
        test_method (list[str], optional):
            统计检验方法列表，包括
            1. `ttest_ind`,
            2. `ttest_rel`,
            3. `ttest_1samp`,
            4. `mannwhitneyu`,
            5. `external`.
            Defaults to ["ttest_ind"].
        p_list (list[float] | None, optional):
            预计算的p值列表，用于显著性标记. Defaults to None.
        popmean (Num, optional):
            单样本t检验的假设均值. Defaults to 0.
        statistical_line_color (str, optional):
            显著性标记线的颜色. Defaults to "0.5".
        asterisk_fontsize (Num, optional):
            显著性星号的字体大小. Defaults to 10.
        asterisk_color (str, optional):
            显著性星号的颜色. Defaults to "k".
        y_base (float | None, optional):
            显著性连线的起始Y轴位置（高度）。如果为None，则使用内部算法自动计算一个合适的位置。Defaults to None.
        interval (float | None, optional):
            相邻显著性连线之间的垂直距离（Y轴增量）。如果为None，则使用内部算法根据图表范围和比较对数自动计算。Defaults to None.
        ax_bottom_is_0 (bool, optional):
            Y轴是否从0开始. Defaults to False.
        y_max_tick_is_1 (bool, optional):
            Y轴最大刻度是否限制为1. Defaults to False.
        math_text (bool, optional):
            是否将Y轴显示为科学计数法格式. Defaults to True.
        one_decimal_place (bool, optional):
            Y轴刻度是否只保留一位小数. Defaults to False.
        percentage (bool, optional):
            是否将Y轴显示为百分比格式. Defaults to False.

    Raises:
        ValueError: 当data数据格式无效时抛出
        ValueError: 当errorbar_type不是"sd"或"se"时抛出

    Returns:
        Axes | None: 返回matplotlib的坐标轴对象或None
    """
    # 处理None值
    if not _is_valid_data(data):
        raise ValueError("无效的 data")
    ax = ax or plt.gca()
    labels_name = labels_name or [str(i) for i in range(len(data))]
    colors = colors or ["gray"] * len(data)
    # 统一参数型
    width = float(width)
    color_alpha = float(color_alpha)
    dots_size = float(dots_size)
    title_fontsize = float(title_fontsize)
    title_pad = float(title_pad)
    x_label_fontsize = float(x_label_fontsize)
    x_tick_fontsize = float(x_tick_fontsize)
    x_tick_rotation = float(x_tick_rotation)
    y_label_fontsize = float(y_label_fontsize)
    y_tick_fontsize = float(y_tick_fontsize)
    y_tick_rotation = float(y_tick_rotation)
    popmean = float(popmean)
    asterisk_fontsize = float(asterisk_fontsize)

    x_positions = np.arange(len(labels_name))
    means, sds, ses = [], [], []
    scatter_positions = []
    for i, d in enumerate(data):
        mean, sd, se = compute_summary(np.array(d))
        means.append(mean)
        sds.append(sd)
        ses.append(se)
        # 创建随机数生成器
        rng = np.random.default_rng(seed=42)
        scatter_x = rng.normal(i, 0.1, len(d))
        scatter_positions.append(scatter_x)
    if errorbar_type == "sd":
        error_values = sds
    elif errorbar_type == "se":
        error_values = ses
    else:
        raise ValueError("errorbar_type 只能是 'sd' 或者 'se'")

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
            extent = (float(x - width / 2), float(x + width / 2), 0, h)
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
    if show_dots:
        for i, d in enumerate(data):
            if dots_color is None:
                _add_scatter(ax, scatter_positions[i], d, ["gray"] * len(d), dots_size)
            else:
                _add_scatter(ax, scatter_positions[i], d, dots_color[i], dots_size)

    # 美化
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(
        title_name,
        fontsize=title_fontsize,
        pad=float(title_pad),
    )
    # x轴
    ax.set_xlim(np.min(x_positions) - 0.5, np.max(x_positions) + 0.5)
    ax.set_xlabel(x_label_name, fontsize=x_label_fontsize)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(
        labels_name,
        fontsize=x_tick_fontsize,
        rotation=x_tick_rotation,
        ha=x_label_ha,
        rotation_mode="anchor",
    )
    # y轴
    ax.tick_params(
        axis="y",
        labelsize=y_tick_fontsize,
        rotation=y_tick_rotation,
    )
    ax.set_ylabel(y_label_name, fontsize=y_label_fontsize)
    all_values = np.concatenate([np.asarray(x) for x in data]).ravel()
    set_yaxis(
        ax,
        all_values,
        y_lim=y_lim,
        ax_bottom_is_0=ax_bottom_is_0,
        y_max_tick_is_1=y_max_tick_is_1,
        math_text=math_text,
        one_decimal_place=one_decimal_place,
        percentage=percentage,
    )

    # 添加统计显著性标记
    if statistic:
        _statistics(
            data,
            test_method,
            p_list,
            popmean,
            ax,
            all_values,
            statistical_line_color,
            asterisk_fontsize,
            asterisk_color,
            y_base,
            interval,
        )
    return ax


def plot_one_group_violin_figure(
    data: Sequence[list[float] | NDArray[np.float64]],
    ax: Axes | None = None,
    labels_name: list[str] | None = None,
    width: Num = 0.8,
    colors: list[str] | None = None,
    color_alpha: Num = 1,
    gradient_color: bool = False,
    colors_start: list[str] | None = None,
    colors_end: list[str] | None = None,
    show_dots: bool = False,
    dots_size: Num = 35,
    title_name: str = "",
    title_fontsize: Num = 12,
    title_pad: Num = 10,
    x_label_name: str = "",
    x_label_ha: str = "center",
    x_label_fontsize: Num = 10,
    x_tick_fontsize: Num = 8,
    x_tick_rotation: Num = 0,
    y_label_name: str = "",
    y_label_fontsize: Num = 10,
    y_tick_fontsize: Num = 8,
    y_tick_rotation: Num = 0,
    y_lim: tuple[float, float] | None = None,
    statistic: bool = False,
    test_method: list[str] = ["ttest_ind"],
    popmean: Num = 0,
    p_list: list[float] | None = None,
    statistical_line_color: str = "0.5",
    asterisk_fontsize: Num = 10,
    asterisk_color: str = "k",
    y_base: float | None = None,
    interval: float | None = None,
    ax_bottom_is_0: bool = False,
    y_max_tick_is_1: bool = False,
    math_text: bool = True,
    one_decimal_place: bool = False,
    percentage: bool = False,
) -> Axes | None:
    """绘制单组小提琴图，可选散点叠加、渐变填色和统计显著性标注。

    Args:
        data (Sequence[list[float] | NDArray[np.float64]]):
            输入数据，可以是二维numpy数组或嵌套序列，每个子序列代表一个小提琴的数据点
        ax (Axes | None, optional):
            matplotlib的坐标轴对象，如果为None则使用当前坐标轴. Defaults to None.
        labels_name (list[str] | None, optional):
            小提琴图的标签名称列表. Defaults to None.
        width (Num, optional):
            小提琴图的宽度. Defaults to 0.8.
        colors (list[str] | None, optional):
            小提琴图的颜色列表. Defaults to None.
        color_alpha (Num, optional):
            小提琴图颜色的透明度. Defaults to 1.
        gradient_color (bool, optional):
            是否使用渐变颜色填充小提琴图. Defaults to False.
        colors_start (list[str] | None, optional):
            渐变色的起始颜色列表. Defaults to None.
        colors_end (list[str] | None, optional):
            渐变色的结束颜色列表. Defaults to None.
        show_dots (bool, optional):
            是否显示散点. Defaults to False.
        dots_size (Num, optional):
            散点的大小. Defaults to 35.
        title_name (str, optional):
            图表标题. Defaults to "".
        title_fontsize (Num, optional):
            标题字体大小. Defaults to 12.
        title_pad (Num, optional):
            标题与图表的间距. Defaults to 10.
        x_label_name (str, optional):
            X轴标签名称. Defaults to "".
        x_label_ha (str, optional):
            X轴标签的水平对齐方式. Defaults to "center".
        x_label_fontsize (Num, optional):
            X轴标签字体大小. Defaults to 10.
        x_tick_fontsize (Num, optional):
            X轴刻度字体大小. Defaults to 8.
        x_tick_rotation (Num, optional):
            X轴刻度旋转角度. Defaults to 0.
        y_label_name (str, optional):
            Y轴标签名称. Defaults to "".
        y_label_fontsize (Num, optional):
            Y轴标签字体大小. Defaults to 10.
        y_tick_fontsize (Num, optional):
            Y轴刻度字体大小. Defaults to 8.
        y_tick_rotation (Num, optional):
            Y轴刻度旋转角度. Defaults to 0.
        y_lim (tuple[Num, Num] | None, optional):
            Y轴的范围限制. Defaults to None.
        statistic (bool, optional):
            是否进行统计显著性分析. Defaults to False.
        test_method (list[str], optional):
            统计检验方法列表. Defaults to ["ttest_ind"].
        popmean (Num, optional):
            单样本t检验的假设均值. Defaults to 0.
        p_list (list[float] | None, optional):
            预计算的p值列表，用于显著性标记. Defaults to None.
        statistical_line_color (str, optional):
            显著性标记线的颜色. Defaults to "0.5".
        asterisk_fontsize (Num, optional):
            显著性星号的字体大小. Defaults to 10.
        asterisk_color (str, optional):
            显著性星号的颜色. Defaults to "k".
        y_base (float | None, optional):
            显著性连线的起始Y轴位置（高度）。如果为None，则使用内部算法自动计算一个合适的位置。Defaults to None.
        interval (float | None, optional):
            相邻显著性连线之间的垂直距离（Y轴增量）。如果为None，则使用内部算法根据图表范围和比较对数自动计算。Defaults to None.
        ax_bottom_is_0 (bool, optional):
            Y轴是否从0开始. Defaults to False.
        y_max_tick_is_1 (bool, optional):
            Y轴最大刻度是否限制为1. Defaults to False.
        math_text (bool, optional):
            是否将Y轴显示为科学计数法格式. Defaults to True.
        one_decimal_place (bool, optional):
            Y轴刻度是否只保留一位小数. Defaults to False.
        percentage (bool, optional):
            是否将Y轴显示为百分比格式. Defaults to False.

    Raises:
        ValueError: 当data数据格式无效时抛出

    Returns:
        Axes | None: 返回matplotlib的坐标轴对象或None
    """
    # 处理None值
    if not _is_valid_data(data):
        raise ValueError("无效的 data")
    ax = ax or plt.gca()
    labels_name = labels_name or [str(i) for i in range(len(data))]
    colors = colors or ["gray"] * len(data)
    # 统一参数型
    width = float(width)
    color_alpha = float(color_alpha)
    dots_size = float(dots_size)
    title_fontsize = float(title_fontsize)
    title_pad = float(title_pad)
    x_label_fontsize = float(x_label_fontsize)
    x_tick_fontsize = float(x_tick_fontsize)
    x_tick_rotation = float(x_tick_rotation)
    y_label_fontsize = float(y_label_fontsize)
    y_tick_fontsize = float(y_tick_fontsize)
    y_tick_rotation = float(y_tick_rotation)
    popmean = float(popmean)
    asterisk_fontsize = float(asterisk_fontsize)

    def _draw_gradient_violin(ax, data, pos, width, c1, c2, color_alpha):
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
            Rectangle(
                (pos - width / 16, q1),  # 左下角坐标
                float(width / 8),  # 宽度
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
            if colors_start is None:
                colors_start = ["#e38a48"] * len(data)
            if colors_end is None:  # 默认颜色
                colors_end = ["#4573a5"] * len(data)
            c1 = colors_start[i]
            c2 = colors_end[i]
        else:
            c1 = c2 = colors[i]
        ymax, ymin = _draw_gradient_violin(ax, d, i, width, c1, c2, color_alpha)

        ymax_lst.append(ymax)
        ymin_lst.append(ymin)
    ymax = max(ymax_lst)
    ymin = min(ymin_lst)

    # 绘制散点（复用现有函数）
    if show_dots:
        # 创建随机数生成器
        rng = np.random.default_rng(seed=42)
        scatter_positions = [rng.normal(i, 0.1, len(d)) for i, d in enumerate(data)]
        for i, d in enumerate(data):
            _add_scatter(ax, scatter_positions[i], d, colors[i], dots_size)

    # 美化
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(title_name, fontsize=title_fontsize, pad=title_pad)
    # x轴
    ax.set_xlim(-0.5, len(data) - 0.5)
    ax.set_xlabel(x_label_name, fontsize=x_label_fontsize)
    ax.set_xticks(np.arange(len(data)))
    ax.set_xticklabels(
        labels_name,
        fontsize=x_tick_fontsize,
        rotation=x_tick_rotation,
        ha=x_label_ha,
        rotation_mode="anchor",
    )
    # y轴
    ax.tick_params(
        axis="y",
        labelsize=y_tick_fontsize,
        rotation=y_tick_rotation,
    )
    ax.set_ylabel(y_label_name, fontsize=y_label_fontsize)
    all_values = [ymin, ymax]
    set_yaxis(
        ax,
        all_values,
        y_lim=y_lim,
        ax_bottom_is_0=ax_bottom_is_0,
        y_max_tick_is_1=y_max_tick_is_1,
        math_text=math_text,
        one_decimal_place=one_decimal_place,
        percentage=percentage,
    )

    # 添加统计标记（复用现有函数）
    if statistic:
        _statistics(
            data,
            test_method,
            p_list,
            popmean,
            ax,
            all_values,
            statistical_line_color,
            asterisk_fontsize,
            asterisk_color,
            y_base,
            interval,
        )

    return ax
