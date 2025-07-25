## 普通安装

`plotfig` 支持通过 `pip` 或源码安装，要求 Python 3.11 及以上版本。


**使用 pip 安装 <small>(推荐)</small>**

```bash
pip install plotfig
```

**使用 GitHub 源码安装**

```bash
git clone https://github.com/RicardoRyn/plotfig.git
cd plotfig
pip install .
```

## 开发版安装

当你希望参与 plotfig 的开发，或想在使用过程中尝试尚未正式发布的新功能、最新修复的 bug 时，可以选择以开发模式安装。
该方式会以“可编辑模式（editable mode）”将项目安装到环境中，使你对本地源码的修改可以立即生效，非常适合用于开发、调试和贡献代码。

建议先 Fork 仓库，然后克隆你自己的 Fork：

```bash
git clone -b dev https://github.com/<your-username>/plotfig.git
cd plotfig
pip install -e .
```

## 依赖要求

`plotfig` 依赖若干核心库，这些依赖会在安装过程中自动处理，但建议用户事先了解其版本要求以避免兼容性问题。

- [matplotlib](https://matplotlib.org/) &ge; 3.10.1  
- [mne-connectivity](https://mne.tools/mne-connectivity/stable/index.html) &ge; 0.7.0  
- [nibabel](https://nipy.org/nibabel/) &ge; 5.3.2  
- [numpy](https://numpy.org/) &ge; 2.2.4  
- [pandas](https://pandas.pydata.org/) &ge; 2.2.3  
- [plotly](https://plotly.com/) &ge; 6.0.1  
- [scipy](https://scipy.org/) &ge; 1.15.2  
- [surfplot](https://surfplot.readthedocs.io/en/latest/index.html) &ge; 0.2.0  
