import numpy as np
import matplotlib.pyplot as plt
from plotfig import plot_one_group_bar_figure

fig, ax = plt.subplots()

data1 = np.random.rand(10)
data2 = np.random.rand(10)

ax = plot_one_group_bar_figure([data1, data2], ax=ax)

fig.savefig("test.png")
