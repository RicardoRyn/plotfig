# 安装


`plotfig` 支持通过 `pip` 或源码安装，要求 Python 3.11 及以上版本。

## 使用 pip 安装 (推荐)

```bash
pip install plotfig
```

## 使用 GitHub 源码安装

```bash
git clone --depth 1 https://github.com/RicardoRyn/plotfig.git
cd plotfig
pip install .
```

## 依赖要求

`plotfig` 依赖若干核心库，这些依赖将在安装过程中自动处理，但需要注意：

- [surfplot](https://github.com/danjgale/surfplot) 需使用其 GitHub 仓库中的最新版，而非 PyPI 上的版本，因后者尚未包含所需功能。

!!! warning "指定 `surfplot` 版本"

    由于 PyPI 上的 `surfplot` 版本较旧，缺少 `plotfig` 所需功能，建议通过以下步骤安装其 GitHub 仓库的最新版。

    如果您无须绘制 `brain surface` 图，可以忽略此步骤。

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

## 贡献指南

如果您希望体验这些功能或参与 `plotfig` 的开发，可以选择以 开发模式（editable mode） 安装项目。

这种安装方式允许您对本地源码的修改立即生效，非常适合调试、开发和贡献代码。

推荐先 Fork 仓库，然后克隆您自己的 Fork 并安装 `main` 分支：

```bash
git clone https://github.com/USERNAME/plotfig.git
cd plotfig
pip install -e .
```

---

**欢迎提交 Issue 或 PR！**

无论是 Bug 报告、功能建议、还是文档改进。

都非常欢迎在 [Issue](https://github.com/RicardoRyn/plotfig/issues) 中提出。

也可以直接提交 [PR](https://github.com/RicardoRyn/plotfig/pulls)，一起变得更强 💪！
