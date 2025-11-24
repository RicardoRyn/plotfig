# 脑连接图

透明的大脑图，可以展示脑区间的连接关系。
需要准备左右半脑的surface文件、脑区相关的nii.gz文件以及连接矩阵。


```python
from plotfig import plot_brain_connection_figure, gen_symmetric_matrix


# 生成随机的连接矩阵
connectome = gen_symmetric_matrix(31, sparsity=0.1, seed=42)

# 左右脑surface文件以及网络节点文件需自行提供
lh_surfgii_file = r"example_data/103818.L.midthickness.32k_fs_LR.surf.gii"
rh_surfgii_file = r"example_data/103818.R.midthickness.32k_fs_LR.surf.gii"
niigz_file = r"example_data/network.nii.gz"

# html文件输出位置
output_file = "example_data/brain_connection.html"

fig = plot_brain_connection_figure(
    connectome,
    lh_surfgii_file=lh_surfgii_file,
    rh_surfgii_file=rh_surfgii_file,
    niigz_file=niigz_file,
    output_file=output_file,
    scale_method="width",
    line_width=10,
    nodes_name=[f"ROI_{i}" for i in range(connectome.shape[0])],
)

```

## 结果展示

![output](brain_connectivity_files/output.gif)

html文件可以在浏览器中交互。可以手动截图，也可以使用以下命令来批量生成多视角生成图片。


```python
from pathlib import Path
from plotfig import save_brain_connection_frames


# 新建文件夹保存帧图
Path(f"./example_data/brain_connection_figures").mkdir(parents=True, exist_ok=True)
save_brain_connection_frames(
    fig,
    output_dir=rf"./example_data/brain_connection_figures",
    n_frames=36
)

```

    100%|██████████| 36/36 [01:55<00:00,  3.19s/it]
    2025-11-24 11:02:55.867 | INFO     | plotfig.brain_connection:save_brain_connection_frames:323 - 保存了 36 张图片在 ./example_data/brain_connection_figures
    

plotfig 提供了将图片序列整合生成 GIF 动画的工具函数。


```python
from pathlib import Path
from plotfig import create_gif_from_images

create_gif_from_images(
    Path("example_data/brain_connection_figures"),
    output_name="output.gif"
)

```

    2025-11-24 11:07:46.885 | INFO     | plotfig.brain_connection:create_gif_from_images:417 - GIF 已保存到: example_data\brain_connection_figures\outpug.gif
    
