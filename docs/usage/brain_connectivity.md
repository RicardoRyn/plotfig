# 脑连接图

透明的大脑图，可以展示脑区间的连接关系。
需要准备左右半脑的surface文件、脑区相关的nii.gz文件以及连接矩阵。


```python
import numpy as np
from plotfig import *

# 生成一个 31x31 的连接矩阵（对称加权矩阵，对角线为0）
matrix = np.zeros((31, 31))
matrix[0, 1] = 1
matrix[0, 2] = 2
matrix[0, 3] = 3
matrix[4, 1] = -1
matrix[4, 2] = -2
matrix[4, 3] = -3
matrix = (matrix + matrix.T) / 2  # 矩阵对称

connectome = matrix

output_file = "./figures/brain_connection.html"

lh_surfgii_file = r"e:\6_Self\plot_self_brain_connectivity\103818.L.midthickness.32k_fs_LR.surf.gii"
rh_surfgii_file = r"e:\6_Self\plot_self_brain_connectivity\103818.R.midthickness.32k_fs_LR.surf.gii"
niigz_file = rf"e:\6_Self\plot_self_brain_connectivity\human_Self_processing_network.nii.gz"

fig = plot_brain_connection_figure(
    connectome,
    lh_surfgii_file=lh_surfgii_file,
    rh_surfgii_file=rh_surfgii_file,
    niigz_file=niigz_file,
    output_file=output_file,
    scale_method="width",
    line_width=10,
)
```


    
![png](brain_connectivity_files/human.gif)
    


html文件可以在浏览器中交互。可以手动截图，也可以使用以下命令来生成图片。


```python
from pathlib import Path


Path(f"./figures/brain_connection").mkdir(parents=True, exist_ok=True)  # 新建文件夹保存帧图
save_brain_connection_frames(fig, output_dir=rf"./figures/brain_connection", n_frames=36)
```

    100%|██████████| 36/36 [02:01<00:00,  3.37s/it]

    保存了 36 张图片在 ./figures/brain_connection
    

    
    
