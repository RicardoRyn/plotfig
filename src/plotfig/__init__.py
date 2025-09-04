from .bar import (
    plot_one_group_bar_figure,
    plot_one_group_violin_figure,
    plot_multi_group_bar_figure,
)
from .correlation import plot_correlation_figure
from .matrix import plot_matrix_figure
from .brain_surface import plot_brain_surface_figure
from .circos import plot_circos_figure
from .brain_connection import plot_brain_connection_figure, save_brain_connection_frames

from importlib.metadata import version, PackageNotFoundError

__all__ = [
    "plot_one_group_bar_figure",
    "plot_one_group_violin_figure",
    "plot_multi_group_bar_figure",

    "plot_correlation_figure",

    "plot_matrix_figure",

    "plot_brain_surface_figure",

    "plot_circos_figure",

    "plot_brain_connection_figure",
    "save_brain_connection_frames",
]

try:
    __version__ = version("plotfig")
except PackageNotFoundError:
    __version__ = "unknown"
