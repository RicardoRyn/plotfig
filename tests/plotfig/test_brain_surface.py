import matplotlib.pyplot as plt
import pytest
from matplotlib.axes import Axes

from plotfig import plot_brain_surface_figure


class TestPlotBrainSurfaceFigureSuccesses:
    """测试 plot_brain_surface_figure 函数的正常绘图功能"""

    def setup_method(self):
        """测试前初始化：创建图形和测试数据"""
        self.fig, self.ax = plt.subplots()
        self.test_data = {
            "lh_V1": 1.0,
            "rh_V2": 2.0,
        }

    def teardown_method(self):
        """测试后清理：关闭图形"""
        plt.close(self.fig)

    def test_basic_plotting(self):
        """最基本的烟雾测试：确保函数能正常运行并返回Axes对象"""
        result = plot_brain_surface_figure(self.test_data, ax=self.ax)

        assert isinstance(result, Axes)

    def test_with_custom_parameters(self):
        """测试自定义参数（species、atlas、colorbar等）是否能正常工作"""
        custom_data = {
            "lh_MST": 1.0,
            "rh_FST": 2.0,
        }

        result = plot_brain_surface_figure(
            custom_data,
            species="macaque",
            atlas="charm6",
            surf="midthickness",
            ax=self.ax,
            vmin=0,
            vmax=5,
            cmap="Reds",
            colorbar=True,
            colorbar_location="right",
            colorbar_label_name="Myelin Content",
            colorbar_label_rotation=0,
            colorbar_decimals=2,
            colorbar_fontsize=10,
            colorbar_nticks=3,
            colorbar_shrink=0.2,
            colorbar_aspect=9,
            colorbar_draw_border=True,
            title_name="测试图",
            title_fontsize=13,
            as_outline=False,
        )

        assert isinstance(result, Axes)
        assert result.get_title() == "测试图"

    def test_vmin_equals_vmax(self):
        """测试 vmin 等于 vmax 时的特殊处理"""
        data = {"lh_V1": 5.0, "rh_V2": 5.0}
        result = plot_brain_surface_figure(data, ax=self.ax, vmin=5, vmax=5)
        assert isinstance(result, Axes)

    def test_negative_values(self):
        """测试负数值"""
        data = {"lh_V1": -1.0, "rh_V2": -2.0}
        result = plot_brain_surface_figure(data, ax=self.ax)
        assert isinstance(result, Axes)

    def test_large_values(self):
        """测试大数值"""
        data = {"lh_V1": 1000.0, "rh_V2": 200000.0}
        result = plot_brain_surface_figure(data, ax=self.ax)
        assert isinstance(result, Axes)


class TestPlotBrainSurfaceFigureErrors:
    """测试 plot_brain_surface_figure 函数的参数验证和异常处理"""

    @staticmethod
    def test_empty_data_raises_error():
        """测试空数据应该抛出异常"""
        with pytest.raises(ValueError, match="data 不能为空"):
            plot_brain_surface_figure({})

    @staticmethod
    def test_vmin_greater_than_vmax_raises_error():
        """测试vmin大于vmax时应该抛出异常"""
        data = {"lh_V1": 1.0}

        with pytest.raises(ValueError, match="vmin必须小于等于vmax"):
            plot_brain_surface_figure(data, vmin=10, vmax=5)

    @staticmethod
    def test_unsupported_species_raises_error():
        """测试不支持的物种应该抛出异常"""
        data = {"lh_V1": 1.0}

        with pytest.raises(ValueError, match="不支持的物种"):
            plot_brain_surface_figure(data, species="dog")

    @staticmethod
    def test_unsupported_atlas_raises_error():
        """测试不支持的图集应该抛出异常"""
        data = {"lh_V1": 1.0}

        with pytest.raises(ValueError, match="不支持的图集"):
            plot_brain_surface_figure(data, atlas="invalid_atlas")

    @staticmethod
    def test_invalid_region_label_raises_error():
        """测试脑区标签在图集中找不到时应该抛出异常"""
        data = {"lh_invalid_region": 1.0}
        with pytest.raises(ValueError, match="以下脑区标签在指定图集中未找到"):
            plot_brain_surface_figure(data)
