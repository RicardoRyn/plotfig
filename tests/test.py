import matplotlib.pyplot as plt

from plotfig import plot_brain_surface_figure

fig, ax = plt.subplots()

plot_data = {"lh_V1": 1}

ax = plot_brain_surface_figure(plot_data, ax=ax)

fig.savefig("test.png")
