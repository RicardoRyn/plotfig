# 矩阵图

矩阵图是一种用于展示多个变量之间成对关系的可视化方式，常见形式为一个对称的二维网格，其中每个单元格表示一对变量之间的统计关系。
它常用于探索数据集中多个变量之间的相关结构，是数据分析和科研绘图中的常用工具。

`plot_matrix_figure` 支持自动生成矩阵图。

## 快速出图

我们可以生成一个 10 × 19 的矩阵图，用于展示 10 个元素与另 19 个元素之间的成对关系。


```python
import numpy as np
from plotfig import *

data = np.random.rand(10, 19)

ax = plot_matrix_figure(data)
```


    
![png](matrix_files/matrix_4_0.png)
    


## 参数设置

全部参数见[`plot_matrix_figure`](../api/#plotfig.matrix.plot_matrix_figure)的 API 文档。


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

data = np.random.rand(4,4)

fig, ax = plt.subplots(figsize=(3,3))
ax = plot_matrix_figure(
    data,
    row_labels_name=["A", "B", "C", "D"],
    col_labels_name=["E", "F", "G", "H"],
    cmap="viridis",
    title_name="Matrix Figure",
    title_fontsize=10,
    colorbar=True,
    colorbar_label_name="Colorbar",
)
```


    
![png](matrix_files/matrix_7_0.png)
    

