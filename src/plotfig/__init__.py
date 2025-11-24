from importlib.metadata import version, PackageNotFoundError

from .bar import (
    plot_one_group_bar_figure,
    plot_one_group_violin_figure,
    plot_multi_group_bar_figure,
)
from .correlation import plot_correlation_figure
from .matrix import plot_matrix_figure
from .brain_surface import plot_brain_surface_figure
from .circos import plot_circos_figure
from .brain_connection import (
    plot_brain_connection_figure,
    save_brain_connection_frames,
    batch_crop_images,
    create_gif_from_images,
)
from .utils import (
    gen_hex_colors,
    gen_symmetric_matrix,
    gen_cmap,
    value_to_hex,
    is_symmetric_square,
)


__all__ = [
    # bar
    "plot_one_group_bar_figure",
    "plot_one_group_violin_figure",
    "plot_multi_group_bar_figure",
    # correlation
    "plot_correlation_figure",
    # matrix
    "plot_matrix_figure",
    # brain_surface
    "plot_brain_surface_figure",
    # circos
    "plot_circos_figure",
    # brain_connection
    "plot_brain_connection_figure",
    "save_brain_connection_frames",
    "batch_crop_images",
    "create_gif_from_images",
    # utils
    "gen_hex_colors",
    "gen_symmetric_matrix",
    "gen_cmap",
    "value_to_hex",
    "is_symmetric_square",
]

__author__ = "Ricardo Ryn"
__description__ = "A python package for neuroscience plotting."
try:
    __version__ = version("plotfig")
except PackageNotFoundError:
    __version__ = "unknown"
