# 相关图

## 快速出图

假如我们有2组样本数量一致的数据（都有100个样本）。我们希望画图显示它们是否具有相关性。


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

np.random.seed(42)
data1 = np.arange(100)
data2 = data1 + np.random.normal(1,50, 100)
# data2是在data1的基础上加上了噪声。
# 正经人都知道data1和data2相关，那么plotfig知不知道呢？

plot_correlation_figure(data1,data2)
```


    
![png](correlation_files/correlation_2_0.png)
    


## 参数设置

全部参数见[`plotfig.correlation`](../api/index.md/#plotfig.correlation)的API 文档。


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

np.random.seed(42)
data1 = np.arange(100)
data2 = data1 + np.random.normal(1,50, 100)
# data2是在data1的基础上加上了噪声。
# 正经人都知道data1和data2相关，那么plotfig知不知道呢？

fig, ax = plt.subplots(figsize=(3, 3))
plot_correlation_figure(
    data1,
    data2,
    stats_method="spearman",  # 仅有“spearman, pearson”，默认是spearman
    ci=True,  # 显示95%置信区间
    dots_color="green",
    line_color="pink",
    title_name="Correlation between data1 and data2",
    title_fontsize=10,
    title_pad=20,  # 控制释标题和图的距离，默认是10
    x_label_name="Data1",
    y_label_name="Data2",
)
```


    
![png](correlation_files/correlation_5_0.png)
    


利用 `hexbin=True` 。我们可以展示大量散点分布的密度，而不需要绘制所有的散点。


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

np.random.seed(42)
n = 100_000
data1 = np.random.standard_normal(n)
data2 = 2.0 + 3.0 * data1 + 4.0 * np.random.standard_normal(n)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3), layout="constrained")
plot_correlation_figure(
    data1,
    data2,
    ax=ax1
)

hb = plot_correlation_figure(
    data1,
    data2,
    ax=ax2,
    hexbin=True,
    hexbin_cmap="Reds",
    hexbin_gridsize=30
)
cb = fig.colorbar(hb, ax=ax2, label='counts')

```


    
![png](correlation_files/correlation_7_0.png)
    

