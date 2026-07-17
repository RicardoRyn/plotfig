# 简介

`plotfig` 是一个专为科学数据可视化设计的 Python 库，致力于为认知神经科研工作人员提供高效、易用且美观的图形绘制工具。
该项目基于业界主流的可视化库—— `matplotlib`、`surfplot` 和 `plotly`等库开发，融合了三者的强大功能，能够满足神经科学以及脑连接组学中多种场景下的复杂绘图需求。

![plotfig](assets/plotfig.png)

## 项目结构

项目采用模块化设计，包含如下主要功能模块：

- `bar.py`：条形图绘制，适用于分组数据的对比展示。
- `matrix.py`：通用矩阵可视化，支持多种配色和注释方式。
- `correlation.py`：相关性矩阵可视化，便于分析变量间的相关性分布。
- `circos.py`：弦图可视化，适合平面展示脑区之间的连接关系。
- `brain_surface.py`：脑表面可视化，实现三维脑表面图集结构的绘制。
- `brain_connection.py`：玻璃脑连接可视化，支持复杂的脑网络结构展示。

## 特性

- `plotfig` API 设计简洁，参数灵活，适合科研人员和数据分析师快速集成到自己的数据分析流程中。
- 其模块化架构便于后续功能扩展和自定义开发。
- 结合 `matplotlib` 支持矢量图或高分辨率位图和交互式 HTML 输出，适合论文发表和学术展示。

---

## Matplotlib 核心三要素：Figure、Axes 与 Subplot

烫知识：一张图上的所有元素[^1]。

![Parts of a Figure](https://matplotlib.org/stable/_images/anatomy.png)

在使用 Matplotlib 绘图时，Figure（画布）、Axes（坐标系） 和 Subplot（子图） 是三个最基础、最核心的概念。

### Figure（画布/图形窗口）

Figure 是整个绘图的最顶层容器。
你可以把它理解为一张空白的画布，或者是电脑屏幕上弹出的那个图形窗口。
Figure 承载着所有绘图元素。
你可以在它上面设置整张图的尺寸（figsize）、背景颜色、分辨率（dpi）等全局属性。

### Axes（坐标系/绘图区）

Axes 是 Matplotlib 中真正的“画图区域”，也是绝大多数数据处理操作的发生地。
Axes 是一个带有数据坐标系统的矩形区域。
它不仅包含你绘制的折线、散点、柱状图等图形，还包含了 X 轴、Y 轴、刻度标签、轴标签、标题等所有辅助元素。

一个 Figure（画布）上可以包含多个 Axes（坐标系）。
这些坐标系可以按网格整齐排列，也可以脱离网格、在画布上任意浮动。

### Subplot（子图/网格分区）

Subplot 是 Axes（坐标系）在网格排列下的一种特殊称呼。
当你想在一张画布上整齐地展示多张图表时（比如上下对比，或 2x2 的四方格），就需要将画布划分为规则的网格。
划分后，每一个格子里的坐标系，就叫做 Subplot（子图）。

Subplot 本质上就是一个 Axes。
它们具有完全相同的属性和方法（都可以画图、设置坐标轴）。
唯一的不同在于，Subplot 是通过 `subplots()` 函数在预设网格中批量生成的。

!!! info
    Subplot（子图）：专指通过 `subplots(`) 或 `add_subplot()` 在规则网格中生成的 Axes。

    Axes（坐标系）：是更广义的概念。它不仅包含网格里的子图，还包含通过 `add_axes([left, bottom, width, height])` 方法在画布上任意位置浮动的坐标系，也包含嵌入在主图中的嵌套小图（Inset Axes）。

[^1]: [Quick start guide of matplotlib.](https://matplotlib.org/stable/tutorials/introductory/usage.html#parts-of-a-figure)
