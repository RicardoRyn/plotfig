import matplotlib.colors as mcolors
import numpy as np
from matplotlib.colors import Colormap, LinearSegmentedColormap, Normalize


def gen_hex_colors(n: int, seed: int = 42) -> list[str]:
    """生成指定数量的随机十六进制颜色代码。

    该函数使用 NumPy 的随机数生成器创建随机 RGB 颜色值，并转换为十六进制格式。
    通过固定随机种子确保结果可重复，适用于需要一致配色方案的科学可视化。

    Args:
        n (int): 需要生成的颜色数量，必须为正整数。
        seed (int): 随机种子，用于确保结果可重复。默认为 42。

    Returns:
        list[str]: 包含 n 个十六进制颜色字符串的列表，格式为 "#RRGGBB"。

    Examples:
        >>> # 生成 3 个随机颜色
        >>> colors = gen_hex_colors(3)
        >>> print(colors)
        ['#66a0a9', '#8b7d3a', '#c94f6d']

        >>> # 使用不同的随机种子
        >>> colors = gen_hex_colors(5, seed=123)
        >>> len(colors)
        5

        >>> # 在绘图中使用
        >>> import matplotlib.pyplot as plt
        >>> colors = gen_hex_colors(10)
        >>> for i, color in enumerate(colors):
        ...     plt.bar(i, i+1, color=color)

    Notes:
        - RGB 值范围为 [0, 255]
        - 相同的 n 和 seed 参数总是生成相同的颜色序列
        - 生成的颜色是完全随机的，可能包含对比度较低的颜色
    """

    RNG = np.random.default_rng(seed=seed)
    rgb = RNG.integers(0, 256, size=(n, 3))  # n×3 的整数矩阵
    colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in rgb]
    return colors


def gen_white_to_color_cmap(color: str = "red") -> Colormap:
    """生成从白色到指定颜色的线性渐变色图。

    该函数创建一个双色线性渐变色图，从白色（最小值）平滑过渡到指定颜色（最大值）。
    适用于热力图、相关矩阵、脑连接图等需要表示连续数值强度的可视化场景。

    Args:
        color (str): 渐变的目标颜色，支持 matplotlib 颜色名称（如 "red", "blue"）、
            十六进制格式（如 "#FF0000"）或 RGB 元组。默认为 "red"。

    Returns:
        Colormap: matplotlib 的线性渐变色图对象，可直接用于绘图函数。

    Examples:
        >>> # 生成红色渐变色图
        >>> cmap = gen_cmap("red")
        >>> 
        >>> # 在热力图中使用
        >>> import matplotlib.pyplot as plt
        >>> import numpy as np
        >>> data = np.random.rand(10, 10)
        >>> plt.imshow(data, cmap=gen_cmap("blue"))
        >>> plt.colorbar()
        >>> 
        >>> # 使用十六进制颜色
        >>> cmap = gen_cmap("#FF5733")
        >>> 
        >>> # 在散点图中使用
        >>> x = np.random.rand(100)
        >>> y = np.random.rand(100)
        >>> c = np.random.rand(100)
        >>> plt.scatter(x, y, c=c, cmap=gen_cmap("purple"))

    Notes:
        - 色图名称固定为 "white_to_color"
        - 渐变是线性的，白色对应数值范围的最小值，指定颜色对应最大值
        - 支持所有 matplotlib 认可的颜色格式
        - 常用于表示正值数据，如相关系数的绝对值、连接强度等

    See Also:
        value_to_hex : 将数值映射为十六进制颜色
        matplotlib.colors.LinearSegmentedColormap : 底层实现类
    """

    cmap = LinearSegmentedColormap.from_list("white_to_color", ["white", color])
    return cmap


def value_to_hex(value: float, cmap: Colormap, norm: Normalize) -> str:
    """将数值通过色图和归一化映射为十六进制颜色字符串。

    该函数实现了从数值到颜色的完整映射流程：首先使用归一化对象将数值映射到 [0, 1] 区间，
    然后通过色图将归一化值转换为 RGBA 颜色，最后转换为十六进制格式。常用于根据数据强度
    动态生成颜色，如脑连接图中根据连接强度着色连线。

    Args:
        value (float): 需要映射的原始数值，可以是任意范围的浮点数。
        cmap (Colormap): matplotlib 色图对象，定义了归一化值到颜色的映射关系。
        norm (Normalize): matplotlib 归一化对象，定义了原始数值到 [0, 1] 的映射规则。
            常用类型包括 Normalize（线性）、LogNorm（对数）等。

    Returns:
        str: 十六进制颜色字符串，格式为 "#RRGGBB"。

    Examples:
        >>> import matplotlib.pyplot as plt
        >>> from matplotlib.colors import Normalize
        >>> 
        >>> # 创建色图和归一化对象
        >>> cmap = gen_cmap("red")
        >>> norm = Normalize(vmin=0, vmax=100)
        >>> 
        >>> # 将数值映射为颜色
        >>> color1 = value_to_hex(25, cmap, norm)  # 浅红色
        >>> color2 = value_to_hex(75, cmap, norm)  # 深红色
        >>> print(color1, color2)
        '#ffbfbf' '#bf4040'
        >>> 
        >>> # 在脑连接图中使用
        >>> connection_strengths = [0.1, 0.5, 0.9]
        >>> norm = Normalize(vmin=0, vmax=1)
        >>> colors = [value_to_hex(s, cmap, norm) for s in connection_strengths]
        >>> 
        >>> # 使用对数归一化
        >>> from matplotlib.colors import LogNorm
        >>> norm_log = LogNorm(vmin=1, vmax=1000)
        >>> color = value_to_hex(100, cmap, norm_log)

    Notes:
        - 归一化对象决定了数值如何映射到 [0, 1] 区间
        - 色图决定了 [0, 1] 区间的值如何映射到具体颜色
        - 返回的十六进制颜色可直接用于 matplotlib 或 plotly 绘图
        - 如果 value 超出归一化对象的范围，会被裁剪到边界值

    See Also:
        gen_cmap : 生成线性渐变色图
        matplotlib.colors.Normalize : 线性归一化
        matplotlib.colors.LogNorm : 对数归一化
    """

    rgba = cmap(norm(value))  # 得到 RGBA
    return mcolors.to_hex(rgba)
