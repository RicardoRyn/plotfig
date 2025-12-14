import warnings
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

from .utils.bar import (
    _annotate_significance,
    _compute_summary,
    _set_yaxis,
)

warnings.simplefilter("always")

Num = int | float | np.integer | np.floating

__all__ = [
    "plot_multi_group_bar_figure",
]


def _data_valiation(data):
    # 验证数据结构：必须是三层嵌套
    if not isinstance(data, (Sequence, np.ndarray)):
        raise ValueError(
            f"data 必须是序列类型（list, tuple）或 numpy 数组，"
            f"当前类型为 {type(data).__name__}"
        )
    if len(data) == 0:
        raise ValueError("data 不能为空，至少需要一个组")
    # 收集每个组的 bar 数量，用于后续检查一致性
    n_bars = []
    # 验证第一层和第二层
    for i, group in enumerate(data):
        if not isinstance(group, (Sequence, np.ndarray)):
            raise ValueError(
                f"data[{i}] 必须是序列或数组类型，当前类型为 {type(group).__name__}"
            )
        if len(group) == 0:
            raise ValueError(f"data[{i}] 不能为空，每个组至少需要一个柱子")
        # 记录当前组的 bar 数量
        n_bars.append(len(group))
        # 验证第二层和第三层
        for j, bar in enumerate(group):
            if not isinstance(bar, (Sequence, np.ndarray)):
                raise ValueError(
                    f"data[{i}][{j}] 必须是序列或数组类型，当前类型为 {type(bar).__name__}"
                )
            if len(bar) == 0:
                raise ValueError(f"data[{i}][{j}] 不能为空，每个柱子至少需要一个数据点")
            # 验证第三层：检查是否为数值类型
            for k, value in enumerate(bar):
                if not isinstance(value, (int, float, np.integer, np.floating)):
                    raise ValueError(
                        f"data[{i}][{j}][{k}] 必须是数值类型，"
                        f"当前值为 {value!r}，类型为 {type(value).__name__}"
                    )
    # 检查所有组的 bar 数量是否一致
    if len(set(n_bars)) > 1:
        # 构建详细的错误信息
        error_details = [
            f"data[{i}] 有 {count} 个柱子" for i, count in enumerate(n_bars)
        ]
        raise ValueError(
            "所有组的柱子数量必须一致，但发现不同的数量：\n" + "\n".join(error_details)
        )


def plot_multi_group_bar_figure(
    data: Sequence[Sequence[Sequence[float]]],
    ax: Axes | None = None,
    group_labels: list[str] | None = None,
    bar_labels: list[str] | None = None,
    bar_width: Num = 0.2,
    bar_gap: Num = 0.1,
    bar_color: list[str] | None = None,
    errorbar_type: str = "sd",
    dots_color: str = "gray",
    dots_size: int = 35,
    legend: bool = True,
    legend_position: tuple[Num, Num] = (1.2, 1),
    title_name: str = "",
    title_fontsize=12,
    title_pad=10,
    x_label_name: str = "",
    x_label_ha="center",
    x_label_fontsize=10,
    x_tick_fontsize=8,
    x_tick_rotation=0,
    y_label_name: str = "",
    y_label_fontsize=10,
    y_tick_fontsize=8,
    y_tick_rotation=0,
    y_lim: tuple[float, float] | None = None,
    statistic: bool = False,
    test_method: str = "external",
    p_list: list[list[Num]] | None = None,
    line_color="0.5",
    asterisk_fontsize=10,
    asterisk_color="k",
    y_base: float | None = None,
    interval: float | None = None,
    ax_bottom_is_0: bool = False,
    y_max_tick_is_1: bool = False,
    math_text: bool = True,
    one_decimal_place: bool = False,
    percentage: bool = False,
) -> Axes:
    """绘制多组分组条形图，支持误差线、散点叠加和统计显著性标注。

    该函数用于可视化多组数据的比较，每组包含多个柱子，每个柱子显示均值、误差线
    和原始数据点。特别适用于认知神经科学中的组间比较分析。

    Args:
        data (Sequence[Sequence[Sequence[float]]]): 三层嵌套的数据结构
            - 第一层：组 (groups)
            - 第二层：每组内的柱子 (bars)，所有组的柱子数量必须一致
            - 第三层：每个柱子内的数据点 (points)，数量可以不同
        ax (Axes | None): matplotlib 的 Axes 对象。如果为 None，使用当前活动的 Axes。
        group_labels (list[str] | None): 每个组的标签。如果为 None，自动生成 "Group 1", "Group 2" 等。
        bar_labels (list[str] | None): 每个柱子的标签，用于图例。如果为 None，自动生成 "Bar 1", "Bar 2" 等。
        bar_width (Num): 柱子的宽度。默认为 0.2。
        bar_gap (Num): 同一组内柱子之间的间隔。默认为 0.1。
        bar_color (list[str] | None): 每个柱子的颜色列表。如果为 None，所有柱子使用灰色。
        errorbar_type (str): 误差线类型，'sd' 表示标准差，'se' 表示标准误。默认为 'sd'。
        dots_color (str): 散点的颜色。默认为 'gray'。
        dots_size (int): 散点的大小。默认为 35。
        legend (bool): 是否显示图例。默认为 True。
        legend_position (tuple[Num, Num]): 图例位置，使用 bbox_to_anchor 坐标。默认为 (1.2, 1)。
        title_name (str): 图表标题。默认为空字符串。
        title_fontsize (int): 标题字体大小。默认为 12。
        title_pad (int): 标题与图表的间距。默认为 10。
        x_label_name (str): x 轴标签文本。默认为空字符串。
        x_label_ha (str): x 轴刻度标签的水平对齐方式。默认为 'center'。
        x_label_fontsize (int): x 轴标签字体大小。默认为 10。
        x_tick_fontsize (int): x 轴刻度字体大小。默认为 8。
        x_tick_rotation (int): x 轴刻度旋转角度。默认为 0。
        y_label_name (str): y 轴标签文本。默认为空字符串。
        y_label_fontsize (int): y 轴标签字体大小。默认为 10。
        y_tick_fontsize (int): y 轴刻度字体大小。默认为 8。
        y_tick_rotation (int): y 轴刻度旋转角度。默认为 0。
        y_lim (tuple[float, float] | None): 手动指定的 y 轴范围 (y_min, y_max)。
            如果为 None，根据数据自动计算。
        statistic (bool): 是否添加统计显著性标注。默认为 False。
        test_method (str): 统计检验方法。当前仅支持 'external'（使用外部提供的 p 值）。
        p_list (list[list[Num]] | None): 外部提供的 p 值列表。
            结构为 [组1的p值列表, 组2的p值列表, ...]，每个组的 p 值列表对应该组内所有两两比较。
            当 statistic=True 且 test_method='external' 时必须提供。
        line_color (str): 显著性标注连线的颜色。默认为 '0.5'（中灰色）。
        asterisk_fontsize (int): 显著性星号的字体大小。默认为 10。
        asterisk_color (str): 显著性星号的颜色。默认为 'k'（黑色）。
        y_base (float | None): 显著性标注的起始 y 坐标。如果为 None，自动计算为数据最大值。
        interval (float | None): 多个显著性标注之间的垂直间隔。
            如果为 None，自动计算为 (y_max - 数据最大值) / (比较数量 + 1)。
        ax_bottom_is_0 (bool): 是否将 y 轴底部固定为 0。默认为 False。
        y_max_tick_is_1 (bool): 是否将最大刻度限制为 1。默认为 False。
        math_text (bool): 是否使用科学计数法格式。默认为 True。
        one_decimal_place (bool): 是否将刻度格式化为一位小数。默认为 False。
        percentage (bool): 是否将刻度格式化为百分比形式。默认为 False。

    Returns:
        Axes: 包含绘制内容的 matplotlib Axes 对象。

    Raises:
        ValueError: 当 data 不是三层嵌套结构时抛出。
        ValueError: 当所有组的柱子数量不一致时抛出。
        ValueError: 当 errorbar_type 不是 'sd' 或 'se' 时抛出。
        ValueError: 当 statistic=True 且 test_method='external' 但 p_list 为 None 时抛出。

    Examples:
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> from plotfig import plot_multi_group_bar_figure
        >>>
        >>> # 创建示例数据：2 组，每组 3 个柱子
        >>> data = [
        ...     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ...     [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
        ... ]
        >>>
        >>> # 绘制基本图表
        >>> fig, ax = plt.subplots(figsize=(8, 6))
        >>> ax = plot_multi_group_bar_figure(
        ...     data,
        ...     ax=ax,
        ...     group_labels=['Control', 'Treatment'],
        ...     bar_labels=['Condition A', 'Condition B', 'Condition C'],
        ...     title_name='Multi-Group Comparison'
        ... )
        >>> fig.show()

    Notes:
        - 显著性星号规则：* (p≤0.05), ** (p≤0.01), *** (p≤0.001)
    """
    _data_valiation(data)

    n_groups = len(data)
    n_bars = len(data[0])

    ax = ax or plt.gca()
    group_labels = group_labels or [f"Group {i + 1}" for i in range(len(data))]
    bar_labels = bar_labels or [f"Bar {i + 1}" for i in range(n_bars)]
    bar_color = bar_color or ["gray"] * n_bars

    # 把所有子列表展开成一个大列表
    all_values = [x for sublist1 in data for sublist2 in sublist1 for x in sublist2]

    x_positions_all = []
    for index_group, group_data in enumerate(data):
        x_positions = (
            np.arange(n_bars) * (bar_width + bar_gap)
            + bar_width / 2
            + index_group
            - (n_bars * bar_width + (n_bars - 1) * bar_gap) / 2
        )
        x_positions_all.append(x_positions)

        # 计算均值、标准差、标准误
        means = [_compute_summary(group_data[i])[0] for i in range(n_bars)]
        sds = [_compute_summary(group_data[i])[1] for i in range(n_bars)]
        ses = [_compute_summary(group_data[i])[2] for i in range(n_bars)]
        if errorbar_type == "sd":
            error_values = sds
        elif errorbar_type == "se":
            error_values = ses
        else:
            raise ValueError("errorbar_type 只能是 'sd' 或者 'se'")
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
            # 创建随机数生成器
            rng = np.random.default_rng(seed=42)
            dot_x_pos = rng.normal(
                x_positions[index_bar], scale=bar_width / 7, size=len(dot)
            )
            ax.scatter(
                dot_x_pos,
                dot,
                c=dots_color,
                s=dots_size,
                edgecolors="white",
                linewidths=1,
                alpha=0.5,
            )

    if legend:
        ax.legend(bars, bar_labels, bbox_to_anchor=legend_position)

    # 美化
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(
        title_name,
        fontsize=title_fontsize,
        pad=title_pad,
    )
    # x轴
    ax.set_xlabel(x_label_name, fontsize=x_label_fontsize)
    ax.set_xticks(np.arange(n_groups))
    ax.set_xticklabels(
        group_labels,
        ha=x_label_ha,
        rotation_mode="anchor",
        fontsize=x_tick_fontsize,
        rotation=x_tick_rotation,
    )
    # y轴
    ax.tick_params(
        axis="y",
        labelsize=y_tick_fontsize,
        rotation=y_tick_rotation,
    )
    ax.set_ylabel(y_label_name, fontsize=y_label_fontsize)
    _set_yaxis(
        ax,
        all_values,
        y_lim,
        ax_bottom_is_0,
        y_max_tick_is_1,
        math_text,
        one_decimal_place,
        percentage,
    )

    # 添加统计显著性标记
    if statistic:
        for index_group, group_data in enumerate(data):
            x_positions = x_positions_all[index_group]
            comparisons = []
            idx = 0
            for i in range(len(group_data)):
                for j in range(i + 1, len(group_data)):
                    if test_method == "external":
                        if p_list is None:
                            raise ValueError("p_list不能为空")
                        p = p_list[index_group][idx]
                        idx += 1
                    else:
                        raise ValueError("多组数据统计测试方法暂时仅支持 external方法")
                    if p <= 0.05:
                        comparisons.append((x_positions[i], x_positions[j], p))
            y_max = ax.get_ylim()[1]
            y_base = y_base or np.max(all_values)
            interval = interval or (y_max - np.max(all_values)) / (len(comparisons) + 1)

            _annotate_significance(
                ax,
                comparisons,
                y_base,
                interval,
                line_color=line_color,
                star_offset=interval / 5,
                fontsize=asterisk_fontsize,
                color=asterisk_color,
            )

    return ax
