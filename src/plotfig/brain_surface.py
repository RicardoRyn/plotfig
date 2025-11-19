from pathlib import Path
from typing import TypeAlias
from collections.abc import Mapping

import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from surfplot import Plot

# 类型别名定义
Num: TypeAlias = float | int

__all__ = [
    "plot_brain_surface_figure",
]

# 路径常量
NEURODATA = Path(__file__).resolve().parent / "data" / "neurodata"


def _map_labels_to_values(data, gifti_file):
    gifti = nib.load(gifti_file)
    # 获取顶点标签编号数组，shape=(顶点数,)
    labels = gifti.darrays[0].data  
    # 构建标签编号到脑区名称的映射字典
    key_to_label = {label.key: label.label for label in gifti.labeltable.labels}
    # 检查数据中是否有在图集中找不到的脑区标签
    missing_labels = list(set(data.keys()) - set(key_to_label.values()))
    if missing_labels:
        raise ValueError(
            f"以下脑区标签在指定图集中未找到，请检查名称是否正确: {missing_labels}"
        )

    # 准备输出数组，初始化为NaN
    parc = np.full(labels.shape, np.nan, dtype=float)
    # 遍历所有标签，将数据映射到对应的顶点
    for key, label_name in key_to_label.items():
        if label_name in data:
            parc[labels == key] = data[label_name]
    return parc


def plot_brain_surface_figure(
    data: Mapping[str, Num],
    species: str = "human",
    atlas: str = "glasser",
    surf: str = "veryinflated",
    ax: Axes | None = None,
    vmin: Num | None = None,
    vmax: Num | None = None,
    cmap: str = "viridis",
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
    title_fontsize: int = 12,
    as_outline: bool = False,
) -> Axes: 
    """在大脑皮层表面绘制数值数据的函数。

    Args:
        data (dict[str, float]): 包含脑区名称和对应数值的字典，键为脑区名称（如"lh_bankssts"），值为数值
        species (str, optional): 物种名称，支持"human"、"chimpanzee"、"macaque". Defaults to "human".
        atlas (str, optional): 脑图集名称，根据物种不同可选不同图集。人上包括"glasser"、"bna"，黑猩猩上包括"bna"，猕猴上包括"charm5"、"charm6"、"bna"以及"d99". Defaults to "glasser".
        surf (str, optional): 大脑皮层表面类型，如"inflated"、"veryinflated"、"midthickness"等. Defaults to "veryinflated".
        ax (Axes | None, optional): matplotlib的坐标轴对象，如果为None则使用当前坐标轴. Defaults to None.
        vmin (Num | None, optional): 颜色映射的最小值，None表示使用数据中的最小值. Defaults to None.
        vmax (Num | None, optional): 颜色映射的最大值，None表示使用数据中的最大值. Defaults to None.
        cmap (str, optional): 颜色映射方案，如"viridis"、"Blues"、"Reds"等. Defaults to "viridis".
        colorbar (bool, optional): 是否显示颜色条. Defaults to True.
        colorbar_location (str, optional): 颜色条位置，可选"left"、"right"、"top"、"bottom". Defaults to "right".
        colorbar_label_name (str, optional): 颜色条标签名称. Defaults to "".
        colorbar_label_rotation (int, optional): 颜色条标签旋转角度. Defaults to 0.
        colorbar_decimals (int, optional): 颜色条刻度标签的小数位数. Defaults to 1.
        colorbar_fontsize (int, optional): 颜色条字体大小. Defaults to 8.
        colorbar_nticks (int, optional): 颜色条刻度数量. Defaults to 2.
        colorbar_shrink (float, optional): 颜色条收缩比例. Defaults to 0.15.
        colorbar_aspect (int, optional): 颜色条宽高比. Defaults to 8.
        colorbar_draw_border (bool, optional): 是否绘制颜色条边框. Defaults to False.
        title_name (str, optional): 图形标题. Defaults to "".
        title_fontsize (int, optional): 标题字体大小. Defaults to 12.
        as_outline (bool, optional): 是否以轮廓线形式显示. Defaults to False.

    Raises:
        ValueError: 当指定的物种不支持时抛出
        ValueError: 当指定的图集不支持时抛出
        ValueError: 当数据为空时抛出
        ValueError: 当vmin大于vmax时抛出

    Returns:
        Axes: 包含绘制图像的matplotlib坐标轴对象
    """
    # 获取或创建坐标轴对象
    ax = ax or plt.gca()

    # 提取所有数值用于确定vmin和vmax
    values = list(data.values())
    if not values:
        raise ValueError("data 不能为空")
    vmin = min(values) if vmin is None else vmin
    vmax = max(values) if vmax is None else vmax
    if vmin == vmax:
        vmin, vmax = min(0, vmin), max(0, vmax)
    if vmin > vmax:
        raise ValueError("vmin必须小于等于vmax")

    # 设置数据文件路径
    # 定义不同物种、表面类型和图集的文件路径信息
    atlas_info = {
        "human": {
            "surf": {
                "lh": f"surfaces/human_fsLR/tpl-fsLR_den-32k_hemi-L_{surf}.surf.gii",
                "rh": f"surfaces/human_fsLR/tpl-fsLR_den-32k_hemi-R_{surf}.surf.gii",
            },
            "atlas": {
                "glasser": {
                    "lh": "atlases/human_Glasser/fsaverage.L.Glasser.32k_fs_LR.label.gii",
                    "rh": "atlases/human_Glasser/fsaverage.R.Glasser.32k_fs_LR.label.gii",
                },
                "bna": {
                    "lh": "atlases/human_BNA/fsaverage.L.BNA.32k_fs_LR.label.gii",
                    "rh": "atlases/human_BNA/fsaverage.R.BNA.32k_fs_LR.label.gii",
                },
            },
            "sulc": {
                "lh": "surfaces/human_fsLR/100206.L.sulc.32k_fs_LR.shape.gii",
                "rh": "surfaces/human_fsLR/100206.R.sulc.32k_fs_LR.shape.gii",
            }
        },
        "chimpanzee": {
            "surf": {
                "lh": f"surfaces/chimpanzee_BNA/ChimpYerkes29_v1.2.L.{surf}.32k_fs_LR.surf.gii",
                "rh": f"surfaces/chimpanzee_BNA/ChimpYerkes29_v1.2.R.{surf}.32k_fs_LR.surf.gii",
            },
            "atlas": {
                "bna": {
                    "lh": "atlases/chimpanzee_BNA/ChimpBNA.L.32k_fs_LR.label.gii",
                    "rh": "atlases/chimpanzee_BNA/ChimpBNA.R.32k_fs_LR.label.gii",
                },
            }
        },
        "macaque": {
            "surf": {
                "lh": f"surfaces/macaque_BNA/civm.L.{surf}.32k_fs_LR.surf.gii",
                "rh": f"surfaces/macaque_BNA/civm.R.{surf}.32k_fs_LR.surf.gii",
            },
            "atlas": {
                "charm5": {
                    "lh": "atlases/macaque_CHARM5/L.charm5.label.gii",
                    "rh": "atlases/macaque_CHARM5/R.charm5.label.gii",
                },
                "charm6": {
                    "lh": "atlases/macaque_CHARM6/L.charm6.label.gii",
                    "rh": "atlases/macaque_CHARM6/R.charm6.label.gii",
                },
                "bna": {
                    "lh": "atlases/macaque_BNA/MBNA_124_32k_L.label.gii",
                    "rh": "atlases/macaque_BNA/MBNA_124_32k_R.label.gii",
                },
                "d99": {
                    "lh": "atlases/macaque_D99/L.d99.label.gii",
                    "rh": "atlases/macaque_D99/R.d99.label.gii",
                },
            },
            "sulc": {
                "lh": "surfaces/macaque_BNA/SC_06018.L.sulc.32k_fs_LR.shape.gii",
                "rh": "surfaces/macaque_BNA/SC_06018.R.sulc.32k_fs_LR.shape.gii",
            }

        }
    }

    # 检查物种是否支持
    if species not in atlas_info:
        raise ValueError(f"Unsupported species: {species}. Supported species are: {list(atlas_info.keys())}")
    else:
        # 检查指定物种的图集是否支持
        if atlas not in atlas_info[species]["atlas"]:
            raise ValueError(f"Unsupported {atlas} atlas for {species}")

    # 创建Plot对象，用于绘制大脑皮层
    if surf != "flat":
        p = Plot(
            NEURODATA / atlas_info[species]["surf"]["lh"],
            NEURODATA / atlas_info[species]["surf"]["rh"],
        )
    else:
        # NOTE: 目前只有人和猕猴具有flat surface，暂时不支持黑猩猩
        p = Plot(
            NEURODATA / atlas_info[species]["surf"]["lh"],
            NEURODATA / atlas_info[species]["surf"]["rh"],
            views="dorsal",
            zoom = 1.2,
        )
        lh_sulc_file = NEURODATA / atlas_info[species]["sulc"]["lh"]
        rh_sulc_file = NEURODATA / atlas_info[species]["sulc"]["rh"]
        p.add_layer(
            {
                "left": nib.load(lh_sulc_file).darrays[0].data,
                "right": nib.load(rh_sulc_file).darrays[0].data,
            },
            cmap="Grays_r",
            cbar=False
        )

    # 分离左半球和右半球的数据
    hemisphere_data = {}
    for hemi in ["lh", "rh"]:
        hemi_data = {k: v for k, v in data.items() if k.startswith(f"{hemi}_")}
        hemi_parc = _map_labels_to_values(
            hemi_data, NEURODATA / atlas_info[species]["atlas"][atlas][hemi]
        )
        hemisphere_data[hemi] = hemi_parc

    # 画图
    # colorbar参数设置（用列表统一管理，便于维护）
    colorbar_params = [
        ("location", colorbar_location),
        ("label_direction", colorbar_label_rotation),
        ("decimals", colorbar_decimals),
        ("fontsize", colorbar_fontsize),
        ("n_ticks", colorbar_nticks),
        ("shrink", colorbar_shrink),
        ("aspect", colorbar_aspect),
        ("draw_border", colorbar_draw_border),
    ]
    colorbar_kws = {k: v for k, v in colorbar_params}
    # 添加图层到绘图对象
    p.add_layer(
        {"left": hemisphere_data["lh"], "right": hemisphere_data["rh"]},
        cbar=colorbar,
        cmap=cmap,
        color_range=(vmin, vmax),
        cbar_label=colorbar_label_name,
        zero_transparent=False,
        as_outline=as_outline,
    )
    # 构建坐标轴并应用颜色条设置
    ax = p.build_axis(ax=ax, cbar_kws=colorbar_kws)
    # 设置图形标题
    ax.set_title(title_name, fontsize=title_fontsize)

    return ax
