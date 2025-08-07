# Changelog

## [1.5.0](https://github.com/RicardoRyn/plotfig/compare/v1.4.0...v1.5.0) (2025-08-07)


### Features

* **bar:** support combining multiple statistical test methods ([34b6960](https://github.com/RicardoRyn/plotfig/commit/34b6960ff705468154bc5fbf75b9917ba8ac64fd))
* **connec:** Add `line_color` parameter to customize connection line colors ([e4de41e](https://github.com/RicardoRyn/plotfig/commit/e4de41effe495767cde0980ce5e2cee458d8b3a8))


### Code Refactoring

* **bar:** mark string input for `test_method` as planned for deprecation ([e56d6d7](https://github.com/RicardoRyn/plotfig/commit/e56d6d7b79104b6079619b73158e21ee284a5304))

## [1.4.0](https://github.com/RicardoRyn/plotfig/compare/v1.3.3...v1.4.0) (2025-07-30)


### Features

* **bar:** support color transparency adjustment via `color_alpha` argument ([530980d](https://github.com/RicardoRyn/plotfig/commit/530980dc346a338658d8333bb274004fcaac8d7d))

## [1.3.3](https://github.com/RicardoRyn/plotfig/compare/v1.3.2...v1.3.3) (2025-07-29)


### Bug Fixes

* **bar**: handle empty significance plot without error

## [1.3.2](https://github.com/RicardoRyn/plotfig/compare/v1.3.1...v1.3.2) (2025-07-29)


### Bug Fixes

* **deps**: use the correct version of surfplot

## [1.3.1](https://github.com/RicardoRyn/plotfig/compare/v1.3.0...v1.3.1) (2025-07-28)


### Bug Fixes

* **deps**: update surfplot dependency info to use GitHub version

## [1.3.0](https://github.com/RicardoRyn/plotfig/compare/v1.2.1...v1.3.0) (2025-07-28)


### Features

* **bar**: add one-sample t-test functionality


### Bug Fixes

* **bar**: isolate random number generator inside function


### Code Refactoring

* **surface**: unify brain surface plotting with new plot_brain_surface_figure
* **bar**: replace print with warnings.warn
* **bar**: rename arguments in plot_one_group_bar_figure
* **tests**: remove unused tests folder

## [1.2.1](https://github.com/RicardoRyn/plotfig/compare/v1.2.0...v1.2.1) (2025-07-24)


### Bug Fixes

* **bar**: rename `y_lim_range` to `y_lim` in `plot_one_group_bar_figure`

## [1.2.0](https://github.com/RicardoRyn/plotfig/compare/v1.1.0...v1.2.0) (2025-07-24)


### Features

* **violin**: add function to plot single-group violin fig


### Bug Fixes

* **matrix**: changed return value to None

## [1.1.0](https://github.com/RicardoRyn/plotfig/compare/v1.0.0...v1.1.0) (2025-07-21)


### Features

* **corr**: allow hexbin to show dense scatter points in correlation plot
* **bar**: support gradient color bars and now can change border color

## 1.0.0 (2025-07-03)


### Features

* **bar**: support plotting single-group bar charts with statistical tests
* **bar**: support plotting multi-group bars charts
* **corr**: support combined sactter and line correlation plots
* **matrix**: support plotting matrix plots (i.e. heatmaps)
* **surface**: support brain region plots for human, chimpanzee and macaque
* **circos**: support brain connectivity circos plots
* **connection**: support glass brain connectivity plots


### Bug Fixes

* **surface**: fix bug where function did not retrun fig only
* **surface**: fix bug where brain region with zero values were not displayed


### Code Refactoring

* **src**: refactor code for more readability and maintainability
