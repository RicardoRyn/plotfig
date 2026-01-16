import matplotlib.pyplot as plt
import numpy as np

from plotfig import plot_brain_surface_figure

fig, ax = plt.subplots()
plot_data = {"lh_V1": 1}

ax = plot_brain_surface_figure(plot_data)
fig.savefig("./test.png")

print(np.random.randint(0, 10))
