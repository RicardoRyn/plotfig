# Circos Plot

## Quick Plot

Circos plot is a visualization chart used to display connectivity relationships between different brain regions.
By connecting brain regions with arcs, you can quickly understand the connections between brain regions.

```python
from plotfig import plot_circos_figure
from plotfig.utils import gen_symmetric_matrix

# Randomly generate symmetric weighted matrix (diagonal is 0)
connectome = gen_symmetric_matrix(30, mode="nonneg", sparsity=0.1)

# Plot
fig = plot_circos_figure(connectome)

# Save image
# fig.savefig("./figures/circos1.png")
```

![png](../../assets/usage/circos_files/circos_1_0.png)

## Parameter Settings

For all parameters, see the API documentation for [`plot_circos_figure`](../api/#plotfig.circos.plot_circos_figure).

```python
from plotfig import plot_circos_figure
from plotfig.utils import gen_symmetric_matrix

# Randomly generate a 10x10 symmetric weighted matrix (diagonal is 0)
connectome = gen_symmetric_matrix(10, mode="nonneg", sparsity=0.2)
node_names = ["lh_A", "lh_B", "lh_C", "lh_D", "lh_E", "rh_A", "rh_B", "rh_C", "rh_D", "rh_E"]
node_colors = ["#ff0000", "blue", "green", "yellow", "orange", "red", "blue", "green", "yellow", "orange"]

# Plot
fig = plot_circos_figure(
    connectome,
    symmetric=True,
    node_names=node_names,
    node_colors=node_colors,
    node_space=2,
    node_label_fontsize=15,
    vmin=0.1,
    vmax=0.9,
    edge_color="purple",
    edge_alpha=0.8,
    colorbar=True,
    colorbar_orientation="horizontal",
    colorbar_label="Conncetivity",
)

# Save image
# fig.savefig("./figures/circos.png")
```

![png](../../assets/usage/circos_files/circos_3_0.png)

### Combining with Other Plots

By default, the `plot_circos_figure` function returns a `fig`, which can be directly used for saving, such as `fig.savefig("./figures/circos.png")`.

In special cases, we can also return `ax` to combine it with other plots.

```python
import matplotlib.pyplot as plt
from plotfig import plot_circos_figure
from plotfig.utils import gen_symmetric_matrix

fig = plt.figure(figsize=(6, 3))

ax1 = fig.add_subplot(1, 2, 1)
ax1.plot([1, 2, 3, 4], [2, 1, 4, 3])

ax2 = fig.add_subplot(1, 2, 2, projection="polar")
connectome = gen_symmetric_matrix(10, mode="nonneg", sparsity=0.1)
ax2 = plot_circos_figure(connectome, ax=ax2)

# Save image
# fig.savefig("./figures/circos.png")
```

![png](../../assets/usage/circos_files/circos_5_0.png)

### Symmetric and Asymmetric Circos Plots

`plotfig` can plot both symmetric and asymmetric styles of circos plots. Simply set it through the `symmetric` parameter.

```python
import matplotlib.pyplot as plt
from plotfig import plot_circos_figure
from plotfig.utils import gen_symmetric_matrix

fig = plt.figure(figsize=(7, 3))
ax1 = fig.add_subplot(1, 2, 1, projection="polar")
ax2 = fig.add_subplot(1, 2, 2, projection="polar")

connectome = gen_symmetric_matrix(10, mode="nonneg", sparsity=0.1)

ax1 = plot_circos_figure(connectome, symmetric=True, ax=ax1, colorbar=False)
ax2 = plot_circos_figure(connectome, symmetric=False, ax=ax2)

# Save image
# fig.savefig("./figures/circos.png")
```

![png](../../assets/usage/circos_files/circos_7_0.png)

### Edge Colors

The `edge_color` parameter can be used to set the color of edges, but regardless, the shade of edges will still be automatically adjusted based on connection weights.

```python
import matplotlib.pyplot as plt
from plotfig import plot_circos_figure
from plotfig.utils import gen_symmetric_matrix

fig = plt.figure(figsize=(12, 3), layout="constrained")
ax1 = fig.add_subplot(1, 3, 1, projection="polar")
ax2 = fig.add_subplot(1, 3, 2, projection="polar")
ax3 = fig.add_subplot(1, 3, 3, projection="polar")

connectome = gen_symmetric_matrix(10, mode="nonneg", sparsity=0.1)

ax1 = plot_circos_figure(connectome, ax=ax1, edge_color="red")
ax2 = plot_circos_figure(connectome, ax=ax2, edge_color="green")
ax3 = plot_circos_figure(connectome, ax=ax3, edge_color="blue")

# Save image
# fig.savefig("./figures/circos.png")
```

![png](../../assets/usage/circos_files/circos_9_0.png)

You can also apply Matplotlib's built-in common color maps (Colormap) through the `cmap` parameter.

!!! warning
    When using `cmap`, the `edge_color` parameter will no longer take effect.

```python
import matplotlib.pyplot as plt
from plotfig import plot_circos_figure
from plotfig.utils import gen_symmetric_matrix

fig = plt.figure(figsize=(12, 3), layout="constrained")
ax1 = fig.add_subplot(1, 3, 1, projection="polar")
ax2 = fig.add_subplot(1, 3, 2, projection="polar")
ax3 = fig.add_subplot(1, 3, 3, projection="polar")

connectome = gen_symmetric_matrix(10, mode="nonneg", sparsity=0.1)

ax1 = plot_circos_figure(connectome, ax=ax1, cmap="Reds")
ax2 = plot_circos_figure(connectome, ax=ax2, cmap="viridis")
ax3 = plot_circos_figure(connectome, ax=ax3, cmap="bwr")

# Save image
# fig.savefig("./figures/circos.png")
```

![png](../../assets/usage/circos_files/circos_11_0.png)

When negative values exist in the connectome data, edge colors cannot be customized, and the system will default to using Matplotlib's `bwr` color map.

```python
from plotfig import plot_circos_figure
from plotfig.utils import gen_symmetric_matrix

# Generate symmetric matrix with negative values
connectome = gen_symmetric_matrix(10, mode="all", sparsity=0.1)

fig = plot_circos_figure(connectome)

# Save image
# fig.savefig("./figures/circos.png")
```

    2025-09-05 15:09:37.347 | WARNING  | plotfig.circos:plot_circos_figure:116 - Due to negative values in connectome, connection colors cannot be customized; positive values will be displayed in red and negative values in blue

![png](../../assets/usage/circos_files/circos_13_1.png)
