## 1.3.3 (2025-07-29)

### Fix

- **bar**: handle empty significance plot without error

## [1.4.0](https://github.com/RicardoRyn/plotfig/compare/1.3.3...v1.4.0) (2025-07-30)


### Features

* **bar:** support color transparency adjustment via `color_alpha` argument ([530980d](https://github.com/RicardoRyn/plotfig/commit/530980dc346a338658d8333bb274004fcaac8d7d))


### Documentation

* **announce:** change default content of main.html ([01d73d1](https://github.com/RicardoRyn/plotfig/commit/01d73d19e2ea733ee8184a50158107e349727509))
* **announce:** remove main.html file ([09c3cde](https://github.com/RicardoRyn/plotfig/commit/09c3cde56f8d27690e9eea1250c14152508046c7))
* **bar:** add usage example for `color_alpha` ([303e2a3](https://github.com/RicardoRyn/plotfig/commit/303e2a39d29e516ebded6504ba04a357d8428630))

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
