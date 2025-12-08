# Changelog

## [1.13.0](https://github.com/RicardoRyn/plotfig/compare/v1.12.1...v1.13.0) (2025-12-08)


### Features ✨

* **bar:** add customizable y_base and interval for significance annotations ([b544985](https://github.com/RicardoRyn/plotfig/commit/b544985ac29208885c9ef24d80c30bd17ce25e05)), closes [#61](https://github.com/RicardoRyn/plotfig/issues/61)

## [1.12.1](https://github.com/RicardoRyn/plotfig/compare/v1.12.0...v1.12.1) (2025-11-24)


### Code Refactoring ♻️

* **brain_connection:** reorganize imports and improve gif generation ([790f43b](https://github.com/RicardoRyn/plotfig/commit/790f43be2ffb29f4892d8eea32dcc298e745d55e))

## [1.12.0](https://github.com/RicardoRyn/plotfig/compare/v1.11.0...v1.12.0) (2025-11-23)


### Features ✨

* **matrix:** add xlabel and ylabel parameters for axis labels ([2bea2b0](https://github.com/RicardoRyn/plotfig/commit/2bea2b0338bbc13a8186592559b11bc081a999e2)), closes [#56](https://github.com/RicardoRyn/plotfig/issues/56)

## [1.11.0](https://github.com/RicardoRyn/plotfig/compare/v1.10.0...v1.11.0) (2025-11-22)


### Features ✨

* **correlation:** add axis limits ([0484b2b](https://github.com/RicardoRyn/plotfig/commit/0484b2bb81018ead5d253ead263dddd7f716291f)), closes [#53](https://github.com/RicardoRyn/plotfig/issues/53)

## [1.10.0](https://github.com/RicardoRyn/plotfig/compare/v1.9.0...v1.10.0) (2025-11-19)


### Features ✨

* **data:** add human and macaque flat brain surface data ([86c56b6](https://github.com/RicardoRyn/plotfig/commit/86c56b6d556f62e087ff37cb515c927596f83afe))
* **surface:** add flat surface support and sulcal data ([fd64707](https://github.com/RicardoRyn/plotfig/commit/fd6470774b83fd97de96fba3fc60e73cc56fa1e0))

## [1.9.0](https://github.com/RicardoRyn/plotfig/compare/v1.8.1...v1.9.0) (2025-11-12)


### Features ✨

* **connection:** add batch image cropping and GIF creation utilities ([f6554aa](https://github.com/RicardoRyn/plotfig/commit/f6554aaac27549428b10646d11a646b93ce389af))

## [1.8.1](https://github.com/RicardoRyn/plotfig/compare/v1.8.0...v1.8.1) (2025-10-29)


### Bug Fixes 🔧

* **bar:** fix the statistic line color not displaying as expected ([25338dd](https://github.com/RicardoRyn/plotfig/commit/25338dd2322b9bb88297b44a22c67a6b0d92a4cf))

## [1.8.0](https://github.com/RicardoRyn/plotfig/compare/v1.7.0...v1.8.0) (2025-09-10)


### Features ✨

* **circos:** add support for changing node label orientation via `node_label_orientation` ([abb7746](https://github.com/RicardoRyn/plotfig/commit/abb77465b33ea91d1a23592436b27d400799995f))


### Bug Fixes 🔧

* **bar:** remove leftover debug print in bar functions ([37f6f4c](https://github.com/RicardoRyn/plotfig/commit/37f6f4cfe55ed7ad0578040838f09f5966ce89cf))

## [1.7.0](https://github.com/RicardoRyn/plotfig/compare/v1.6.1...v1.7.0) (2025-09-09)


### Features ✨

* **bar:** allow single-group bar plots to optionally show dots ([de2a2bb](https://github.com/RicardoRyn/plotfig/commit/de2a2bb5ab846041b380cf6225002575beb0406a))

## [1.6.1](https://github.com/RicardoRyn/plotfig/compare/v1.6.0...v1.6.1) (2025-09-07)


### Bug Fixes 🔧

* **circos:** prevent type warning from type annotations ([b3552da](https://github.com/RicardoRyn/plotfig/commit/b3552dafd21fe72d9a294e0a52b8dc286d6a108e))

## [1.6.0](https://github.com/RicardoRyn/plotfig/compare/v1.5.1...v1.6.0) (2025-09-06)


### Features ✨

* **circos:** Implement a new method for drawing circos plots ([ebf3352](https://github.com/RicardoRyn/plotfig/commit/ebf3352491566817fc6202c1a9323e9f6e8a323a))
* **utils:** Add several utility functions ([b59f2a4](https://github.com/RicardoRyn/plotfig/commit/b59f2a49a6683e8ce942f47a2adc2a79a94e6f84))


### Bug Fixes 🔧

* **bar:** fix bug causing multi_bar plot failure ([a797006](https://github.com/RicardoRyn/plotfig/commit/a797006ed7b0598f65ff14f29d1c4c0280b1d811))
* **connec:** Fix color bug caused by integer values ([b104c1f](https://github.com/RicardoRyn/plotfig/commit/b104c1f985c4aeaf1576c716fc1f0b7725774e26))


### Code Refactoring ♻️

* **circos:** Temporarily disable circos plot ([a96bb09](https://github.com/RicardoRyn/plotfig/commit/a96bb09cc799ce34785146f6bd855631ae1ad73a))
* **corr/matrix:** function now returns Axes object ([e47cada](https://github.com/RicardoRyn/plotfig/commit/e47cada18a411fe28f7dc8a6ef62dea00acd3888))
* **corr:** change default ax title font size in correlation plots to 12 ([5aab9fe](https://github.com/RicardoRyn/plotfig/commit/5aab9fe082f05894379c90b7e7a4a5a3a4739c49))
* **surface:** Deprecate old functions ([d90dc92](https://github.com/RicardoRyn/plotfig/commit/d90dc927731cd369d2ac1cc0939556b13d54158c))

## [1.5.1](https://github.com/RicardoRyn/plotfig/compare/v1.5.0...v1.5.1) (2025-08-11)


### Bug Fixes

* **connec:** fix issue with line_color display under color scale ([83d46d7](https://github.com/RicardoRyn/plotfig/commit/83d46d7031c49a455ab2648a92193ae5278750f4))


### Code Refactoring

* **bar:** Remove the legacy `plot_one_group_violin_figure_old` function ([6d1316d](https://github.com/RicardoRyn/plotfig/commit/6d1316d3050279f849d5c941ff6280c0ce419145))

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
