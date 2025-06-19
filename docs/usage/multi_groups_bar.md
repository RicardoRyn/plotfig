# 多组柱状图

## 快速出图

假如我们有2组数据，每组数据中又有3个bar。每个bar中有10个样本点。


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

plot_multi_group_bar_figure([[group1_bar1, group1_bar2, group1_bar3], [group2_bar1, group2_bar2, group2_bar3]])
```


    
![png](multi_groups_bar_files/multi_groups_bar_2_0.png)
    


## 图的美化

和单组柱状图类似，多组柱状图也有大量可调节的参数。
全部参数见[`plotfig.bar.plot_multi_group_bar_figure`](../api/#plotfig.bar.plot_multi_group_bar_figure)的API 文档。


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
plot_multi_group_bar_figure(
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
)
```


    
![png](multi_groups_bar_files/multi_groups_bar_5_0.png)
    


## 统计

多组柱状图暂时只支持外部进行检验，传入p值后在组内标星号。


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
plot_multi_group_bar_figure(
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


    
![png](multi_groups_bar_files/multi_groups_bar_8_0.png)
    

