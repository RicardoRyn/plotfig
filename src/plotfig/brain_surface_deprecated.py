import os.path as op
import math
import numpy as np
import pandas as pd
import nibabel as nib
from matplotlib.ticker import ScalarFormatter
from matplotlib.cm import ScalarMappable
from surfplot import Plot

from typing import TypeAlias
import numpy.typing as npt
import matplotlib.pyplot as plt
import warnings  # 在顶部导入

# 类型别名定义
Num: TypeAlias = float | int  # 可同时接受int和float的类型
NumArray: TypeAlias = list[Num] | npt.NDArray[np.float64]  # 数字数组类型

__all__ = [
    "plot_human_brain_figure",
    "plot_human_hemi_brain_figure",
    "plot_macaque_brain_figure",
    "plot_macaque_hemi_brain_figure",
    "plot_chimpanzee_brain_figure",
    "plot_chimpanzee_hemi_brain_figure",
]


def plot_human_brain_figure(
    data: dict[str, float],
    surf: str = "veryinflated",
    atlas: str = "glasser",
    vmin: Num | None = None,
    vmax: Num | None = None,
    plot: bool = True,
    cmap: str = "Reds",
    as_outline: bool = False,
    colorbar: bool = True,
    colorbar_location: str = "right",
    colorbar_label_name: str = "",
    colorbar_label_rotation: int = 0,
    colorbar_decimals: int = 1,
    colorbar_fontsize: int = 8,
    colorbar_nticks: int = 2,
    colorbar_shrink: float = 0.15,
    colorbar_aspect: int = 8,
    colorbar_draw_border: bool = False,
    title_name: str = "",
    title_fontsize: int = 15,
    title_y: float = 0.9,
    rjx_colorbar: bool = False,
    rjx_colorbar_direction: str = "vertical",
    horizontal_center: bool = True,
    rjx_colorbar_outline: bool = False,
    rjx_colorbar_label_name: str = "",
    rjx_colorbar_tick_fontsize: int = 10,
    rjx_colorbar_label_fontsize: int = 10,
    rjx_colorbar_tick_rotation: int = 0,
    rjx_colorbar_tick_length: int = 0,
    rjx_colorbar_nticks: int = 2,
) -> plt.Figure | tuple[np.ndarray, np.ndarray]:
    """
    绘制人类大脑表面图，支持 Glasser 和 BNA 图谱。

    Args:
        data (dict[str, float]): 包含 ROI 名称及其对应值的字典。
        surf (str, optional): 大脑表面类型（如 "veryinflated", "inflated"）。默认为 "veryinflated"。
        atlas (str, optional): 使用的图谱名称，支持 "glasser" 或 "bna"。默认为 "glasser"。
        vmin (Num, optional): 颜色映射的最小值。可以是整数或浮点数。默认为 None。
        vmax (Num, optional): 颜色映射的最大值。可以是整数或浮点数。默认为 None。
        plot (bool, optional): 是否直接绘制图形。默认为 True。
        cmap (str, optional): 颜色映射方案。默认为 "Reds"。
        as_outline (bool, optional): 是否以轮廓形式显示颜色层。默认为 False。
        colorbar (bool, optional): 是否显示颜色条。默认为 True。
        colorbar_location (str, optional): 颜色条的位置。默认为 "right"。
        colorbar_label_name (str, optional): 颜色条的标签名称。默认为空字符串。
        colorbar_label_rotation (int, optional): 颜色条标签的旋转角度。默认为 0。
        colorbar_decimals (int, optional): 颜色条刻度的小数位数。默认为 1。
        colorbar_fontsize (int, optional): 颜色条标签的字体大小。默认为 8。
        colorbar_nticks (int, optional): 颜色条上的刻度数量。默认为 2。
        colorbar_shrink (float, optional): 颜色条的缩放比例。默认为 0.15。
        colorbar_aspect (int, optional): 颜色条的宽高比。默认为 8。
        colorbar_draw_border (bool, optional): 是否绘制颜色条边框。默认为 False。
        title_name (str, optional): 图形标题。默认为空字符串。
        title_fontsize (int, optional): 标题字体大小。默认为 15。
        title_y (float, optional): 标题在 y 轴上的位置（范围通常为 0~1）。默认为 0.9。
        rjx_colorbar (bool, optional): 是否使用自定义颜色条。默认为 False。
        rjx_colorbar_direction (str, optional): 自定义颜色条方向，支持 "vertical" 或 "horizontal"。默认为 "vertical"。
        horizontal_center (bool, optional): 水平颜色条是否居中。默认为 True。
        rjx_colorbar_outline (bool, optional): 自定义颜色条是否显示边框。默认为 False。
        rjx_colorbar_label_name (str, optional): 自定义颜色条标签名称。默认为空字符串。
        rjx_colorbar_tick_fontsize (int, optional): 自定义颜色条刻度字体大小。默认为 10。
        rjx_colorbar_label_fontsize (int, optional): 自定义颜色条标签字体大小。默认为 10。
        rjx_colorbar_tick_rotation (int, optional): 自定义颜色条刻度标签旋转角度。默认为 0。
        rjx_colorbar_tick_length (int, optional): 自定义颜色条刻度长度。默认为 0。
        rjx_colorbar_nticks (int, optional): 自定义颜色条上的刻度数量。默认为 2。

    Returns:
        Union[plt.Figure, tuple[np.ndarray, np.ndarray]]: 如果 `plot=True`，返回 matplotlib 的 Figure 对象；
        否则返回左右脑数据数组的元组 `(lh_parc, rh_parc)`。
    """
    # 发出弃用警告
    warnings.warn(
        "plot_human_brain_figure 即将弃用，请使用 plot_brain_surface_figure 替代。未来版本将移除本函数。",
        DeprecationWarning,
        stacklevel=2
    )

    # 设置必要文件路径
    current_dir = op.dirname(__file__)
    neuromaps_data_dir = op.join(current_dir, "data/neurodata")
    if atlas == "glasser":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/human_Glasser/fsaverage.L.Glasser.32k_fs_LR.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/human_Glasser/fsaverage.R.Glasser.32k_fs_LR.label.gii",
        )
        df = pd.read_csv(op.join(current_dir, "data/atlas_tables/human_glasser.csv"))
    elif atlas == "bna":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/human_BNA/fsaverage.L.BNA.32k_fs_LR.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/human_BNA/fsaverage.R.BNA.32k_fs_LR.label.gii",
        )
        df = pd.read_csv(op.join(current_dir, "data/atlas_tables", "human_bna.csv"))
    # 获取文件Underlay
    lh = op.join(
        neuromaps_data_dir,
        f"surfaces/human_fsLR/tpl-fsLR_den-32k_hemi-L_{surf}.surf.gii",
    )
    rh = op.join(
        neuromaps_data_dir,
        f"surfaces/human_fsLR/tpl-fsLR_den-32k_hemi-R_{surf}.surf.gii",
    )
    p = Plot(lh, rh)
    # 将原始数据拆分成左右脑数据
    lh_data, rh_data = {}, {}
    for roi in data:
        if "lh_" in roi:
            lh_data[roi] = data[roi]
        elif "rh_" in roi:
            rh_data[roi] = data[roi]
    # 加载图集分区数据
    lh_roi_list, rh_roi_list = (
        list(df["ROIs_name"])[0 : int(len(df["ROIs_name"]) / 2)],
        list(df["ROIs_name"])[int(len(df["ROIs_name"]) / 2) : len(df["ROIs_name"])],
    )
    # 处理左脑数据
    lh_parc = nib.load(lh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in lh_roi_list}
    for vertex_index, label in enumerate(lh_parc):
        if label - 1 >= 0:
            roi_vertics[lh_roi_list[label - 1]].append(vertex_index)
    lh_parc = np.full(lh_parc.shape, np.nan)
    for roi in lh_data:
        lh_parc[roi_vertics[roi]] = lh_data[roi]
    # 处理右脑数据
    rh_parc = nib.load(rh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in rh_roi_list}
    for vertex_index, label in enumerate(rh_parc):
        if label - 1 - len(lh_roi_list) >= 0:
            roi_vertics[rh_roi_list[label - 1 - len(lh_roi_list)]].append(vertex_index)
    rh_parc = np.full(rh_parc.shape, np.nan)
    for roi in rh_data:
        rh_parc[roi_vertics[roi]] = rh_data[roi]
    # 画图
    if plot:
        # 画图元素参数设置
        if vmin is None:
            vmin = min(data.values())
        if vmax is None:
            vmax = max(data.values())
        if vmin > vmax:
            print("vmin必须小于等于vmax")
            return
        if vmin == vmax:
            vmin = min(0, vmin)
            vmax = max(0, vmax)
        # colorbar参数设置
        colorbar_kws = {
            "location": colorbar_location,
            "label_direction": colorbar_label_rotation,
            "decimals": colorbar_decimals,
            "fontsize": colorbar_fontsize,
            "n_ticks": colorbar_nticks,
            "shrink": colorbar_shrink,
            "aspect": colorbar_aspect,
            "draw_border": colorbar_draw_border,
        }
        p.add_layer(
            {"left": lh_parc, "right": rh_parc},
            cbar=colorbar,
            cmap=cmap,
            color_range=(vmin, vmax),
            cbar_label=colorbar_label_name,
            zero_transparent=False,
            as_outline=as_outline,
        )
        fig = p.build(cbar_kws=colorbar_kws)
        fig.suptitle(title_name, fontsize=title_fontsize, y=title_y)
        ############################################### rjx_colorbar ###############################################
        sm = ScalarMappable(cmap=cmap)
        sm.set_array((vmin, vmax))  # 设置值范围
        if rjx_colorbar:
            if rjx_colorbar_direction == "vertical":
                formatter = ScalarFormatter(useMathText=True)  # 科学计数法相关
                formatter.set_powerlimits(
                    (-3, 3)
                )  # <=-1也就是小于等于0.1，>=2，也就是大于等于100，会写成科学计数法
                cax = fig.add_axes(
                    [1, 0.425, 0.01, 0.15]
                )  # [left, bottom, width, height]
                cbar = fig.colorbar(
                    sm, cax=cax, orientation="vertical", cmap=cmap
                )  # "vertical", "horizontal"
                cbar.outline.set_visible(rjx_colorbar_outline)
                cbar.ax.set_ylabel(
                    rjx_colorbar_label_name, fontsize=rjx_colorbar_label_fontsize
                )
                cbar.ax.yaxis.set_label_position(
                    "left"
                )  # 原本设置y轴label默认在右边，现在换到左边
                cbar.ax.tick_params(
                    axis="y",
                    which="major",
                    labelsize=rjx_colorbar_tick_fontsize,
                    rotation=rjx_colorbar_tick_rotation,
                    length=rjx_colorbar_tick_length,
                )
                cbar.set_ticks(np.linspace(vmin, vmax, rjx_colorbar_nticks))
                if vmax < 0.001 or vmax > 1000:  # y轴设置科学计数法
                    cbar.ax.yaxis.set_major_formatter(formatter)
                    cbar.ax.yaxis.get_offset_text().set_visible(
                        False
                    )  # 隐藏默认的偏移文本
                    exponent = math.floor(math.log10(vmax))
                    # 手动添加文本
                    cbar.ax.text(
                        1.05,
                        1.15,
                        rf"$\times 10^{{{exponent}}}$",
                        transform=cbar.ax.transAxes,
                        fontsize=rjx_colorbar_tick_fontsize,
                        verticalalignment="bottom",
                        horizontalalignment="left",
                    )
            elif rjx_colorbar_direction == "horizontal":
                if horizontal_center:
                    cax = fig.add_axes([0.44, 0.5, 0.15, 0.01])
                else:
                    cax = fig.add_axes([0.44, 0.05, 0.15, 0.01])
                cbar = fig.colorbar(sm, cax=cax, orientation="horizontal", cmap=cmap)
                cbar.outline.set_visible(rjx_colorbar_outline)
                cbar.ax.set_title(
                    rjx_colorbar_label_name, fontsize=rjx_colorbar_label_fontsize
                )
                cbar.ax.tick_params(
                    axis="x",
                    which="major",
                    labelsize=rjx_colorbar_tick_fontsize,
                    rotation=rjx_colorbar_tick_rotation,
                    length=rjx_colorbar_tick_length,
                )
                if vmax < 0.001 or vmax > 1000:  # y轴设置科学计数法
                    cbar.ax.xaxis.set_major_formatter(formatter)
                cbar.set_ticks(np.linspace(vmin, vmax, rjx_colorbar_nticks))
            ########################################### rjx_colorbar ###############################################
        return fig
    return lh_parc, rh_parc


def plot_human_hemi_brain_figure(
    data: dict[str, float],
    hemi: str = "lh",
    surf: str = "veryinflated",
    atlas: str = "glasser",
    vmin: Num | None = None,
    vmax: Num | None = None,
    cmap: str = "Reds",
    colorbar: bool = True,
    colorbar_location: str = "right",
    colorbar_label_name: str = "",
    colorbar_label_rotation: int = 0,
    colorbar_decimals: int = 1,
    colorbar_fontsize: int = 8,
    colorbar_nticks: int = 2,
    colorbar_shrink: float = 0.15,
    colorbar_aspect: int = 8,
    colorbar_draw_border: bool = False,
    title_name: str = "",
    title_fontsize: int = 15,
    title_y: float = 0.9,
) -> plt.Figure | None:
    warnings.warn(
        "plot_human_hemi_brain_figure 即将弃用，请使用 plot_brain_surface_figure 替代。未来版本将移除本函数。",
        DeprecationWarning,
        stacklevel=2
    )
    """
    绘制人类大脑单侧（左脑或右脑）表面图，支持 Glasser 和 BNA 图谱。

    Args:
        data (dict[str, float]): 包含 ROI 名称及其对应值的字典。
        hemi (str, optional): 脑半球选择，支持 "lh"（左脑）或 "rh"（右脑）。默认为 "lh"。
        surf (str, optional): 大脑表面类型（如 "veryinflated", "inflated"）。默认为 "veryinflated"。
        atlas (str, optional): 使用的图谱名称，支持 "glasser" 或 "bna"。默认为 "glasser"。
        vmin (Num, optional): 颜色映射的最小值。可以是整数或浮点数。默认为 None。
        vmax (Num, optional): 颜色映射的最大值。可以是整数或浮点数。默认为 None。
        cmap (str, optional): 颜色映射方案。默认为 "Reds"。
        colorbar (bool, optional): 是否显示颜色条。默认为 True。
        colorbar_location (str, optional): 颜色条的位置。默认为 "right"。
        colorbar_label_name (str, optional): 颜色条的标签名称。默认为空字符串。
        colorbar_label_rotation (int, optional): 颜色条标签的旋转角度。默认为 0。
        colorbar_decimals (int, optional): 颜色条刻度的小数位数。默认为 1。
        colorbar_fontsize (int, optional): 颜色条标签的字体大小。默认为 8。
        colorbar_nticks (int, optional): 颜色条上的刻度数量。默认为 2。
        colorbar_shrink (float, optional): 颜色条的缩放比例。默认为 0.15。
        colorbar_aspect (int, optional): 颜色条的宽高比。默认为 8。
        colorbar_draw_border (bool, optional): 是否绘制颜色条边框。默认为 False。
        title_name (str, optional): 图形标题。默认为空字符串。
        title_fontsize (int, optional): 标题字体大小。默认为 15。
        title_y (float, optional): 标题在 y 轴上的位置（范围通常为 0~1）。默认为 0.9。

    Returns:
        plt.Figure: 返回一个 matplotlib 的 Figure 对象，表示生成的大脑表面图。
    """

    # 设置必要文件路径
    current_dir = op.dirname(__file__)
    neuromaps_data_dir = op.join(current_dir, "data/neurodata")
    if atlas == "glasser":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/human_Glasser/fsaverage.L.Glasser.32k_fs_LR.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/human_Glasser/fsaverage.R.Glasser.32k_fs_LR.label.gii",
        )
        df = pd.read_csv(op.join(current_dir, "data/atlas_tables", "human_glasser.csv"))
    elif atlas == "bna":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/human_BNA/fsaverage.L.BNA.32k_fs_LR.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/human_BNA/fsaverage.R.BNA.32k_fs_LR.label.gii",
        )
        df = pd.read_csv(op.join(current_dir, "data/atlas_tables", "human_bna.csv"))
    # 获取文件Underlay

    lh = op.join(
        neuromaps_data_dir,
        f"surfaces/human_fsLR/tpl-fsLR_den-32k_hemi-L_{surf}.surf.gii",
    )
    rh = op.join(
        neuromaps_data_dir,
        f"surfaces/human_fsLR/tpl-fsLR_den-32k_hemi-R_{surf}.surf.gii",
    )
    if hemi == "lh":
        p = Plot(lh, size=(800, 400), zoom=1.2)
    elif hemi == "rh":
        p = Plot(rh, size=(800, 400), zoom=1.2)
    # 将原始数据拆分成左右脑数据
    lh_data, rh_data = {}, {}
    for roi in data:
        if "lh_" in roi:
            lh_data[roi] = data[roi]
        elif "rh_" in roi:
            rh_data[roi] = data[roi]
    # 加载图集分区数据
    lh_roi_list, rh_roi_list = (
        list(df["ROIs_name"])[0 : int(len(df["ROIs_name"]) / 2)],
        list(df["ROIs_name"])[int(len(df["ROIs_name"]) / 2) : len(df["ROIs_name"])],
    )
    # 处理左脑数据
    lh_parc = nib.load(lh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in lh_roi_list}
    for vertex_index, label in enumerate(lh_parc):
        if label - 1 >= 0:
            roi_vertics[lh_roi_list[label - 1]].append(vertex_index)
    lh_parc = np.full(lh_parc.shape, np.nan)
    for roi in lh_data:
        lh_parc[roi_vertics[roi]] = lh_data[roi]
    # 处理右脑数据
    rh_parc = nib.load(rh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in rh_roi_list}
    for vertex_index, label in enumerate(rh_parc):
        if label - 1 - len(lh_roi_list) >= 0:
            roi_vertics[rh_roi_list[label - 1 - len(lh_roi_list)]].append(vertex_index)
    rh_parc = np.full(rh_parc.shape, np.nan)
    for roi in rh_data:
        rh_parc[roi_vertics[roi]] = rh_data[roi]
    # 画图元素参数设置
    if vmin is None:
        vmin = min(data.values())
    if vmax is None:
        vmax = max(data.values())
    if vmin > vmax:
        print("vmin必须小于等于vmax")
        return
    if vmin == vmax:
        vmin = min(0, vmin)
        vmax = max(0, vmax)
    # colorbar参数设置
    colorbar_kws = {
        "location": colorbar_location,
        "label_direction": colorbar_label_rotation,
        "decimals": colorbar_decimals,
        "fontsize": colorbar_fontsize,
        "n_ticks": colorbar_nticks,
        "shrink": colorbar_shrink,
        "aspect": colorbar_aspect,
        "draw_border": colorbar_draw_border,
    }
    if hemi == "lh":
        p.add_layer(
            {"left": lh_parc},
            cbar=colorbar,
            cmap=cmap,
            color_range=(vmin, vmax),
            cbar_label=colorbar_label_name,
            zero_transparent=False,
        )
    elif hemi == "rh":
        p.add_layer(
            {"left": rh_parc},
            cbar=colorbar,
            cmap=cmap,
            color_range=(vmin, vmax),
            cbar_label=colorbar_label_name,
            zero_transparent=False,
        )  # 很怪，但是这里就是写“{'left': rh_parc}”
    fig = p.build(cbar_kws=colorbar_kws)
    fig.suptitle(title_name, fontsize=title_fontsize, y=title_y)
    return fig


def plot_macaque_brain_figure(
    data: dict[str, float],
    surf: str = "veryinflated",
    atlas: str = "charm5",
    vmin: Num | None = None,
    vmax: Num | None = None,
    plot: bool = True,
    cmap: str = "Reds",
    colorbar: bool = True,
    colorbar_location: str = "right",
    colorbar_label_name: str = "",
    colorbar_label_rotation: int = 0,
    colorbar_decimals: int = 1,
    colorbar_fontsize: int = 8,
    colorbar_nticks: int = 2,
    colorbar_shrink: float = 0.15,
    colorbar_aspect: int = 8,
    colorbar_draw_border: bool = False,
    title_name: str = "",
    title_fontsize: int = 15,
    title_y: float = 0.9,
    rjx_colorbar: bool = False,
    rjx_colorbar_direction: str = "vertical",
    horizontal_center: bool = True,
    rjx_colorbar_outline: bool = False,
    rjx_colorbar_label_name: str = "",
    rjx_colorbar_tick_fontsize: int = 10,
    rjx_colorbar_label_fontsize: int = 10,
    rjx_colorbar_tick_rotation: int = 0,
    rjx_colorbar_tick_length: int = 0,
    rjx_colorbar_nticks: int = 2,
) -> plt.Figure | tuple[np.ndarray, np.ndarray]:
    """
    绘制猕猴大脑表面图，支持多种图谱（CHARM5、CHARM6、BNA、D99）。

    Args:
        data (dict[str, float]): 包含 ROI 名称及其对应值的字典。
        surf (str, optional): 大脑表面类型（如 "veryinflated", "inflated"）。默认为 "veryinflated"。
        atlas (str, optional): 使用的图谱名称，支持 "charm5", "charm6", "bna", "d99"。默认为 "charm5"。
        vmin (Num, optional): 颜色映射的最小值。可以是整数或浮点数。默认为 None。
        vmax (Num, optional): 颜色映射的最大值。可以是整数或浮点数。默认为 None。
        plot (bool, optional): 是否直接绘制图形。默认为 True。
        cmap (str, optional): 颜色映射方案。默认为 "Reds"。
        colorbar (bool, optional): 是否显示颜色条。默认为 True。
        colorbar_location (str, optional): 颜色条的位置。默认为 "right"。
        colorbar_label_name (str, optional): 颜色条的标签名称。默认为空字符串。
        colorbar_label_rotation (int, optional): 颜色条标签的旋转角度。默认为 0。
        colorbar_decimals (int, optional): 颜色条刻度的小数位数。默认为 1。
        colorbar_fontsize (int, optional): 颜色条标签的字体大小。默认为 8。
        colorbar_nticks (int, optional): 颜色条上的刻度数量。默认为 2。
        colorbar_shrink (float, optional): 颜色条的缩放比例。默认为 0.15。
        colorbar_aspect (int, optional): 颜色条的宽高比。默认为 8。
        colorbar_draw_border (bool, optional): 是否绘制颜色条边框。默认为 False。
        title_name (str, optional): 图形标题。默认为空字符串。
        title_fontsize (int, optional): 标题字体大小。默认为 15。
        title_y (float, optional): 标题在 y 轴上的位置（范围通常为 0~1）。默认为 0.9。
        rjx_colorbar (bool, optional): 是否使用自定义颜色条。默认为 False。
        rjx_colorbar_direction (str, optional): 自定义颜色条方向，支持 "vertical" 或 "horizontal"。默认为 "vertical"。
        horizontal_center (bool, optional): 水平颜色条是否居中。默认为 True。
        rjx_colorbar_outline (bool, optional): 自定义颜色条是否显示边框。默认为 False。
        rjx_colorbar_label_name (str, optional): 自定义颜色条标签名称。默认为空字符串。
        rjx_colorbar_tick_fontsize (int, optional): 自定义颜色条刻度字体大小。默认为 10。
        rjx_colorbar_label_fontsize (int, optional): 自定义颜色条标签字体大小。默认为 10。
        rjx_colorbar_tick_rotation (int, optional): 自定义颜色条刻度标签旋转角度。默认为 0。
        rjx_colorbar_tick_length (int, optional): 自定义颜色条刻度长度。默认为 0。
        rjx_colorbar_nticks (int, optional): 自定义颜色条上的刻度数量。默认为 2。

    Returns:
        Union[plt.Figure, tuple[np.ndarray, np.ndarray]]: 如果 `plot=True`，返回 matplotlib 的 Figure 对象；
        否则返回左右脑数据数组的元组 `(lh_parc, rh_parc)`。
    """
    # 设置必要文件路径
    current_dir = op.dirname(__file__)
    neuromaps_data_dir = op.join(current_dir, "data/neurodata")
    if atlas == "charm5":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_CHARM5/L.charm5.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_CHARM5/R.charm5.label.gii",
        )
        df = pd.read_csv(
            op.join(current_dir, "data/atlas_tables", "macaque_charm5.csv")
        )
    elif atlas == "charm6":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_CHARM6/L.charm6.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_CHARM6/R.charm6.label.gii",
        )
        df = pd.read_csv(
            op.join(current_dir, "data/atlas_tables", "macaque_charm6.csv")
        )
    elif atlas == "bna":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_BNA/L.charm5.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_BNA/R.charm5.label.gii",
        )
        df = pd.read_csv(op.join(current_dir, "data/atlas_tables", "macaque_bna.csv"))
    elif atlas == "d99":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_D99/L.d99.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_D99/R.d99.label.gii",
        )
        df = pd.read_csv(op.join(current_dir, "data/atlas_tables", "macaque_d99.csv"))
    # 获取文件Underlay
    lh = op.join(
        neuromaps_data_dir, f"surfaces/macaque_BNA/civm.L.{surf}.32k_fs_LR.surf.gii"
    )
    rh = op.join(
        neuromaps_data_dir, f"surfaces/macaque_BNA/civm.R.{surf}.32k_fs_LR.surf.gii"
    )
    p = Plot(lh, rh)
    # 将原始数据拆分成左右脑数据
    lh_data, rh_data = {}, {}
    for roi in data:
        if "lh_" in roi:
            lh_data[roi] = data[roi]
        elif "rh_" in roi:
            rh_data[roi] = data[roi]
    # 加载图集分区数据
    lh_roi_list, rh_roi_list = (
        list(df["ROIs_name"])[0 : int(len(df["ROIs_name"]) / 2)],
        list(df["ROIs_name"])[int(len(df["ROIs_name"]) / 2) : len(df["ROIs_name"])],
    )
    # 处理左脑数据
    lh_parc = nib.load(lh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in lh_roi_list}
    for vertex_index, label in enumerate(lh_parc):
        if label - 1 >= 0:
            roi_vertics[lh_roi_list[label - 1]].append(vertex_index)
    lh_parc = np.full(lh_parc.shape, np.nan)
    for roi in lh_data:
        lh_parc[roi_vertics[roi]] = lh_data[roi]
    # 处理右脑数据
    rh_parc = nib.load(rh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in rh_roi_list}
    for vertex_index, label in enumerate(rh_parc):
        if label - 1 - len(lh_roi_list) >= 0:
            roi_vertics[rh_roi_list[label - 1 - len(lh_roi_list)]].append(vertex_index)
    rh_parc = np.full(rh_parc.shape, np.nan)
    for roi in rh_data:
        rh_parc[roi_vertics[roi]] = rh_data[roi]
    # 画图
    if plot:
        # 画图元素参数设置
        if vmin is None:
            vmin = min(data.values())
        if vmax is None:
            vmax = max(data.values())
        if vmin > vmax:
            print("vmin必须小于等于vmax")
            return
        if vmin == vmax:
            vmin = min(0, vmin)
            vmax = max(0, vmax)
        # colorbar参数设置
        colorbar_kws = {
            "location": colorbar_location,
            "label_direction": colorbar_label_rotation,
            "decimals": colorbar_decimals,
            "fontsize": colorbar_fontsize,
            "n_ticks": colorbar_nticks,
            "shrink": colorbar_shrink,
            "aspect": colorbar_aspect,
            "draw_border": colorbar_draw_border,
        }
        p.add_layer(
            {"left": lh_parc, "right": rh_parc},
            cbar=colorbar,
            cmap=cmap,
            color_range=(vmin, vmax),
            cbar_label=colorbar_label_name,
            zero_transparent=False,
        )
        fig = p.build(cbar_kws=colorbar_kws)
        fig.suptitle(title_name, fontsize=title_fontsize, y=title_y)
        ############################################### rjx_colorbar ###############################################
        sm = ScalarMappable(cmap=cmap)
        sm.set_array((vmin, vmax))  # 设置值范围
        if rjx_colorbar:
            formatter = ScalarFormatter(useMathText=True)  # 科学计数法相关
            formatter.set_powerlimits(
                (-3, 3)
            )  # <=-1也就是小于等于0.1，>=2，也就是大于等于100，会写成科学计数法
            if rjx_colorbar_direction == "vertical":
                cax = fig.add_axes(
                    [1, 0.425, 0.01, 0.15]
                )  # [left, bottom, width, height]
                cbar = fig.colorbar(
                    sm, cax=cax, orientation="vertical", cmap=cmap
                )  # "vertical", "horizontal"
                cbar.outline.set_visible(rjx_colorbar_outline)
                cbar.ax.set_ylabel(
                    rjx_colorbar_label_name, fontsize=rjx_colorbar_label_fontsize
                )
                cbar.ax.yaxis.set_label_position(
                    "left"
                )  # 原本设置y轴label默认在右边，现在换到左边
                cbar.ax.tick_params(
                    axis="y",
                    which="major",
                    labelsize=rjx_colorbar_tick_fontsize,
                    rotation=rjx_colorbar_tick_rotation,
                    length=rjx_colorbar_tick_length,
                )
                cbar.set_ticks(np.linspace(vmin, vmax, rjx_colorbar_nticks))
                if vmax < 0.001 or vmax > 1000:  # y轴设置科学计数法
                    cbar.ax.yaxis.set_major_formatter(formatter)
                    cbar.ax.yaxis.get_offset_text().set_visible(
                        False
                    )  # 隐藏默认的偏移文本
                    exponent = math.floor(math.log10(vmax))
                    # 手动添加文本
                    cbar.ax.text(
                        1.05,
                        1.15,
                        rf"$\times 10^{{{exponent}}}$",
                        transform=cbar.ax.transAxes,
                        fontsize=rjx_colorbar_tick_fontsize,
                        verticalalignment="bottom",
                        horizontalalignment="left",
                    )
            elif rjx_colorbar_direction == "horizontal":
                if horizontal_center:
                    cax = fig.add_axes([0.44, 0.5, 0.15, 0.01])
                else:
                    cax = fig.add_axes([0.44, 0.05, 0.15, 0.01])
                cbar = fig.colorbar(sm, cax=cax, orientation="horizontal", cmap=cmap)
                cbar.outline.set_visible(rjx_colorbar_outline)
                cbar.ax.set_title(
                    rjx_colorbar_label_name, fontsize=rjx_colorbar_label_fontsize
                )
                cbar.ax.tick_params(
                    axis="x",
                    which="major",
                    labelsize=rjx_colorbar_tick_fontsize,
                    rotation=rjx_colorbar_tick_rotation,
                    length=rjx_colorbar_tick_length,
                )
                if vmax < 0.001 or vmax > 1000:  # y轴设置科学计数法
                    cbar.ax.xaxis.set_major_formatter(formatter)
            cbar.set_ticks([vmin, vmax])
            ########################################### rjx_colorbar ###############################################
        return fig
    return lh_parc, rh_parc


def plot_macaque_hemi_brain_figure(
    data: dict[str, float],
    hemi: str = "lh",
    surf: str = "veryinflated",
    atlas: str = "charm5",
    vmin: Num | None = None,
    vmax: Num | None = None,
    cmap: str = "Reds",
    colorbar: bool = True,
    colorbar_location: str = "right",
    colorbar_label_name: str = "",
    colorbar_label_rotation: int = 0,
    colorbar_decimals: int = 1,
    colorbar_fontsize: int = 8,
    colorbar_nticks: int = 2,
    colorbar_shrink: float = 0.15,
    colorbar_aspect: int = 8,
    colorbar_draw_border: bool = False,
    title_name: str = "",
    title_fontsize: int = 15,
    title_y: float = 0.9,
) -> plt.Figure | None:
    warnings.warn(
        "plot_macaque_hemi_brain_figure 即将弃用，请使用 plot_brain_surface_figure 替代。未来版本将移除本函数。",
        DeprecationWarning,
        stacklevel=2
    )
    """
    绘制猕猴大脑单侧（左脑或右脑）表面图，支持多种图谱（CHARM5、CHARM6、BNA、D99）。

    Args:
        data (dict[str, float]): 包含 ROI 名称及其对应值的字典。
        hemi (str, optional): 脑半球选择，支持 "lh"（左脑）或 "rh"（右脑）。默认为 "lh"。
        surf (str, optional): 大脑表面类型（如 "veryinflated", "inflated"）。默认为 "veryinflated"。
        atlas (str, optional): 使用的图谱名称，支持 "charm5", "charm6", "bna", "d99"。默认为 "charm5"。
        vmin (Num, optional): 颜色映射的最小值。可以是整数或浮点数。默认为 None。
        vmax (Num, optional): 颜色映射的最大值。可以是整数或浮点数。默认为 None。
        cmap (str, optional): 颜色映射方案。默认为 "Reds"。
        colorbar (bool, optional): 是否显示颜色条。默认为 True。
        colorbar_location (str, optional): 颜色条的位置。默认为 "right"。
        colorbar_label_name (str, optional): 颜色条的标签名称。默认为空字符串。
        colorbar_label_rotation (int, optional): 颜色条标签的旋转角度。默认为 0。
        colorbar_decimals (int, optional): 颜色条刻度的小数位数。默认为 1。
        colorbar_fontsize (int, optional): 颜色条标签的字体大小。默认为 8。
        colorbar_nticks (int, optional): 颜色条上的刻度数量。默认为 2。
        colorbar_shrink (float, optional): 颜色条的缩放比例。默认为 0.15。
        colorbar_aspect (int, optional): 颜色条的宽高比。默认为 8。
        colorbar_draw_border (bool, optional): 是否绘制颜色条边框。默认为 False。
        title_name (str, optional): 图形标题。默认为空字符串。
        title_fontsize (int, optional): 标题字体大小。默认为 15。
        title_y (float, optional): 标题在 y 轴上的位置（范围通常为 0~1）。默认为 0.9。

    Returns:
        plt.Figure: 返回一个 matplotlib 的 Figure 对象，表示生成的大脑表面图。
    """

    # 设置必要文件路径
    current_dir = op.dirname(__file__)
    neuromaps_data_dir = op.join(current_dir, "data/neurodata")
    if atlas == "charm5":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_CHARM5/L.charm5.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_CHARM5/R.charm5.label.gii",
        )
        df = pd.read_csv(
            op.join(current_dir, "data/atlas_tables", "macaque_charm5.csv")
        )
    elif atlas == "charm6":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_CHARM6/L.charm6.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_CHARM6/R.charm6.label.gii",
        )
        df = pd.read_csv(
            op.join(current_dir, "data/atlas_tables", "macaque_charm6.csv")
        )
    elif atlas == "bna":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_BNA/L.charm5.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_BNA/R.charm5.label.gii",
        )
        df = pd.read_csv(op.join(current_dir, "data/atlas_tables", "macaque_bna.csv"))
    elif atlas == "d99":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_D99/L.d99.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/macaque_D99/R.d99.label.gii",
        )
        df = pd.read_csv(op.join(current_dir, "data/atlas_tables", "macaque_d99.csv"))
    # 获取文件Underlay
    lh = op.join(
        neuromaps_data_dir, f"surfaces/macaque_BNA/civm.L.{surf}.32k_fs_LR.surf.gii"
    )
    rh = op.join(
        neuromaps_data_dir, f"surfaces/macaque_BNA/civm.R.{surf}.32k_fs_LR.surf.gii"
    )
    if hemi == "lh":
        p = Plot(lh, size=(800, 400), zoom=1.2)
    elif hemi == "rh":
        p = Plot(rh, size=(800, 400), zoom=1.2)
    # 将原始数据拆分成左右脑数据
    lh_data, rh_data = {}, {}
    for roi in data:
        if "lh_" in roi:
            lh_data[roi] = data[roi]
        elif "rh_" in roi:
            rh_data[roi] = data[roi]
    # 加载分区数据
    lh_roi_list, rh_roi_list = (
        list(df["ROIs_name"])[0 : int(len(df["ROIs_name"]) / 2)],
        list(df["ROIs_name"])[int(len(df["ROIs_name"]) / 2) : len(df["ROIs_name"])],
    )
    # 处理左脑数据
    lh_parc = nib.load(lh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in lh_roi_list}
    for vertex_index, label in enumerate(lh_parc):
        if label - 1 >= 0:
            roi_vertics[lh_roi_list[label - 1]].append(vertex_index)
    lh_parc = np.full(lh_parc.shape, np.nan)
    for roi in lh_data:
        lh_parc[roi_vertics[roi]] = lh_data[roi]
    # 处理右脑数据
    rh_parc = nib.load(rh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in rh_roi_list}
    for vertex_index, label in enumerate(rh_parc):
        if label - len(lh_roi_list) - 1 >= 0:
            roi_vertics[rh_roi_list[label - len(lh_roi_list) - 1]].append(vertex_index)
    rh_parc = np.full(rh_parc.shape, np.nan)
    for roi in rh_data:
        rh_parc[roi_vertics[roi]] = rh_data[roi]
    # 画图元素参数设置
    if vmin is None:
        vmin = min(data.values())
    if vmax is None:
        vmax = max(data.values())
    if vmin > vmax:
        print("vmin必须小于等于vmax")
        return
    if vmin == vmax:
        vmin = min(0, vmin)
        vmax = max(0, vmax)
    # colorbar参数设置
    colorbar_kws = {
        "location": colorbar_location,
        "label_direction": colorbar_label_rotation,
        "decimals": colorbar_decimals,
        "fontsize": colorbar_fontsize,
        "n_ticks": colorbar_nticks,
        "shrink": colorbar_shrink,
        "aspect": colorbar_aspect,
        "draw_border": colorbar_draw_border,
    }
    if hemi == "lh":
        p.add_layer(
            {"left": lh_parc},
            cbar=colorbar,
            cmap=cmap,
            color_range=(vmin, vmax),
            cbar_label=colorbar_label_name,
            zero_transparent=False,
        )
    else:
        p.add_layer(
            {"left": rh_parc},
            cbar=colorbar,
            cmap=cmap,
            color_range=(vmin, vmax),
            cbar_label=colorbar_label_name,
            zero_transparent=False,
        )  # 很怪，但是这里就是写“{'left': rh_parc}”
    fig = p.build(cbar_kws=colorbar_kws)
    fig.suptitle(title_name, fontsize=title_fontsize, y=title_y)
    return fig


def plot_chimpanzee_brain_figure(
    data: dict[str, float],
    surf: str = "veryinflated",
    atlas: str = "bna",
    vmin: Num | None = None,
    vmax: Num | None = None,
    plot: bool = True,
    cmap: str = "Reds",
    colorbar: bool = True,
    colorbar_location: str = "right",
    colorbar_label_name: str = "",
    colorbar_label_rotation: int = 0,
    colorbar_decimals: int = 1,
    colorbar_fontsize: int = 8,
    colorbar_nticks: int = 2,
    colorbar_shrink: float = 0.15,
    colorbar_aspect: int = 8,
    colorbar_draw_border: bool = False,
    title_name: str = "",
    title_fontsize: int = 15,
    title_y: float = 0.9,
    rjx_colorbar: bool = False,
    rjx_colorbar_direction: str = "vertical",
    horizontal_center: bool = True,
    rjx_colorbar_outline: bool = False,
    rjx_colorbar_label_name: str = "",
    rjx_colorbar_tick_fontsize: int = 10,
    rjx_colorbar_label_fontsize: int = 10,
    rjx_colorbar_tick_rotation: int = 0,
    rjx_colorbar_tick_length: int = 0,
    rjx_colorbar_nticks: int = 2,
) -> plt.Figure | tuple[np.ndarray, np.ndarray]:
    warnings.warn(
        "plot_chimpanzee_brain_figure 即将弃用，请使用 plot_brain_surface_figure 替代。未来版本将移除本函数。",
        DeprecationWarning,
        stacklevel=2
    )
    """
    绘制黑猩猩大脑表面图，支持 BNA 图谱。

    Args:
        data (dict[str, float]): 包含 ROI 名称及其对应值的字典。
        surf (str, optional): 大脑表面类型（如 "veryinflated", "midthickness"）。默认为 "veryinflated"。
        atlas (str, optional): 使用的图谱名称，目前仅支持 "bna"。默认为 "bna"。
        vmin (Num, optional): 颜色映射的最小值。可以是整数或浮点数。默认为 None。
        vmax (Num, optional): 颜色映射的最大值。可以是整数或浮点数。默认为 None。
        plot (bool, optional): 是否直接绘制图形。默认为 True。
        cmap (str, optional): 颜色映射方案。默认为 "Reds"。
        colorbar (bool, optional): 是否显示颜色条。默认为 True。
        colorbar_location (str, optional): 颜色条的位置。默认为 "right"。
        colorbar_label_name (str, optional): 颜色条的标签名称。默认为空字符串。
        colorbar_label_rotation (int, optional): 颜色条标签的旋转角度。默认为 0。
        colorbar_decimals (int, optional): 颜色条刻度的小数位数。默认为 1。
        colorbar_fontsize (int, optional): 颜色条标签的字体大小。默认为 8。
        colorbar_nticks (int, optional): 颜色条上的刻度数量。默认为 2。
        colorbar_shrink (float, optional): 颜色条的缩放比例。默认为 0.15。
        colorbar_aspect (int, optional): 颜色条的宽高比。默认为 8。
        colorbar_draw_border (bool, optional): 是否绘制颜色条边框。默认为 False。
        title_name (str, optional): 图形标题。默认为空字符串。
        title_fontsize (int, optional): 标题字体大小。默认为 15。
        title_y (float, optional): 标题在 y 轴上的位置（范围通常为 0~1）。默认为 0.9。
        rjx_colorbar (bool, optional): 是否使用自定义颜色条。默认为 False。
        rjx_colorbar_direction (str, optional): 自定义颜色条方向，支持 "vertical" 或 "horizontal"。默认为 "vertical"。
        horizontal_center (bool, optional): 水平颜色条是否居中。默认为 True。
        rjx_colorbar_outline (bool, optional): 自定义颜色条是否显示边框。默认为 False。
        rjx_colorbar_label_name (str, optional): 自定义颜色条标签名称。默认为空字符串。
        rjx_colorbar_tick_fontsize (int, optional): 自定义颜色条刻度字体大小。默认为 10。
        rjx_colorbar_label_fontsize (int, optional): 自定义颜色条标签字体大小。默认为 10。
        rjx_colorbar_tick_rotation (int, optional): 自定义颜色条刻度标签旋转角度。默认为 0。
        rjx_colorbar_tick_length (int, optional): 自定义颜色条刻度长度。默认为 0。
        rjx_colorbar_nticks (int, optional): 自定义颜色条上的刻度数量。默认为 2。

    Returns:
        Union[plt.Figure, tuple[np.ndarray, np.ndarray]]: 如果 `plot=True`，返回 matplotlib 的 Figure 对象；
        否则返回左右脑数据数组的元组 `(lh_parc, rh_parc)`。
    """

    # 设置必要文件路径
    current_dir = op.dirname(__file__)
    neuromaps_data_dir = op.join(current_dir, "data/neurodata")
    if atlas == "bna":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/chimpanzee_BNA/ChimpBNA.L.32k_fs_LR.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/chimpanzee_BNA/ChimpBNA.R.32k_fs_LR.label.gii",
        )
        df = pd.read_csv(
            op.join(current_dir, "data/atlas_tables", "chimpanzee_bna.csv")
        )
    # 获取文件Underlay
    lh = op.join(
        neuromaps_data_dir,
        f"surfaces/chimpanzee_BNA/ChimpYerkes29_v1.2.L.{surf}.32k_fs_LR.surf.gii",
    )
    rh = op.join(
        neuromaps_data_dir,
        f"surfaces/chimpanzee_BNA/ChimpYerkes29_v1.2.R.{surf}.32k_fs_LR.surf.gii",
    )
    p = Plot(lh, rh)
    # 将原始数据拆分成左右脑数据
    lh_data, rh_data = {}, {}
    for roi in data:
        if "lh_" in roi:
            lh_data[roi] = data[roi]
        elif "rh_" in roi:
            rh_data[roi] = data[roi]
    # 加载图集分区数据
    lh_roi_list, rh_roi_list = (
        list(df["ROIs_name"])[0 : int(len(df["ROIs_name"]) / 2)],
        list(df["ROIs_name"])[int(len(df["ROIs_name"]) / 2) : len(df["ROIs_name"])],
    )
    # 处理左脑数据
    lh_parc = nib.load(lh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in lh_roi_list}
    for vertex_index, label in enumerate(lh_parc):
        if label - 1 >= 0:
            roi_vertics[lh_roi_list[label - 1]].append(vertex_index)
    lh_parc = np.full(lh_parc.shape, np.nan)
    for roi in lh_data:
        lh_parc[roi_vertics[roi]] = lh_data[roi]
    # 处理右脑数据
    rh_parc = nib.load(rh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in rh_roi_list}
    for vertex_index, label in enumerate(rh_parc):
        if label - 1 - len(lh_roi_list) >= 0:
            roi_vertics[rh_roi_list[label - 1 - len(lh_roi_list)]].append(vertex_index)
    rh_parc = np.full(rh_parc.shape, np.nan)
    for roi in rh_data:
        rh_parc[roi_vertics[roi]] = rh_data[roi]
    # 画图
    if plot:
        # 画图元素参数设置
        if vmin is None:
            vmin = min(data.values())
        if vmax is None:
            vmax = max(data.values())
        if vmin > vmax:
            print("vmin必须小于等于vmax")
            return
        if vmin == vmax:
            vmin = min(0, vmin)
            vmax = max(0, vmax)
        # colorbar参数设置
        colorbar_kws = {
            "location": colorbar_location,
            "label_direction": colorbar_label_rotation,
            "decimals": colorbar_decimals,
            "fontsize": colorbar_fontsize,
            "n_ticks": colorbar_nticks,
            "shrink": colorbar_shrink,
            "aspect": colorbar_aspect,
            "draw_border": colorbar_draw_border,
        }
        p.add_layer(
            {"left": lh_parc, "right": rh_parc},
            cbar=colorbar,
            cmap=cmap,
            color_range=(vmin, vmax),
            cbar_label=colorbar_label_name,
            zero_transparent=False,
        )
        fig = p.build(cbar_kws=colorbar_kws)
        fig.suptitle(title_name, fontsize=title_fontsize, y=title_y)
        ############################################### rjx_colorbar ###############################################
        sm = ScalarMappable(cmap=cmap)
        sm.set_array((vmin, vmax))  # 设置值范围
        if rjx_colorbar:
            formatter = ScalarFormatter(useMathText=True)  # 科学计数法相关
            formatter.set_powerlimits(
                (-3, 3)
            )  # <=-1也就是小于等于0.1，>=2，也就是大于等于100，会写成科学计数法
            if rjx_colorbar_direction == "vertical":
                cax = fig.add_axes(
                    [1, 0.425, 0.01, 0.15]
                )  # [left, bottom, width, height]
                cbar = fig.colorbar(
                    sm, cax=cax, orientation="vertical", cmap=cmap
                )  # "vertical", "horizontal"
                cbar.outline.set_visible(rjx_colorbar_outline)
                cbar.ax.set_ylabel(
                    rjx_colorbar_label_name, fontsize=rjx_colorbar_label_fontsize
                )
                cbar.ax.yaxis.set_label_position(
                    "left"
                )  # 原本设置y轴label默认在右边，现在换到左边
                cbar.ax.tick_params(
                    axis="y",
                    which="major",
                    labelsize=rjx_colorbar_tick_fontsize,
                    rotation=rjx_colorbar_tick_rotation,
                    length=rjx_colorbar_tick_length,
                )
                cbar.set_ticks(np.linspace(vmin, vmax, rjx_colorbar_nticks))
                if vmax < 0.001 or vmax > 1000:  # y轴设置科学计数法
                    cbar.ax.yaxis.set_major_formatter(formatter)
                    cbar.ax.yaxis.get_offset_text().set_visible(
                        False
                    )  # 隐藏默认的偏移文本
                    exponent = math.floor(math.log10(vmax))
                    # 手动添加文本
                    cbar.ax.text(
                        1.05,
                        1.15,
                        rf"$\times 10^{{{exponent}}}$",
                        transform=cbar.ax.transAxes,
                        fontsize=rjx_colorbar_tick_fontsize,
                        verticalalignment="bottom",
                        horizontalalignment="left",
                    )
            elif rjx_colorbar_direction == "horizontal":
                if horizontal_center:
                    cax = fig.add_axes([0.44, 0.5, 0.15, 0.01])
                else:
                    cax = fig.add_axes([0.44, 0.05, 0.15, 0.01])
                cbar = fig.colorbar(sm, cax=cax, orientation="horizontal", cmap=cmap)
                cbar.outline.set_visible(rjx_colorbar_outline)
                cbar.ax.set_title(
                    rjx_colorbar_label_name, fontsize=rjx_colorbar_label_fontsize
                )
                cbar.ax.tick_params(
                    axis="x",
                    which="major",
                    labelsize=rjx_colorbar_tick_fontsize,
                    rotation=rjx_colorbar_tick_rotation,
                    length=rjx_colorbar_tick_length,
                )
                if vmax < 0.001 or vmax > 1000:  # y轴设置科学计数法
                    cbar.ax.xaxis.set_major_formatter(formatter)
            cbar.set_ticks([vmin, vmax])
            ########################################### rjx_colorbar ###############################################
        return fig
    return lh_parc, rh_parc


def plot_chimpanzee_hemi_brain_figure(
    data: dict[str, float],
    hemi: str = "lh",
    surf: str = "veryinflated",
    atlas: str = "bna",
    vmin: Num | None = None,
    vmax: Num | None = None,
    cmap: str = "Reds",
    colorbar: bool = True,
    colorbar_location: str = "right",
    colorbar_label_name: str = "",
    colorbar_label_rotation: int = 0,
    colorbar_decimals: int = 1,
    colorbar_fontsize: int = 8,
    colorbar_nticks: int = 2,
    colorbar_shrink: float = 0.15,
    colorbar_aspect: int = 8,
    colorbar_draw_border: bool = False,
    title_name: str = "",
    title_fontsize: int = 15,
    title_y: float = 0.9,
) -> plt.Figure:
    warnings.warn(
        "plot_chimpanzee_hemi_brain_figure 即将弃用，请使用 plot_brain_surface_figure 替代。未来版本将移除本函数。",
        DeprecationWarning,
        stacklevel=2
    )
    """
    绘制黑猩猩大脑单侧（左脑或右脑）表面图，支持 BNA 图谱。

    Args:
        data (dict[str, float]): 包含 ROI 名称及其对应值的字典。
        hemi (str, optional): 脑半球选择，支持 "lh"（左脑）或 "rh"（右脑）。默认为 "lh"。
        surf (str, optional): 大脑表面类型（如 "veryinflated", "midthickness"）。默认为 "veryinflated"。
        atlas (str, optional): 使用的图谱名称，目前仅支持 "bna"。默认为 "bna"。
        vmin (Num, optional): 颜色映射的最小值。可以是整数或浮点数。默认为 None。
        vmax (Num, optional): 颜色映射的最大值。可以是整数或浮点数。默认为 None。
        cmap (str, optional): 颜色映射方案。默认为 "Reds"。
        colorbar (bool, optional): 是否显示颜色条。默认为 True。
        colorbar_location (str, optional): 颜色条的位置。默认为 "right"。
        colorbar_label_name (str, optional): 颜色条的标签名称。默认为空字符串。
        colorbar_label_rotation (int, optional): 颜色条标签的旋转角度。默认为 0。
        colorbar_decimals (int, optional): 颜色条刻度的小数位数。默认为 1。
        colorbar_fontsize (int, optional): 颜色条标签的字体大小。默认为 8。
        colorbar_nticks (int, optional): 颜色条上的刻度数量。默认为 2。
        colorbar_shrink (float, optional): 颜色条的缩放比例。默认为 0.15。
        colorbar_aspect (int, optional): 颜色条的宽高比。默认为 8。
        colorbar_draw_border (bool, optional): 是否绘制颜色条边框。默认为 False。
        title_name (str, optional): 图形标题。默认为空字符串。
        title_fontsize (int, optional): 标题字体大小。默认为 15。
        title_y (float, optional): 标题在 y 轴上的位置（范围通常为 0~1）。默认为 0.9。

    Returns:
        plt.Figure: 返回一个 matplotlib 的 Figure 对象，表示生成的大脑表面图。
    """
    # 设置必要文件路径
    current_dir = op.dirname(__file__)
    neuromaps_data_dir = op.join(current_dir, "data/neurodata")
    if atlas == "bna":
        lh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/chimpanzee_BNA/ChimpBNA.L.32k_fs_LR.label.gii",
        )
        rh_atlas_dir = op.join(
            neuromaps_data_dir,
            "atlases/chimpanzee_BNA/ChimpBNA.R.32k_fs_LR.label.gii",
        )
        df = pd.read_csv(
            op.join(current_dir, "data/atlas_tables", "chimpanzee_bna.csv")
        )
    # 获取文件Underlay
    lh = op.join(
        neuromaps_data_dir,
        f"surfaces/chimpanzee_BNA/ChimpYerkes29_v1.2.L.{surf}.32k_fs_LR.surf.gii",
    )
    rh = op.join(
        neuromaps_data_dir,
        f"surfaces/chimpanzee_BNA/ChimpYerkes29_v1.2.R.{surf}.32k_fs_LR.surf.gii",
    )
    if hemi == "lh":
        p = Plot(lh, size=(800, 400), zoom=1.2)
    elif hemi == "rh":
        p = Plot(rh, size=(800, 400), zoom=1.2)
    # 将原始数据拆分成左右脑数据
    lh_data, rh_data = {}, {}
    for roi in data:
        if "lh_" in roi:
            lh_data[roi] = data[roi]
        elif "rh_" in roi:
            rh_data[roi] = data[roi]
    # 加载分区数据
    lh_roi_list, rh_roi_list = (
        list(df["ROIs_name"])[0 : int(len(df["ROIs_name"]) / 2)],
        list(df["ROIs_name"])[int(len(df["ROIs_name"]) / 2) : len(df["ROIs_name"])],
    )
    # 处理左脑数据
    lh_parc = nib.load(lh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in lh_roi_list}
    for vertex_index, label in enumerate(lh_parc):
        if label - 1 >= 0:
            roi_vertics[lh_roi_list[label - 1]].append(vertex_index)
    lh_parc = np.full(lh_parc.shape, np.nan)
    for roi in lh_data:
        lh_parc[roi_vertics[roi]] = lh_data[roi]
    # 处理右脑数据
    rh_parc = nib.load(rh_atlas_dir).darrays[0].data
    roi_vertics = {roi: [] for roi in rh_roi_list}
    for vertex_index, label in enumerate(rh_parc):
        if label - len(lh_roi_list) - 1 >= 0:
            roi_vertics[rh_roi_list[label - len(lh_roi_list) - 1]].append(vertex_index)
    rh_parc = np.full(rh_parc.shape, np.nan)
    for roi in rh_data:
        rh_parc[roi_vertics[roi]] = rh_data[roi]
    # 画图元素参数设置
    if vmin is None:
        vmin = min(data.values())
    if vmax is None:
        vmax = max(data.values())
    if vmin > vmax:
        print("vmin必须小于等于vmax")
        return
    if vmin == vmax:
        vmin = min(0, vmin)
        vmax = max(0, vmax)
    # colorbar参数设置
    colorbar_kws = {
        "location": colorbar_location,
        "label_direction": colorbar_label_rotation,
        "decimals": colorbar_decimals,
        "fontsize": colorbar_fontsize,
        "n_ticks": colorbar_nticks,
        "shrink": colorbar_shrink,
        "aspect": colorbar_aspect,
        "draw_border": colorbar_draw_border,
    }
    if hemi == "lh":
        p.add_layer(
            {"left": lh_parc},
            cbar=colorbar,
            cmap=cmap,
            color_range=(vmin, vmax),
            cbar_label=colorbar_label_name,
            zero_transparent=False,
        )
    else:
        p.add_layer(
            {"left": rh_parc},
            cbar=colorbar,
            cmap=cmap,
            color_range=(vmin, vmax),
            cbar_label=colorbar_label_name,
            zero_transparent=False,
        )  # 很怪，但是这里就是写“{'left': rh_parc}”
    fig = p.build(cbar_kws=colorbar_kws)
    fig.suptitle(title_name, fontsize=title_fontsize, y=title_y)
    return fig
