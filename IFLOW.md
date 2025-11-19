# IFLOW.md - plotfig项目指南

## 项目概述

`plotfig` 是一个专为认知神经科学设计的Python数据可视化库，基于`matplotlib`、`surfplot`和`plotly`等主流可视化库开发。该项目旨在为科研工作者提供高效、易用且美观的图形绘制工具，特别适用于神经科学和脑连接组学领域的复杂绘图需求。

项目特点：
- 模块化设计，功能丰富
- 支持多种科学绘图类型
- 专门针对神经科学数据可视化需求优化

## 项目结构

```
plotfig/
├── src/plotfig/          # 核心源码目录
│   ├── __init__.py       # 导出所有公共API
│   ├── bar.py            # 条形图绘制
│   ├── brain_connection.py # 大脑连接可视化
│   ├── brain_surface.py  # 脑表面可视化
│   ├── circos.py         # 弦图可视化
│   ├── correlation.py    # 相关性矩阵可视化
│   ├── matrix.py         # 通用矩阵可视化
│   ├── utils/            # 工具函数模块
│   └── data/             # 数据文件
├── tests/                # 测试文件
├── notebooks/            # Jupyter笔记本示例
├── docs/                 # 文档文件
├── pyproject.toml        # 项目配置文件
└── README.md             # 项目说明文档
```

## 核心功能模块

### 1. brain_connection.py
提供大脑连接图的3D可视化功能，支持：
- 基于NIfTI格式图集的ROI节点定位
- 使用Plotly创建交互式3D大脑连接图
- 支持根据连接强度调整线条宽度和颜色
- 可生成旋转动画帧并制作GIF

主要函数：
- `plot_brain_connection_figure`: 绘制大脑连接图
- `save_brain_connection_frames`: 生成旋转动画帧
- `batch_crop_images`: 批量裁剪图像
- `create_gif_from_images`: 从图像生成GIF

### 2. correlation.py
支持两个数据集之间的相关性分析和可视化：
- 支持Spearman和Pearson相关性计算
- 可绘制散点图、回归线和置信区间
- 提供多种轴标签格式化选项

主要函数：
- `plot_correlation_figure`: 绘制相关性图

### 3. 其他模块
- `bar.py`: 条形图和小提琴图绘制
- `matrix.py`: 通用矩阵可视化
- `brain_surface.py`: 脑表面可视化
- `circos.py`: 弦图可视化

## 依赖管理

项目要求Python 3.11+版本，关键依赖包括：
- `matplotlib`: 基础绘图库
- `plotly`: 交互式3D可视化
- `surfplot`: 脑表面绘制（需从GitHub安装最新版）
- `numpy`, `scipy`: 数值计算
- `nibabel`: 神经影像数据处理
- `imageio`: 图像处理

## API使用示例

### 大脑连接可视化
```python
from plotfig import plot_brain_connection_figure

fig = plot_brain_connection_figure(
    connectome=connectome_matrix,
    lh_surfgii_file="lh_surface.gii",
    rh_surfgii_file="rh_surface.gii", 
    niigz_file="atlas.nii.gz",
    scale_method="width_color",
    line_width=10
)
```

### 相关性分析
```python
from plotfig import plot_correlation_figure

plot_correlation_figure(
    data1=[1, 2, 3, 4, 5],
    data2=[2, 4, 6, 8, 10],
    stats_method="pearson",
    ci=True,
    title_name="Correlation Plot"
)
```

## 开发和测试

项目支持开发模式安装：
```bash
pip install -e .
```

测试文件位于`tests/`目录，示例代码在`notebooks/`目录。

## 构建和安装

项目使用Hatchling作为构建后端，通过`pyproject.toml`管理依赖和构建配置。

安装命令：
- PyPI安装：`pip install plotfig`
- 源码安装：`pip install .`
- 开发安装：`pip install -e .`

## 文档和资源

- 在线文档：https://ricardoryn.github.io/plotfig/
- 源代码：https://github.com/RicardoRyn/plotfig
- 问题反馈：https://github.com/RicardoRyn/plotfig/issues