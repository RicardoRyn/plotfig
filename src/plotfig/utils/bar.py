import warnings
from typing import Sequence

import numpy as np
from matplotlib.axes import Axes
from matplotlib.ticker import FormatStrFormatter, FuncFormatter, ScalarFormatter
from numpy.typing import ArrayLike

Num = int | float | np.integer | np.floating


def _compute_summary(data: ArrayLike) -> tuple[float, float, float]:
    """计算数据的统计摘要信息，包括均值、标准差和标准误。

    该函数用于为条形图和小提琴图等可视化提供统计度量，特别是用于绘制误差线。
    标准差使用贝塞尔校正(ddof=1)计算，适用于样本数据的无偏估计。

    Args:
        data (array-like): 一维数值数据数组，用于计算统计摘要。

    Returns:
        tuple: 包含三个元素的元组 (mean, sd, se)
            - mean (float): 数据的算术平均值
            - sd (float): 样本标准差（使用贝塞尔校正）
            - se (float): 标准误（标准差除以样本量的平方根）

    Examples:
        >>> data = [1, 2, 3, 4, 5]
        >>> mean, sd, se = _compute_summary(data)
        >>> print(f"Mean: {mean:.2f}, SD: {sd:.2f}, SE: {se:.2f}")
        Mean: 3.00, SD: 1.58, SE: 0.71
    """
    data = np.asarray(data)
    mean = np.mean(data)
    sd = np.std(data, ddof=1)
    se = sd / np.sqrt(len(data))
    return float(mean), float(sd), float(se)


def _set_yaxis(
    ax: Axes,
    data: ArrayLike,
    y_lim: tuple[float, float] | None,
    ax_bottom_is_0: bool,
    y_max_tick_is_1: bool,
    math_text: bool,
    one_decimal_place: bool,
    percentage: bool,
) -> None:
    """设置图表的 y 轴范围和格式。

    该函数提供灵活的 y 轴配置选项，包括自动计算美观的轴范围（使用黄金比例）、
    多种数值格式化方式（科学计数法、小数、百分比）以及刻度限制功能。

    Args:
        ax (Axes): matplotlib 的 Axes 对象，用于设置 y 轴属性。
        data (ArrayLike): 数值数据数组，用于计算 y 轴的自动范围。
        y_lim (tuple[float, float] | None): 手动指定的 y 轴范围 (y_min, y_max)。
            如果为 None，则根据数据自动计算范围。
        ax_bottom_is_0 (bool): 是否将 y 轴底部固定为 0。
            当为 True 时，y 轴最小值始终为 0，适用于不包含负值的数据。
        y_max_tick_is_1 (bool): 是否将最大刻度限制为 1。
            当为 True 时，移除所有大于 1 的刻度，适用于比例或概率数据。
        math_text (bool): 是否使用科学计数法格式。
            当数据范围超出 [0.1, 100] 时启用，使用 10^n 的形式显示。
        one_decimal_place (bool): 是否将刻度格式化为一位小数。
            与 math_text 互斥，同时启用会发出警告。
        percentage (bool): 是否将刻度格式化为百分比形式。
            与 math_text 互斥，同时启用会发出警告。

    Notes:
        - 自动范围计算使用黄金比例（φ-1 ≈ 0.618）来确定上下边距，使图表更加美观
        - math_text、one_decimal_place 和 percentage 三个格式化选项互斥，
          同时启用多个会导致冲突并发出警告
        - 函数直接修改传入的 ax 对象，不返回任何值

    Examples:
        >>> import matplotlib.pyplot as plt
        >>> import numpy as np
        >>> fig, ax = plt.subplots()
        >>> data = np.random.randn(100)
        >>> _set_yaxis(ax, data, None, False, False, True, False, False)
    """
    data = np.asarray(data)

    if y_lim:
        ax.set_ylim(y_lim)
    else:
        y_min, y_max = np.min(data), np.max(data)
        y_range = y_max - y_min
        golden_ratio = 5**0.5 - 1
        ax_min = 0 if ax_bottom_is_0 else y_min - (y_range / golden_ratio - y_range / 2)
        ax_max = y_max + (y_range / golden_ratio - y_range / 2)
        ax.set_ylim(ax_min, ax_max)

    if y_max_tick_is_1:
        ticks = [tick for tick in ax.get_yticks() if tick <= 1]
        ax.set_yticks(ticks)

    if math_text and (np.min(data) < 0.1 or np.max(data) > 100):
        formatter = ScalarFormatter(useMathText=True)
        formatter.set_powerlimits((-2, 2))
        ax.yaxis.set_major_formatter(formatter)

    if one_decimal_place:
        if math_text:
            warnings.warn(
                "“one_decimal_place”会与“math_text”冲突，请关闭“math_text”后再开启！",
                UserWarning,
            )
        else:
            ax.yaxis.set_major_formatter(FormatStrFormatter("%.1f"))

    if percentage:
        if math_text:
            warnings.warn(
                "“percentage”会与“math_text”冲突，请关闭“math_text”后再开启！",
                UserWarning,
                stacklevel=2,
            )
        else:
            ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x:.0%}"))


def _annotate_significance(
    ax: Axes,
    comparisons: Sequence[tuple[int, int, float]] | Sequence[tuple[int, float]],
    y_base: float,
    interval: float,
    line_color: str,
    star_offset: float,
    fontsize: int | float,
    color: str,
) -> None:
    """在图表上添加统计显著性标注（星号和连线）。

    该函数支持两种显著性标注模式：
    1. 组间比较模式：在两组之间绘制连线，并在连线上方标注显著性星号
    2. 单样本模式：直接在数据点上方标注显著性星号

    显著性星号规则：
    - * : 0.001 < p ≤ 0.01
    - ** : 0.001 < p ≤ 0.01
    - *** : p ≤ 0.001

    Args:
        ax (Axes): matplotlib 的 Axes 对象，用于绘制标注。
        comparisons (Sequence[tuple[int, int, float]] | Sequence[tuple[int, float]]):
            显著性比较数据，支持两种格式：
            - 三元组序列 [(i, j, p_value), ...]：组间比较，i 和 j 是组索引，p_value 是 p 值
            - 二元组序列 [(i, p_value), ...]：单样本检验，i 是组索引，p_value 是 p 值
        y_base (float): 显著性标注的基准 y 坐标位置。
        interval (float): 多个显著性标注之间的垂直间隔，用于避免重叠。
        line_color (str): 连线的颜色（仅用于组间比较模式）。
        star_offset (float): 星号相对于连线的垂直偏移量。
        fontsize (int | float): 星号的字体大小。
        color (str): 星号的颜色。

    Notes:
        - 组间比较模式会自动堆叠多个比较，每个比较占据一个 interval 的高度
        - 星号位置在组间比较模式中位于两组的中点，单样本模式中位于组的正上方
        - 函数直接修改传入的 ax 对象，不返回任何值

    Examples:
        >>> import matplotlib.pyplot as plt
        >>> fig, ax = plt.subplots()
        >>> # 组间比较模式
        >>> comparisons = [(0, 1, 0.001), (1, 2, 0.03)]
        >>> _annotate_significance(ax, comparisons, 5.0, 0.5, 'black', 0.1, 12, 'red')
        >>> # 单样本模式
        >>> comparisons = [(0, 0.02), (1, 0.005)]
        >>> _annotate_significance(ax, comparisons, 5.0, 0.5, 'black', 0.1, 12, 'red')
    """

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
                    color=line_color, width=0.5, headwidth=0.1, headlength=0.1
                ),
            )
            _stars(pval, (i + j) / 2, y + star_offset, color, fontsize)
    elif len(comparisons[0]) == 2:
        for i_pval in comparisons:
            i, pval = i_pval[0], i_pval[1]
            y = y_base
            _stars(pval, i, y + star_offset, color, fontsize)
