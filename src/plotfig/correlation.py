import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (
    ScalarFormatter,
    FuncFormatter,
    MultipleLocator,
    FormatStrFormatter,
)
from scipy import stats


def plot_correlation_figure(
    data1,
    data2,
    ax=None,
    stats_method="pearson",
    ci=False,
    dots_color="steelblue",
    dots_size=1,
    line_color="r",
    title_name="",
    title_fontsize=10,
    title_pad=10,
    x_label_name="",
    x_label_fontsize=10,
    x_tick_fontsize=10,
    x_tick_rotation=0,
    x_major_locator=None,
    x_max_tick_to_value=None,
    x_format="normal",  # normal, sci, 1f, percent
    y_label_name="",
    y_label_fontsize=10,
    y_tick_fontsize=10,
    y_tick_rotation=0,
    y_major_locator=None,
    y_max_tick_to_value=None,
    y_format="normal",  # normal, sci, 1f, percent
    asterisk_fontsize=10,
):
    def set_axis(
        ax, axis, label, labelsize, ticksize, rotation, locator, max_tick_value, fmt
    ):
        if axis == "x":
            set_label = ax.set_xlabel
            get_ticks = ax.get_xticks
            set_ticks = ax.set_xticks
            axis_formatter = ax.xaxis.set_major_formatter
            axis_major_locator = ax.xaxis.set_major_locator
        else:
            set_label = ax.set_ylabel
            get_ticks = ax.get_yticks
            set_ticks = ax.set_yticks
            axis_formatter = ax.yaxis.set_major_formatter
            axis_major_locator = ax.yaxis.set_major_locator

        set_label(label, fontsize=labelsize)
        ax.tick_params(axis=axis, which="major", labelsize=ticksize, rotation=rotation)
        if locator is not None:
            axis_major_locator(MultipleLocator(locator))
        if max_tick_value is not None:
            set_ticks([i for i in get_ticks() if i <= max_tick_value])

        if fmt == "sci":
            formatter = ScalarFormatter(useMathText=True)
            formatter.set_powerlimits((-2, 2))
            axis_formatter(formatter)
        elif fmt == "1f":
            axis_formatter(FormatStrFormatter("%.1f"))
        elif fmt == "percent":
            axis_formatter(FuncFormatter(lambda x, pos: f"{x:.0%}"))

    if ax is None:
        ax = plt.gca()

    A = np.asarray(data1)
    B = np.asarray(data2)

    slope, intercept, r_value, p_value, _ = stats.linregress(A, B)
    x_seq = np.linspace(A.min(), A.max(), 100)
    y_pred = slope * x_seq + intercept

    ax.scatter(A, B, c=dots_color, s=dots_size, alpha=0.8)
    ax.plot(x_seq, y_pred, line_color, lw=2)

    if ci:
        n = len(A)
        dof = n - 2
        t_val = stats.t.ppf(0.975, dof)
        x_mean = A.mean()
        residuals = B - (slope * A + intercept)
        s_err = np.sqrt(np.sum(residuals**2) / dof)
        SSxx = np.sum((A - x_mean) ** 2)
        conf_interval = t_val * s_err * np.sqrt(1 / n + (x_seq - x_mean) ** 2 / SSxx)
        ax.fill_between(
            x_seq,
            y_pred - conf_interval,
            y_pred + conf_interval,
            color="salmon",
            alpha=0.3,
        )

    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(title_name, fontsize=title_fontsize, pad=title_pad)

    set_axis(
        ax,
        "x",
        x_label_name,
        x_label_fontsize,
        x_tick_fontsize,
        x_tick_rotation,
        x_major_locator,
        x_max_tick_to_value,
        x_format,
    )
    set_axis(
        ax,
        "y",
        y_label_name,
        y_label_fontsize,
        y_tick_fontsize,
        y_tick_rotation,
        y_major_locator,
        y_max_tick_to_value,
        y_format,
    )

    # 标注r值或rho值
    if stats_method == "spearman":
        s, p = stats.spearmanr(A, B)
        label = r"$\rho$"
    else:
        s, p = stats.pearsonr(A, B)
        label = "r"

    asterisk = " ***" if p < 0.001 else " **" if p < 0.01 else " *" if p < 0.05 else ""
    x_start, x_end = ax.get_xlim()
    y_start, y_end = ax.get_ylim()
    ax.text(
        x_start + (x_end - x_start) * 0.1,
        y_start + (y_end - y_start) * 0.9,
        f"{label}={s:.3f}{asterisk}",
        va="center",
        fontsize=asterisk_fontsize,
    )
    return


def main():
    """测试绘图函数的功能"""
    from pathlib import Path

    # 测试数据
    data1 = np.random.normal(size=100)
    data2 = 2 * data1 + 4 * np.random.normal(size=100)
    # 测试函数
    fig, ax = plt.subplots(1, 1, figsize=(3, 3))
    plot_correlation_figure(
        data1,
        data2,
        ax=ax,
        stats_method="spearman",
        ci=False,
        dots_color="green",
        dots_size=5,
        line_color="b",
        title_name="this is a title",
        title_fontsize=10,
        title_pad=10,
        x_label_name="",
        x_label_fontsize=10,
        x_tick_fontsize=10,
        x_tick_rotation=0,
        x_major_locator=None,
        x_max_tick_to_value=None,
        x_format="normal",  # normal, sci, 1f, percent
        y_label_name="",
        y_label_fontsize=10,
        y_tick_fontsize=10,
        y_tick_rotation=0,
        y_major_locator=None,
        y_max_tick_to_value=None,
        y_format="1f",
        asterisk_fontsize=7,
    )
    # 测试输出
    save_dir = Path(__file__).parent / "tests_output"
    save_dir.mkdir(exist_ok=True)
    save_path = save_dir / "test.png"
    fig.savefig(save_path, dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
