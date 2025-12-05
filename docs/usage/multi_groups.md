# 多组柱状图

## 快速出图

我们采用了多组柱状图（multi-group bar chart）来展示数据的整体分布情况。
该图包含 两组数据（即两个主类别），每组中包含 三个子柱（bar），分别代表不同的子条件或变量。
在每个 bar 内部，绘制了 10 个样本点，反映个体水平的变异性或观测值。

这种图形结构有助于同时比较：

- 每组内不同条件之间的平均差异；
- 不同组之间的整体趋势；
- 每个条件下样本的离散情况或分布特征。

为了增强信息表达，柱状图上还叠加了误差条（如标准差或准误），并使用散点图展示每个 bar 中的样本分布。


```python
import numpy as np
from plotfig import *

np.random.seed(42)
group1_bar1 = np.random.normal(3, 1, 10)
group1_bar2 = np.random.normal(3, 1, 10)
group1_bar3 = np.random.normal(3, 1, 10)
group2_bar1 = np.random.normal(3, 1, 10)
group2_bar2 = np.random.normal(3, 1, 10)
group2_bar3 = np.random.normal(3, 1, 10)

ax = plot_multi_group_bar_figure([[group1_bar1, group1_bar2, group1_bar3], [group2_bar1, group2_bar2, group2_bar3]])
```


    
![png](multi_groups_files/multi_groups_3_0.png)
    


## 图的美化

与单组柱状图类似，多组柱状图也提供了大量可调节的参数，用于灵活控制图像的外观。  
本节仅展示其中的一部分参数。

完整参数列表请参见 [`plot_multi_group_bar_figure`](../api/#plotfig.bar.plot_multi_group_bar_figure) 的 API 文档。


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

np.random.seed(42)
group1_bar1 = np.random.normal(3, 1, 10)
group1_bar2 = np.random.normal(3, 1, 10)
group1_bar3 = np.random.normal(3, 1, 10)
group2_bar1 = np.random.normal(3, 1, 10)
group2_bar2 = np.random.normal(3, 1, 10)
group2_bar3 = np.random.normal(3, 1, 10)

fig, ax = plt.subplots(figsize=(6, 3))
ax = plot_multi_group_bar_figure(
    [[group1_bar1, group1_bar2, group1_bar3], [group2_bar1, group2_bar2, group2_bar3]],
    ax=ax,
    group_labels=["A", "B"],
    bar_labels=["D", "E", "F"],
    bar_width=0.2,
    bar_gap=0.05,
    bar_color=["tab:blue", "tab:orange", "tab:green"],
    errorbar_type="sd",
    dots_color="pink",
    dots_size=15,
    title_name="Title name",
    title_fontsize=15,
    y_label_name="Y label name",
)
```


    
![png](multi_groups_files/multi_groups_6_0.png)
    


## 统计

多组柱状图目前仅支持通过外部统计检验传入 p 值，并在组内相应位置标注星号。

关于“外部统计检验”的详细说明，请参见：[单组柱状图 / 统计](single_group.md#_7)。


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

np.random.seed(42)
group1_bar1 = np.random.normal(3, 1, 10)
group1_bar2 = np.random.normal(3, 1, 10)
group1_bar3 = np.random.normal(3, 1, 10)
group2_bar1 = np.random.normal(3, 1, 10)
group2_bar2 = np.random.normal(3, 1, 10)
group2_bar3 = np.random.normal(3, 1, 10)

fig, ax = plt.subplots(figsize=(6, 3))
ax = plot_multi_group_bar_figure(
    [[group1_bar1, group1_bar2, group1_bar3], [group2_bar1, group2_bar2, group2_bar3]],
    ax=ax,
    group_labels=["A", "B"],
    bar_labels=["D", "E", "F"],
    bar_width=0.2,
    bar_gap=0.05,
    bar_color=["tab:blue", "tab:orange", "tab:green"],
    errorbar_type="se",
    dots_color="pink",
    dots_size=15,
    title_name="Title name",
    title_fontsize=15,
    y_label_name="Y label name",
    statistic=True,
    test_method="external",
    p_list=[[0.05, 0.01, 0.001], [0.001, 0.01, 0.05]]
)
```


    
![png](multi_groups_files/multi_groups_9_0.png)
    

