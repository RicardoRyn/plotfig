# plotfig

## 简介

`plotfig` 是一个专为科学数据可视化设计的 Python 库，致力于为认知神经科研工作人员提供高效、易用且美观的图形绘制工具。
该项目基于业界主流的可视化库—— `matplotlib`、`surfplot` 和 `plotly`等库开发，融合了三者的强大功能，能够满足神经科学以及脑连接组学中多种场景下的复杂绘图需求。

![plotfig](https://github.com/RicardoRyn/plotfig/blob/main/docs/assets/plotfig.png)

### 项目结构

项目采用模块化设计，核心代码位于 `src/plotfig/` 目录下，包含如下主要功能模块：

- `bar.py`：条形图绘制，适用于分组数据的对比展示。
- `correlation.py`：相关性矩阵可视化，便于分析变量间的相关性分布。
- `matrix.py`：通用矩阵可视化，支持多种配色和注释方式。
- `brain_surface.py`：脑表面可视化，实现三维脑表面图集结构的绘制。
- `circos.py`：弦图可视化，适合平面展示脑区之间的连接关系。
- `brain_connection.py`：玻璃脑连接可视化，支持复杂的脑网络结构展示。

### 文档与示例

`plotfig` 提供了网页文档和使用示例。具体参见[使用教程](https://ricardoryn.github.io/plotfig/)。

## 安装

`plotfig` 支持通过 `pip` 或源码安装，要求 Python 3.11 及以上版本。

### 使用 pip 安装 (推荐)

```bash
pip install plotfig
```

### 使用 GitHub 源码安装

```bash
git clone --depth 1 https://github.com/RicardoRyn/plotfig.git
cd plotfig
pip install .
```

## 依赖

`plotfig` 依赖若干核心库，这些依赖将在安装过程中自动处理，但需要注意：

- [surfplot](https://github.com/danjgale/surfplot) 需使用其 GitHub 仓库中的最新版，而非 PyPI 上的版本，因后者尚未包含所需功能。

> ⚠️ **指定 `surfplot` 版本**
>
> 由于 PyPI 上的 `surfplot` 版本较旧，缺少 `plotfig` 所需功能，建议通过以下步骤安装其 GitHub 仓库的最新版。
>
> 如果您无须绘制 `brain surface` 图，可以忽略此步骤。

```bash
# 卸载旧版本
pip uninstall surfplot

# 克隆源码并安装
git clone --depth 1 https://github.com/danjgale/surfplot.git
cd surfplot
pip install .

# 安装完成后，返回上级目录并删除源码文件夹
cd ..
rm -rf surfplot
```

## 贡献

**_`dev` 分支通常包含最新功能以及尚未合并到 `main` 的修复。_**

如果您希望体验这些功能或参与 `plotfig` 的开发，可以选择以 开发模式（editable mode） 安装项目。

这种安装方式允许您对本地源码的修改立即生效，非常适合调试、开发和贡献代码。

推荐先 Fork 仓库，然后克隆您自己的 Fork 并安装 `dev` 分支：

```bash
git clone -b dev https://github.com/ <your-username >/plotfig.git
cd plotfig
pip install -e .
```

---

**欢迎提交 Issue 或 PR！**

无论是 Bug 报告、功能建议、还是文档改进。

都非常欢迎在 [Issue](https://github.com/RicardoRyn/plotfig/issues) 中提出。

也可以直接提交 [PR](https://github.com/RicardoRyn/plotfig/pulls)，一起变得更强 🙌！
