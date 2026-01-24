<div align="center">

# plotfig

[![PyPI version](https://badge.fury.io/py/plotfig.svg)](https://badge.fury.io/py/plotfig)
[![Python version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

一个专为科学数据可视化设计的 Python 库，致力于为认知神经科研工作人员提供高效、易用且美观的图形绘制工具。

</div>

## 功能特性

- 📊 **多种图表类型**：条形图、矩阵、相关性图、弦图、脑表面图、脑连接图
- 🎨 **专业科研风格**：内置多种配色方案，符合学术发表标准
- 🔬 **专为神经科学设计**：支持脑区 atlas、脑网络可视化等特定场景
- 🚀 **简单易用**：简洁的 API，快速上手

## 示例展示

### 单组条形图
![Single Group Bar](https://github.com/RicardoRyn/plotfig/blob/main/docs/usage/single_group_files/single_group_11_0.png)

### 多组条形图
![Multi Groups Bar](https://github.com/RicardoRyn/plotfig/blob/main/docs/usage/multi_groups_files/multi_groups_2_0.png)

### 相关性矩阵
![Correlation Matrix](https://github.com/RicardoRyn/plotfig/blob/main/docs/usage/correlation_files/correlation_10_0.png)

### 脑连接图
![Brain Connectivity](https://github.com/RicardoRyn/plotfig/blob/main/docs/usage/brain_connectivity_files/output.gif)

### 脑表面图
![Brain Surface](https://github.com/RicardoRyn/plotfig/blob/main/docs/usage/brain_surface_files/brain_surface_10_0.png)

## 快速开始

```python
from plotfig import plot_one_group_bar_figure
import matplotlib.pyplot as plt

# 绘制单组条形图
data = [[1.2, 2.3, 3.1], [4.5, 5.6, 6.2]]
plot_one_group_bar_figure(data)
plt.show()
```

## 安装

`plotfig` 要求 Python 3.11 及以上版本。

**使用 uv 安装：**
```bash
uv add plotfig
```

**使用 pip 安装：**
```bash
pip install plotfig
```

其他安装方式请参见[详细安装教程](https://ricardoryn.github.io/plotfig/installation/)。

## 文档

详细文档和使用示例请访问 [plotfig 文档](https://ricardoryn.github.io/plotfig/)。

## 贡献

欢迎提交 Issue 或 PR！无论是 Bug 报告、功能建议还是文档改进，都非常欢迎在 [Issue](https://github.com/RicardoRyn/plotfig/issues) 中提出。

开发贡献流程请参见[贡献指南](https://ricardoryn.github.io/plotfig/)。
