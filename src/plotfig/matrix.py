import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from typing import Sequence, Any

Num = int | float

__all__ = ["plot_matrix_figure"]

def plot_matrix_figure(
    data: np.ndarray,
    ax: Axes | None = None,
    row_labels_name: Sequence[str] | None = None,
    col_labels_name: Sequence[str] | None = None,
    cmap: str = "bwr",
    vmin: Num | None = None,
    vmax: Num | None = None,
    aspect: str = "equal",
    colorbar: bool = True,
    colorbar_label_name: str = "",
    colorbar_pad: Num = 0.1,
    colorbar_label_fontsize: Num = 10,
    colorbar_tick_fontsize: Num = 10,
    colorbar_tick_rotation: Num = 0,
    row_labels_fontsize: Num = 10,
    col_labels_fontsize: Num = 10,
    x_rotation: Num = 60,
    title_name: str = "",
    title_fontsize: Num = 15,
    title_pad: Num = 20,
    diag_border: bool = False,
    **imshow_kwargs: Any,
) -> AxesImage:
    """Plot a matrix as a heatmap with optional labels, colorbar, and title.

    Args:
        data (np.ndarray): 2D array of shape (N, M) to display as the matrix.
        ax (Axes | None): Matplotlib axes to plot on. If None, uses current axes.
        row_labels_name (Sequence[str] | None): List of labels for the rows.
        col_labels_name (Sequence[str] | None): List of labels for the columns.
        cmap (str): Colormap to use for the matrix.
        vmin (Num | None): Minimum value for color scaling. Defaults to data.min().
        vmax (Num | None): Maximum value for color scaling. Defaults to data.max().
        aspect (str): Aspect ratio of the plot. Usually "equal" or "auto".
        colorbar (bool): Whether to show a colorbar.
        colorbar_label_name (str): Label for the colorbar.
        colorbar_pad (Num): Padding between the colorbar and the matrix.
        colorbar_label_fontsize (Num): Font size of the colorbar label.
        colorbar_tick_fontsize (Num): Font size of the colorbar ticks.
        colorbar_tick_rotation (Num): Rotation angle of the colorbar tick labels.
        row_labels_fontsize (Num): Font size for the row labels.
        col_labels_fontsize (Num): Font size for the column labels.
        x_rotation (Num): Rotation angle for the x-axis (column) labels.
        title_name (Num): Title of the plot.
        title_fontsize (Num): Font size of the title.
        title_pad (Num): Padding above the title.
        diag_border (bool): Whether to draw borders along the diagonal cells.
        **imshow_kwargs (Any): Additional keyword arguments for `imshow()`.

    Returns:
        AxesImage: The image object created by `imshow()`.
    """
    ax = ax or plt.gca()
    vmin = vmin if vmin is not None else np.min(data)
    vmax = vmax if vmax is not None else np.max(data)

    im = ax.imshow(
        data, cmap=cmap, vmin=vmin, vmax=vmax, aspect=aspect, **imshow_kwargs
    )
    ax.set_title(title_name, fontsize=title_fontsize, pad=title_pad)
    if diag_border:
        for i in range(data.shape[0]):
            ax.add_patch(
                plt.Rectangle(
                    (i - 0.5, i - 0.5), 1, 1, fill=False, edgecolor="black", lw=0.5
                )
            )

    if col_labels_name is not None:
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_xticklabels(
            col_labels_name,
            fontsize=col_labels_fontsize,
            rotation=x_rotation,
            ha="right",
            rotation_mode="anchor",
        )

    if row_labels_name is not None:
        ax.set_yticks(np.arange(data.shape[0]))
        ax.set_yticklabels(row_labels_name, fontsize=row_labels_fontsize)

    if colorbar:
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=colorbar_pad)
        cbar = ax.figure.colorbar(im, cax=cax)
        cbar.ax.set_ylabel(
            colorbar_label_name,
            rotation=-90,
            va="bottom",
            fontsize=colorbar_label_fontsize,
        )
        cbar.ax.tick_params(
            labelsize=colorbar_tick_fontsize, rotation=colorbar_tick_rotation
        )
        # Match colorbar height to the main plot
        ax_pos = ax.get_position()
        cax.set_position(
            [cax.get_position().x0, ax_pos.y0, cax.get_position().width, ax_pos.height]
        )

    return


def main():
    pass


if __name__ == "__main__":
    main()
