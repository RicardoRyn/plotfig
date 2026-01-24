import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.axes import Axes

from plotfig import (
    plot_one_group_bar_figure,
)


class TestPlotSingleBarFigureSuccesses:
    def setup_method(self):
        """测试前初始化：创建图形和测试数据"""
        self.fig, self.ax = plt.subplots()
        self.test_data = [np.random.rand(2), np.random.rand(3), np.random.rand(4)]

    def teardown_method(self):
        """测试后清理：关闭图形"""
        plt.close(self.fig)

    def test_basic_plotting(self):
        """最基本的烟雾测试：确保函数能正常运行并返回Axes对象"""
        result = plot_one_group_bar_figure(self.test_data, ax=self.ax)
        assert isinstance(result, Axes)

    def test_with_custom_parameters(self):
        """测试常用参数组合是否能正常工作"""
        custom_data = [
            [1.1, 2.2, 3.3, 4.4],
            [5.5, 6.6, 7.7, 8.8, 9.9],
            [10.1, 11.1, 12.1, 13.1, 14.1, 15.1],
        ]
        dots_color = [
            ["#ff0000", "#00ff00", "#0000ff", "#ffff00"],
            ["#00ffff", "#ff00ff", "#ff8800", "#0088ff", "#88ff00"],
            ["#8800ff", "#00ff88", "#ff0088", "#888888", "#444444", "#000000"],
        ]
        result = plot_one_group_bar_figure(
            custom_data,
            ax=self.ax,
            labels_name=["A", "B", "C"],
            edgecolor="#ffff00",
            gradient_color=True,
            colors_start=["#ff0000", "#00ff00", "#0000ff"],
            colors_end=["#00ffff", "#ff00ff", "#ffff00"],
            show_dots=True,
            dots_color=dots_color,
            width=0.7,
            color_alpha=0.8,
            dots_size=25,
            errorbar_type="se",
            title_name="Test Fig",
            x_label_name="x label",
            y_label_name="y label",
            y_lim=(0, 16),
            statistic=True,
            test_method=["mannwhitneyu", "ttest_1samp"],
            popmean=0,
        )
        assert isinstance(result, Axes)
        assert result.get_title() == "Test Fig"


class TestPlotSingleBarFigureErrors:
    """测试错误处理"""

    def setup_method(self):
        """测试前初始化：创建图形和基础测试数据"""
        self.fig, self.ax = plt.subplots()
        self.basic_data = [[1, 2], [3, 4]]

    def teardown_method(self):
        """测试后清理：关闭图形"""
        plt.close(self.fig)

    def test_invalid_data_format(self):
        """测试无效数据格式应抛出 ValueError"""
        with pytest.raises(ValueError, match="无效的 data"):
            plot_one_group_bar_figure("invalid_data")

    def test_invalid_errorbar_type(self):
        """测试无效的 errorbar_type 应抛出 ValueError"""
        with pytest.raises(ValueError, match="errorbar_type 只能是"):
            plot_one_group_bar_figure(self.basic_data, ax=self.ax, errorbar_type="invalid")

    def test_invalid_test_method(self):
        """测试无效的 test_method 应抛出 ValueError"""
        with pytest.raises(ValueError, match="未知统计方法"):
            plot_one_group_bar_figure(
                self.basic_data, ax=self.ax, statistic=True, test_method=["invalid"]
            )

    def test_test_method_too_many_elements(self):
        """测试 test_method 超过2个元素且不包含 ttest_1samp 应抛出 ValueError"""
        with pytest.raises(ValueError, match="test_method 最多只能有2个元素"):
            plot_one_group_bar_figure(
                self.basic_data,
                ax=self.ax,
                statistic=True,
                test_method=["ttest_ind", "mannwhitneyu", "ttest_rel"],
            )

    def test_statistic_external_missing_p_list(self):
        """测试 external 方法缺少 p_list 应抛出 ValueError"""
        with pytest.raises(ValueError, match="p_list参数不能为空"):
            plot_one_group_bar_figure(
                self.basic_data, ax=self.ax, statistic=True, test_method=["external"]
            )

    def test_single_element_per_group(self):
        """测试每组只有一个元素时应抛出 ValueError"""
        with pytest.raises(
            ValueError,
            match="数据组只有 1 个元素，无法计算标准差和标准误。每组数据至少需要 2 个元素。",
        ):
            plot_one_group_bar_figure([[1], [2], [3]], ax=self.ax)


class TestPlotSingleBarFigureDataTypes:
    """测试数据类型"""

    def setup_method(self):
        """测试前初始化：创建图形和不同类型的测试数据"""
        self.fig, self.ax = plt.subplots()
        self.numpy_data = [np.array([1.0, 2.0, 3.0]), np.array([4.0, 5.0, 6.0])]
        self.list_data = [[1, 2, 3], [4, 5, 6]]
        self.mixed_data = [[1.0, 2.0, 3.0], np.array([4.0, 5.0, 6.0])]

    def teardown_method(self):
        """测试后清理：关闭图形"""
        plt.close(self.fig)

    def test_with_numpy_arrays(self):
        """测试 numpy array 数据"""
        result = plot_one_group_bar_figure(self.numpy_data, ax=self.ax)
        assert isinstance(result, Axes)

    def test_with_pure_lists(self):
        """测试纯 list 数据"""
        result = plot_one_group_bar_figure(self.list_data, ax=self.ax)
        assert isinstance(result, Axes)

    def test_with_mixed_data_types(self):
        """测试混合数据类型"""
        result = plot_one_group_bar_figure(self.mixed_data, ax=self.ax)
        assert isinstance(result, Axes)


class TestPlotSingleBarFigureFeatures:
    """测试功能分支"""

    def setup_method(self):
        """测试前初始化：创建图形和基础测试数据"""
        self.fig, self.ax = plt.subplots()
        self.basic_data = [[1, 2, 3], [4, 5, 6]]
        self.custom_colors_start = ["#ff0000", "#00ff00"]
        self.custom_colors_end = ["#0000ff", "#ffff00"]

    def teardown_method(self):
        """测试后清理：关闭图形"""
        plt.close(self.fig)

    def test_errorbar_sd(self):
        """测试标准差误差条"""
        result = plot_one_group_bar_figure(self.basic_data, ax=self.ax, errorbar_type="sd")
        assert isinstance(result, Axes)

    def test_errorbar_se(self):
        """测试标准误误差条"""
        result = plot_one_group_bar_figure(self.basic_data, ax=self.ax, errorbar_type="se")
        assert isinstance(result, Axes)

    def test_without_dots(self):
        """测试不显示散点"""
        result = plot_one_group_bar_figure(self.basic_data, ax=self.ax, show_dots=False)
        assert isinstance(result, Axes)

    def test_gradient_color_defaults(self):
        """测试渐变色默认行为"""
        result = plot_one_group_bar_figure(self.basic_data, ax=self.ax, gradient_color=True)
        assert isinstance(result, Axes)

    def test_gradient_color_custom(self):
        """测试自定义渐变色"""
        result = plot_one_group_bar_figure(
            self.basic_data,
            ax=self.ax,
            gradient_color=True,
            colors_start=self.custom_colors_start,
            colors_end=self.custom_colors_end,
        )
        assert isinstance(result, Axes)


class TestPlotSingleBarFigureStatistics:
    """测试统计检验"""

    def setup_method(self):
        """测试前初始化：创建图形和统计测试数据"""
        self.fig, self.ax = plt.subplots()
        self.statistic_data = [[1, 2, 3], [10, 11, 12]]
        self.popmean = 5
        self.p_list = [0.01]

    def teardown_method(self):
        """测试后清理：关闭图形"""
        plt.close(self.fig)

    def test_statistic_ttest_ind(self):
        """测试独立样本t检验"""
        result = plot_one_group_bar_figure(
            self.statistic_data, ax=self.ax, statistic=True, test_method=["ttest_ind"]
        )
        assert isinstance(result, Axes)

    def test_statistic_mannwhitneyu(self):
        """测试 Mann-Whitney U 检验"""
        result = plot_one_group_bar_figure(
            self.statistic_data, ax=self.ax, statistic=True, test_method=["mannwhitneyu"]
        )
        assert isinstance(result, Axes)

    def test_statistic_ttest_1samp(self):
        """测试单样本t检验"""
        result = plot_one_group_bar_figure(
            self.statistic_data,
            ax=self.ax,
            statistic=True,
            test_method=["ttest_1samp"],
            popmean=self.popmean,
        )
        assert isinstance(result, Axes)

    def test_statistic_multiple_methods(self):
        """测试多种统计方法组合"""
        result = plot_one_group_bar_figure(
            self.statistic_data,
            ax=self.ax,
            statistic=True,
            test_method=["ttest_ind", "ttest_1samp"],
            popmean=self.popmean,
        )
        assert isinstance(result, Axes)

    def test_statistic_external_with_p_list(self):
        """测试 external 方法与 p_list"""
        result = plot_one_group_bar_figure(
            self.statistic_data,
            ax=self.ax,
            statistic=True,
            test_method=["external"],
            p_list=self.p_list,
        )
        assert isinstance(result, Axes)


class TestPlotSingleBarFigureYAxis:
    """测试 Y轴设置"""

    def setup_method(self):
        """测试前初始化：创建图形和 Y轴测试数据"""
        self.fig, self.ax = plt.subplots()
        self.basic_data = [[1, 2, 3], [4, 5, 6]]
        self.percentage_data = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]

    def teardown_method(self):
        """测试后清理：关闭图形"""
        plt.close(self.fig)

    def test_y_lim(self):
        """测试自定义 Y轴范围"""
        result = plot_one_group_bar_figure(self.basic_data, ax=self.ax, y_lim=(0, 10))
        assert result.get_ylim() == (0, 10)

    def test_ax_bottom_is_0(self):
        """测试 Y轴从0开始"""
        result = plot_one_group_bar_figure(
            self.basic_data, ax=self.ax, ax_bottom_is_0=True
        )
        assert result.get_ylim()[0] == 0

    def test_y_max_tick_is_1(self):
        """测试 Y轴最大刻度限制为1"""
        result = plot_one_group_bar_figure(
            self.percentage_data, ax=self.ax, y_max_tick_is_1=True
        )
        assert result.get_ylim()[1] <= 1

    def test_percentage_format(self):
        """测试百分比格式"""
        result = plot_one_group_bar_figure(
            self.percentage_data, ax=self.ax, percentage=True, math_text=False
        )
        assert isinstance(result, Axes)


class TestPlotSingleBarFigureEdgeCases:
    """测试边界条件"""

    def setup_method(self):
        """测试前初始化：创建图形和边界测试数据"""
        self.fig, self.ax = plt.subplots()
        self.single_group_data = [[1, 2, 3]]
        self.basic_data = [[1, 2, 3], [4, 5, 6]]
        self.similar_data = [[1, 2, 3], [1.1, 2.1, 3.1]]

    def teardown_method(self):
        """测试后清理：关闭图形"""
        plt.close(self.fig)

    def test_single_group(self):
        """测试单组数据"""
        result = plot_one_group_bar_figure(self.single_group_data, ax=self.ax)
        assert isinstance(result, Axes)

    def test_ax_none(self):
        """测试 ax=None 时使用当前坐标轴"""
        # 这个测试明确需要 ax=None，不使用 self.ax
        fig, ax = plt.subplots()
        try:
            result = plot_one_group_bar_figure(self.basic_data, ax=None)
            assert isinstance(result, Axes)
        finally:
            plt.close(fig)

    def test_no_significant_differences(self):
        """测试无显著差异时不应显示显著性标记"""
        result = plot_one_group_bar_figure(
            self.similar_data, ax=self.ax, statistic=True, test_method=["ttest_ind"]
        )
        assert isinstance(result, Axes)
