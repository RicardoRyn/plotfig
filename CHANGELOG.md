## 1.3.3 (2025-07-29)

### Fix

- **bar**: handle empty significance plot without error

## 1.3.2 (2025-07-29)

### Fix

- **deps**: use the correct version of surfplot

## 1.3.1 (2025-07-28)

### Fix

- **deps**: update surfplot dependency info to use GitHub version

## 1.3.0 (2025-07-28)

### Feat

- **bar**: add one-sample t-test functionality

### Fix

- **bar**: isolate random number generator inside function

### Refactor

- **surface**: unify brain surface plotting with new plot_brain_surface_figure
- **bar**: replace print with warnings.warn
- **bar**: rename arguments in plot_one_group_bar_figure
- **tests**: remove unused tests folder

## 1.2.1 (2025-07-24)

### Fix

- **bar**: rename `y_lim_range` to `y_lim` in `plot_one_group_bar_figure`

## 1.2.0 (2025-07-24)

### Feat

- **violin**: add function to plot single-group violin fig

### Fix

- **matrix**: changed return value to None

## 1.1.0 (2025-07-21)

### Feat

- **corr**: allow hexbin to show dense scatter points in correlation plot
- **bar**: support gradient color bars and now can change border color

## 1.0.0 (2025-07-03)

### Feat

- **bar**: support plotting single-group bar charts with statistical tests
- **bar**: support plotting multi-group bars charts
- **corr**: support combined sactter and line correlation plots
- **matrix**: support plotting matrix plots (i.e. heatmaps)
- **surface**: support brain region plots for human, chimpanzee and macaque
- **circos**: support brain connectivity circos plots
- **connection**: support glass brain connectivity plots

### Fix

- **surface**: fix bug where function did not retrun fig only
- **surface**: fix bug where brain region with zero values were not displayed

### Refactor

- **src**: refactor code for more readability and maintainability
