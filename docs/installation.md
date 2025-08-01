## 普通安装

`plotfig` 支持通过 `pip` 或源码安装，要求 Python 3.11 及以上版本。


**使用 pip 安装 <small>(推荐)</small>**

```bash
pip install plotfig
```

**使用 GitHub 源码安装**

```bash
git clone --depth 1 https://github.com/RicardoRyn/plotfig.git
cd plotfig
pip install .
```

## 贡献指南

如果您希望参与 `plotfig` 的开发，或者想体验尚未正式发布的新功能和最新修复的 bug，可以选择以开发模式安装项目。

这种“可编辑模式（editable mode）”安装方式允许您对本地源码的修改立即生效，非常适合开发、调试和贡献代码。

推荐先 Fork 仓库，然后克隆您自己的 Fork：

```bash
git clone -b dev https://github.com/<your-username>/plotfig.git
cd plotfig
pip install -e .
```

## 依赖要求

`plotfig` 依赖若干核心库，这些依赖将在安装过程中自动处理：

- [matplotlib](https://matplotlib.org/) ≥ 3.10.1  
- [mne-connectivity](https://mne.tools/mne-connectivity/stable/index.html) ≥ 0.7.0  
- [nibabel](https://nipy.org/nibabel/) ≥ 5.3.2  
- [numpy](https://numpy.org/) ≥ 2.2.4  
- [pandas](https://pandas.pydata.org/) ≥ 2.2.3  
- [plotly](https://plotly.com/) ≥ 6.0.1  
- [scipy](https://scipy.org/) ≥ 1.15.2  
- [surfplot](https://github.com/danjgale/surfplot) 需使用其 GitHub 仓库中的最新版，而非 PyPI 上的版本，因后者尚未包含所需功能。

!!! warning "指定 `surfplot` 版本"

    由于 PyPI 上的 `surfplot` 版本较旧，缺少 `plotfig` 所需功能，建议通过以下步骤安装其 GitHub 仓库的最新版：

    ```bash
    # 卸载旧版本
    pip uninstall surfplot

    # 克隆源码仓库并安装
    git clone --depth 1 https://github.com/danjgale/surfplot.git
    cd surfplot
    pip install .

    # 安装完成后，返回上级目录并删除源码文件夹
    cd ..
    rm -rf surfplot
    ```
