# 连线图

🚧 施工中 🚧 


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 生成一个随机的10x10矩阵
np.random.seed(1998)
matrix_size = 10
connectome = np.random.rand(matrix_size, matrix_size)
# 使矩阵对称
connectome = (connectome + connectome.T) / 2
# 将对角线置为0
np.fill_diagonal(connectome, 0)

node_colors = ["#ffaec9", "#ffc90e", "#b5e61d", "#7092be", "#efe4b0"]

fig = plot_symmetric_circle_figure(
    connectome, node_colors=node_colors, colorbar=True, vmin=0, vmax=1
)
fig.savefig("./figures/circle1.png", dpi=250, bbox_inches="tight")
```


    
![png](circos_files/circos_1_0.png)
    



```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 生成一个随机的100x100矩阵
matrix_size = 10
connectome = np.random.rand(matrix_size, matrix_size)
# 使矩阵对称
connectome = (connectome + connectome.T) / 2
# 将对角线置为0
np.fill_diagonal(connectome, 0)

fig = plot_asymmetric_circle_figure(connectome, colorbar=True)
fig.savefig("./figures/circle2.png", dpi=250, bbox_inches="tight")
```


    
![png](circos_files/circos_2_0.png)
    

