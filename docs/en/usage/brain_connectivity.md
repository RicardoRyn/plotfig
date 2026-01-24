# Brain Connectivity Plot

Transparent brain plot that can display connectivity relationships between brain regions.
You need to prepare surface files for left and right hemispheres, brain region-related nii.gz files, and a connectivity matrix.

## Quick Plot

For all parameters, see the API documentation for [`plot_brain_connection_figure`](../api/#plotfig.brain_connection.plot_brain_connection_figure).

```python
from plotfig import plot_brain_connection_figure, gen_symmetric_matrix

# Generate random connectivity matrix
connectome = gen_symmetric_matrix(31, sparsity=0.1, seed=42)

# Left and right brain surface files and network node files need to be provided by yourself
lh_surfgii_file = r"example_data/103818.L.midthickness.32k_fs_LR.surf.gii"
rh_surfgii_file = r"example_data/103818.R.midthickness.32k_fs_LR.surf.gii"
niigz_file = r"example_data/network.nii.gz"

# HTML file output location
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

## Result Display

![output](../../assets/usage/brain_connectivity_files/output.gif)

The HTML file can be interactively viewed in a browser. You can manually take screenshots, or use the following command to batch generate multi-view images.

```python
from pathlib import Path
from plotfig import save_brain_connection_frames

# Create new folder to save frame images
Path(f"./example_data/brain_connection_figures").mkdir(parents=True, exist_ok=True)
save_brain_connection_frames(
    fig,
    output_dir=rf"./example_data/brain_connection_figures",
    n_frames=36
)
```

    100%|██████████| 36/36 [01:55<00:00,  3.19s/it]
    2025-11-24 11:02:55.867 | INFO     | plotfig.brain_connection:save_brain_connection_frames:323 - Saved 36 images in ./example_data/brain_connection_figures

plotfig provides a utility function to combine image sequences into GIF animations.

```python
from pathlib import Path
from plotfig import create_gif_from_images

create_gif_from_images(
    Path("example_data/brain_connection_figures"),
    output_name="output.gif"
)
```

    2025-11-24 11:07:46.885 | INFO     | plotfig.brain_connection:create_gif_from_images:417 - GIF saved to: example_data\brain_connection_figures\outpug.gif
