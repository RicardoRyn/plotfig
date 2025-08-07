## [1.4.0](https://github.com/RicardoRyn/plotfig/compare/1.3.3...v1.4.0) (2025-07-30)


### Features

* **bar:** support color transparency adjustment via `color_alpha` argument ([530980d](https://github.com/RicardoRyn/plotfig/commit/530980dc346a338658d8333bb274004fcaac8d7d))


### Documentation

* **announce:** change default content of main.html ([01d73d1](https://github.com/RicardoRyn/plotfig/commit/01d73d19e2ea733ee8184a50158107e349727509))
* **announce:** remove main.html file ([09c3cde](https://github.com/RicardoRyn/plotfig/commit/09c3cde56f8d27690e9eea1250c14152508046c7))
* **bar:** add usage example for `color_alpha` ([303e2a3](https://github.com/RicardoRyn/plotfig/commit/303e2a39d29e516ebded6504ba04a357d8428630))

## [1.5.0](https://github.com/RicardoRyn/plotfig/compare/v1.4.0...v1.5.0) (2025-08-07)


### Features

* **bar:** support combining multiple statistical test methods ([34b6960](https://github.com/RicardoRyn/plotfig/commit/34b6960ff705468154bc5fbf75b9917ba8ac64fd))
* **connec:** Add `line_color` parameter to customize connection line colors ([e4de41e](https://github.com/RicardoRyn/plotfig/commit/e4de41effe495767cde0980ce5e2cee458d8b3a8))
* **连接:** 添加 `line_color` 参数以自定义连接线颜色 ([e4de41e](https://github.com/RicardoRyn/plotfig/commit/e4de41effe495767cde0980ce5e2cee458d8b3a8))


### Documentation

* **changelog:** fix the wrong order ([736dc68](https://github.com/RicardoRyn/plotfig/commit/736dc682aac3208bd4c1518830b7c61f5d620e28))
* **surface:** Add available atlas names in function documentation ([b2de1eb](https://github.com/RicardoRyn/plotfig/commit/b2de1ebd91e09764da996e54eddf7632eee0b6c3))
* **surface:** 在函数注释文档中补充可用atlas名字 ([b2de1eb](https://github.com/RicardoRyn/plotfig/commit/b2de1ebd91e09764da996e54eddf7632eee0b6c3))
* **web:** Change the default statement in the announcement bar ([47bfe81](https://github.com/RicardoRyn/plotfig/commit/47bfe81b2397b8122aff603fa3a00d0997fcd843))
* **web:** change web content and Welcome to Issues & PRs ([0ff2582](https://github.com/RicardoRyn/plotfig/commit/0ff25822e315e14f29ba7d1c466d3f3e429fb70b))
* **web:** Remove the self-referential link on the webpage homepage ([0b1cf14](https://github.com/RicardoRyn/plotfig/commit/0b1cf1448a765fb90a68080426acc0e07452b253))
* **web:** 删除网页主页中对该网页的跳转 ([0b1cf14](https://github.com/RicardoRyn/plotfig/commit/0b1cf1448a765fb90a68080426acc0e07452b253))
* **web:** 更改公告栏中的默认语句 ([47bfe81](https://github.com/RicardoRyn/plotfig/commit/47bfe81b2397b8122aff603fa3a00d0997fcd843))
* **web:** 更改网页上部分表述以及欢迎贡献 ([0ff2582](https://github.com/RicardoRyn/plotfig/commit/0ff25822e315e14f29ba7d1c466d3f3e429fb70b))

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
