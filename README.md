<div align="center">

# plotfig

[![PyPI version](https://badge.fury.io/py/plotfig.svg)](https://badge.fury.io/py/plotfig)
[![Python version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

一个专为认知神经科学研究设计的 Python 可视化库，提供高效、易用且美观的绘图工具。

![plotfig](./docs/assets/plotfig.png)

</div>

## 功能特性

- 📊 **多种图表类型**：条形图、矩阵、相关性图、弦图、脑表面图、脑连接图
- 🎨 **专业科研风格**：内置多种配色方案，符合学术发表标准
- 📈 **自动显著性检验**：内置多种统计方法，自动绘制显著性标记
- 🔬 **专为神经科学设计**：支持常见灵长类脑区 atlas、脑网络可视化等特定场景
- 🚀 **简单易用**：简洁的 API，快速上手

## 快速开始

```python
import matplotlib.pyplot as plt

from plotfig import plot_one_group_bar_figure

# 绘制单组条形图
data = [[1.2, 2.3, 3.1], [4.5, 5.6, 6.2]]
plot_one_group_bar_figure(data)
plt.show()
```

## 安装

`plotfig` 要求 Python 3.11 及以上版本。

**使用 uv 安装：**

**使用 uv 安装：**
```bash
uv add plotfig
```

**使用 pip 安装：**

```bash
pip install plotfig
```

## 文档

详细文档和使用示例请访问 [plotfig 文档](https://ricardoryn.github.io/plotfig/)。

## 贡献

欢迎提交 Issue 或 PR！无论是 Bug 报告、功能建议还是文档改进，都非常欢迎在 [Issue](https://github.com/RicardoRyn/plotfig/issues) 中提出。

开发贡献流程请参见[贡献指南](https://ricardoryn.github.io/plotfig/)。
