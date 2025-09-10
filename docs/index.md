# 简介

`plotfig` 是一个专为科学数据可视化设计的 Python 库，致力于为认知神经科研工作人员提供高效、易用且美观的图形绘制工具。
该项目基于业界主流的可视化库—— `matplotlib`、`surfplot` 和 `plotly`等库开发，融合了三者的强大功能，能够满足神经科学以及脑连接组学中多种场景下的复杂绘图需求。

![plotfig](./assets/plotfig.png)

## 项目结构

项目采用模块化设计，包含如下主要功能模块：

- `bar.py`：条形图绘制，适用于分组数据的对比展示。
- `correlation.py`：相关性矩阵可视化，便于分析变量间的相关性分布。
- `matrix.py`：通用矩阵可视化，支持多种配色和注释方式。
- `brain_surface.py`：脑表面可视化，实现三维脑表面图集结构的绘制。
- `circos.py`：弦图可视化，适合平面展示脑区之间的连接关系。
- `brain_connection.py`：玻璃脑连接可视化，支持复杂的脑网络结构展示。

## 特性

- `plotfig` API 设计简洁，参数灵活，适合科研人员和数据分析师快速集成到自己的数据分析流程中。
- 其模块化架构便于后续功能扩展和自定义开发。
- 结合 `matplotlib` 支持矢量图或高分辨率位图和交互式 HTML 输出，适合论文发表和学术展示。

---

烫知识：一张图上的所有元素[^1]。
![Parts of a Figure](https://matplotlib.org/stable/_images/anatomy.png)

[^1]: [Quick start guide of matplotlib.](https://matplotlib.org/stable/tutorials/introductory/usage.html#parts-of-a-figure)
