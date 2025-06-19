# 脑连接图

🚧 施工中 🚧 


```python
import numpy as np
from plotfig import *

# ------- 模拟数据 -------
size = 202
matrix = np.zeros((size, size))  # 生成全0矩阵

# 增加连接
matrix[0, 1] = 1
matrix[0, 2] = 2
matrix[0, 3] = 3
matrix[4, 1] = -1
matrix[4, 2] = -2
matrix[4, 3] = -3
# 使矩阵对称
matrix = (matrix + matrix.T) / 2
connectome = matrix

# ------- 指定保存位置 -------
output_file = "./figures/brain_connection.html"

# ------- 画图 -------
plot_brain_connection_figure(
    connectome,
    output_file=output_file,
    scale_method="width",
    line_width=10,
)
```
