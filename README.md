# plotfig

## 简介

`plotfig` 是一个专为科学数据可视化设计的 Python 库，
致力于为认知神经科研工作人员提供高效、易用且美观的图形绘制工具。
该项目基于业界主流的可视化库—— `matplotlib`、`surfplot` 和 `plotly`等库开发，
融合了三者的强大功能，能够满足神经科学以及脑连接组学中多种场景下的复杂绘图需求。

![plotfig](https://github.com/RicardoRyn/plotfig/blob/main/docs/assets/plotfig.png)

### 项目结构

项目采用模块化设计，核心代码位于 `src/plotfig/` 目录下，包含如下主要功能模块：

- `bar.py`：条形图绘制，适用于分组数据的对比展示。
- `matrix.py`：通用矩阵可视化，支持多种配色和注释方式。
- `correlation.py`：相关性矩阵可视化，便于分析变量间的相关性分布。
- `circos.py`：弦图可视化，适合平面展示脑区之间的连接关系。
- `brain_surface.py`：脑表面可视化，实现三维脑表面图集结构的绘制。
- `brain_connection.py`：玻璃脑连接可视化，支持复杂的脑网络结构展示。

### 文档与示例

`plotfig` 提供了网页文档和使用示例。具体参见[使用教程](https://ricardoryn.github.io/plotfig/)。

## 安装

`plotfig` 支持通过包管理器安装或直接从源码中安装，要求 Python 3.11 及以上版本。

### 使用包管理器安装 (推荐)

=== "uv"

    ``` bash
    uv add plotfig
    ```

=== "pip"

    ``` bash
    pip install plotfig
    ```

### 从源码中安装

首先下载源码到某个目录（例如 `/path/to/plotfig`）：

```bash
git clone https://github.com/RicardoRyn/plotfig.git /path/to/plotfig
```

然后在您的项目目录中执行：

=== "uv"

    ``` bash
    uv add /path/to/plotfig
    ```

=== "pip"

    ``` bash
    pip install /path/to/plotfig
    ```

> **注意**：`/path/to/plotfig` 应替换为实际的路径。

### 贡献

如果您希望体验这些功能或参与 `plotfig` 的开发，可以选择以 开发模式（editable mode） 安装项目。

这种安装方式允许您对本地源码的修改立即生效，非常适合调试、开发和贡献代码。

推荐流程：

1. Fork 本仓库到您的 GitHub 账号
2. 克隆您的 Fork 到本地：

```bash
git clone https://github.com/USERNAME/plotfig.git /path/to/plotfig
```

3. 在您的项目目录中以开发模式安装：

=== "uv"

    ``` bash
    uv add --editable /path/to/plotfig
    ```

=== "pip"

    ``` bash
    pip install -e /path/to/plotfig
    ```

> **注意**：`/path/to/plotfig` 应替换为实际的路径。

---

**欢迎提交 Issue 或 PR！**

无论是 Bug 报告、功能建议、还是文档改进。

都非常欢迎在 [Issue](https://github.com/RicardoRyn/plotfig/issues) 中提出。

也可以直接提交 [PR](https://github.com/RicardoRyn/plotfig/pulls)，一起变得更强 💪！
