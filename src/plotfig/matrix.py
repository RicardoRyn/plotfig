import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def plot_matrix_figure(
    data,
    ax=None,
    row_labels_name=None,
    col_labels_name=None,
    cmap="bwr",
    vmin=None,
    vmax=None,
    aspect="equal",
    colorbar=True,
    colorbar_label_name="",
    colorbar_pad=0.1,
    colorbar_label_fontsize=10,
    colorbar_tick_fontsize=10,
    colorbar_tick_rotation=0,
    row_labels_fontsize=10,
    col_labels_fontsize=10,
    x_rotation=60,
    title_name="",
    title_fontsize=15,
    title_pad=20,
    diag_border=False,
    **imshow_kwargs,
):
    ax = ax or plt.gca()
    vmin = vmin if vmin is not None else np.min(data)
    vmax = vmax if vmax is not None else np.max(data)

    im = ax.imshow(
        data, cmap=cmap, vmin=vmin, vmax=vmax, aspect=aspect, **imshow_kwargs
    )
    ax.set_title(title_name, fontsize=title_fontsize, pad=title_pad)
    if diag_border:
        for i in range(data.shape[0]):
            ax.add_patch(plt.Rectangle((i-0.5, i-0.5), 1, 1, fill=False, edgecolor='black', lw=0.5))

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
            colorbar_label_name, rotation=-90, va="bottom", fontsize=colorbar_label_fontsize
        )
        cbar.ax.tick_params(
            labelsize=colorbar_tick_fontsize, rotation=colorbar_tick_rotation
        )
        # Match colorbar height to the main plot
        ax_pos = ax.get_position()
        cax.set_position(
            [cax.get_position().x0, ax_pos.y0, cax.get_position().width, ax_pos.height]
        )

    return im


def main():
    """测试绘图函数的功能"""
    from pathlib import Path

    # 测试数据
    np.random.seed(42)
    data = np.random.rand(4, 4)
    # 测试函数
    fig, ax = plt.subplots(1, 1, figsize=(3, 3))
    plot_matrix_figure(
        data,
        ax=ax,
        row_labels_name=["A", "B", "C", "D"],
        col_labels_name=["E", "F", "G", "H"],
        cmap="viridis",
        vmin=None,
        vmax=None,
        aspect="equal",
        colorbar=True,
        colorbar_label_name="",
        colorbar_pad=0.1,
        colorbar_label_fontsize=10,
        colorbar_tick_fontsize=10,
        colorbar_tick_rotation=0,
        row_labels_fontsize=10,
        col_labels_fontsize=10,
        x_rotation=60,
        title_name="",
        title_fontsize=15,
        title_pad=20,
    )
    # 测试输出
    save_dir = Path(__file__).parent / "tests_output"
    save_dir.mkdir(exist_ok=True)  # 自动创建这个目录（如果没有）
    save_path = save_dir / "test.png"
    fig.savefig(save_path, dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
