import numpy as np
import matplotlib.colors as mcolors
from matplotlib.colors import LinearSegmentedColormap, Colormap, Normalize


def gen_hex_colors(n: int, seed: int = 42) -> list[str]:
    """
    生成 n 个随机的十六进制颜色字符串。

    Args:
        n (int): 需要生成的颜色数量。
        seed (int, optional): 随机种子，默认为 42。

    Returns:
        list[str]: 包含 n 个十六进制颜色字符串的列表。
    """

    RNG = np.random.default_rng(seed=seed)
    rgb = RNG.integers(0, 256, size=(n, 3))  # n×3 的整数矩阵
    colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in rgb]
    return colors


def gen_cmap(color: str = "red") -> Colormap:
    """
    生成一个从白色到指定颜色的线性渐变色图。

    Args:
        color (str, optional): 渐变的目标颜色，默认为 "red"。

    Returns:
        Colormap: 线性渐变的色图对象。
    """

    cmap = LinearSegmentedColormap.from_list("white_to_color", ["white", color])
    return cmap


def value_to_hex(value: float, cmap: Colormap, norm: Normalize) -> str:
    """
    根据数值、色图和归一化对象，将数值映射为十六进制颜色字符串。

    Args:
        value (float): 需要映射的数值。
        cmap (Colormap): 用于映射的色图对象。
        norm (Normalize): 用于归一化的对象。

    Returns:
        str: 映射得到的十六进制颜色字符串。
    """

    rgba = cmap(norm(value))  # 得到 RGBA
    return mcolors.to_hex(rgba)
