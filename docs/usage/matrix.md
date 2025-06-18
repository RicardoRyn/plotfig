# 矩阵图

## 快速出图

矩阵图，又称为热图（heat map）直观地展示任意形式的矩阵数据。


```python
import numpy as np
from plotfig import *

data = np.random.rand(10, 19)

plot_matrix_figure(data)
```




    <matplotlib.image.AxesImage at 0x24c9e9bc5f0>




    
![png](matrix_files/matrix_2_1.png)
    


## 参数设置

全部参数见[`plotfig.matrix`](../api/#plotfig.matrix)的API 文档。


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

data = np.random.rand(4,4)

fig, ax = plt.subplots(figsize=(3,3))
plot_matrix_figure(
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




    <matplotlib.image.AxesImage at 0x24c9e02cf50>




    
![png](matrix_files/matrix_5_1.png)
    

