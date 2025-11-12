# Changelog

## [1.9.0](https://github.com/RicardoRyn/plotfig/compare/v1.8.1...v1.9.0) (2025-11-12)


### Features ✨

* **bar:** add one-sample t-test functionality ([00fdceb](https://github.com/RicardoRyn/plotfig/commit/00fdceb4b2b565fb33580a45f88f1ad5f5a8a258)), closes [#5](https://github.com/RicardoRyn/plotfig/issues/5)
* **bar:** allow single-group bar plots to optionally show dots ([de2a2bb](https://github.com/RicardoRyn/plotfig/commit/de2a2bb5ab846041b380cf6225002575beb0406a))
* **bar:** support color transparency adjustment via `color_alpha` argument ([530980d](https://github.com/RicardoRyn/plotfig/commit/530980dc346a338658d8333bb274004fcaac8d7d))
* **bar:** support combining multiple statistical test methods ([34b6960](https://github.com/RicardoRyn/plotfig/commit/34b6960ff705468154bc5fbf75b9917ba8ac64fd))
* **bar:** 增加函数绘制多组bar图 ([d740fbe](https://github.com/RicardoRyn/plotfig/commit/d740fbec2534fd91f660ca183323fdf014c5537a))
* **bar:** 每个独立的样本点都能够指定颜色 ([8c0f297](https://github.com/RicardoRyn/plotfig/commit/8c0f297c7a6c847e53db3ee3f2719568ff644d72))
* **bar:** 能够绘制间渐变色的bar图，设置bar边框颜色 ([02d163f](https://github.com/RicardoRyn/plotfig/commit/02d163ffbe0b0d51cb7c7b59ca7d75b71da4ed9d))
* **circos:** add support for changing node label orientation via `node_label_orientation` ([abb7746](https://github.com/RicardoRyn/plotfig/commit/abb77465b33ea91d1a23592436b27d400799995f))
* **circos:** Implement a new method for drawing circos plots ([ebf3352](https://github.com/RicardoRyn/plotfig/commit/ebf3352491566817fc6202c1a9323e9f6e8a323a))
* **connec:** Add `line_color` parameter to customize connection line colors ([e4de41e](https://github.com/RicardoRyn/plotfig/commit/e4de41effe495767cde0980ce5e2cee458d8b3a8))
* **connection:** add batch image cropping and GIF creation utilities ([f6554aa](https://github.com/RicardoRyn/plotfig/commit/f6554aaac27549428b10646d11a646b93ce389af))
* **connection:** 可为脑连接html文件截图 ([5172a89](https://github.com/RicardoRyn/plotfig/commit/5172a890cea45b3405c3fb4a2048fc0d81295c4b))
* **connection:** 增加函数绘制玻璃大脑连接图 ([43ac5e5](https://github.com/RicardoRyn/plotfig/commit/43ac5e53f92b37b03b475c95fd930cb79cbfeb45)), closes [#1](https://github.com/RicardoRyn/plotfig/issues/1)
* **connection:** 现在默认不显示没有任何连接的节点 ([25c9e0d](https://github.com/RicardoRyn/plotfig/commit/25c9e0de1dd89ccec9755a2b365f1746778cf8ee)), closes [#2](https://github.com/RicardoRyn/plotfig/issues/2)
* **corr:** 在绘制相关点线图时，允许用正六边形展示大量散点的分布密度 ([8e25741](https://github.com/RicardoRyn/plotfig/commit/8e25741fa2337eb8e356f4ae5467ac782b2f0311))
* **corr:** 现在可以手动选择是否显示p值 ([d93e719](https://github.com/RicardoRyn/plotfig/commit/d93e71946cb802b949097e0d5b5fb560e561b05b))
* **surface:** 增加函数绘制猕猴D99图集的脑区图 ([ae33f94](https://github.com/RicardoRyn/plotfig/commit/ae33f94319aa7e4fcb849c11624523da01cbb6ab))
* **surface:** 增加函数绘制黑猩猩BNA图集脑图 ([95aaae1](https://github.com/RicardoRyn/plotfig/commit/95aaae12cf0b9b5c43a7259ecd39dbffdefab515))
* **utils:** Add several utility functions ([b59f2a4](https://github.com/RicardoRyn/plotfig/commit/b59f2a49a6683e8ce942f47a2adc2a79a94e6f84))
* **violin:** add function to plot single-group violin fig ([5c15b21](https://github.com/RicardoRyn/plotfig/commit/5c15b2172ab6df3eb40722f33374abcc606b9be5))
* **violin:** add function to plot single-group violin fig ([8b2884b](https://github.com/RicardoRyn/plotfig/commit/8b2884bdb7eb2a839c46e673e3f29901ec433722))
* **连接:** 添加 `line_color` 参数以自定义连接线颜色 ([e4de41e](https://github.com/RicardoRyn/plotfig/commit/e4de41effe495767cde0980ce5e2cee458d8b3a8))


### Bug Fixes 🔧

* **bar:** fix bug causing multi_bar plot failure ([a797006](https://github.com/RicardoRyn/plotfig/commit/a797006ed7b0598f65ff14f29d1c4c0280b1d811))
* **bar:** fix the statistic line color not displaying as expected ([51489d4](https://github.com/RicardoRyn/plotfig/commit/51489d4231711f756e24203dd25b70e8128fc89f))
* **bar:** handle empty significance plot without error ([a048ef2](https://github.com/RicardoRyn/plotfig/commit/a048ef272e40cdc85be99adcb4dfc11911abf964))
* **bar:** isolate random number generator inside function ([a423c90](https://github.com/RicardoRyn/plotfig/commit/a423c90a3ba6ecdd0950ca10de6e61e9bb94fd64))
* **bar:** remove leftover debug print in bar functions ([37f6f4c](https://github.com/RicardoRyn/plotfig/commit/37f6f4cfe55ed7ad0578040838f09f5966ce89cf))
* **bar:** rename `y_lim_range` to `y_lim` in `plot_one_group_bar_figure` ([8d18d3a](https://github.com/RicardoRyn/plotfig/commit/8d18d3ad24708c0de621cf0fddc7e3382992895c))
* **circos:** prevent type warning from type annotations ([b3552da](https://github.com/RicardoRyn/plotfig/commit/b3552dafd21fe72d9a294e0a52b8dc286d6a108e))
* **connec:** Fix color bug caused by integer values ([b104c1f](https://github.com/RicardoRyn/plotfig/commit/b104c1f985c4aeaf1576c716fc1f0b7725774e26))
* **connec:** fix issue with line_color display under color scale ([83d46d7](https://github.com/RicardoRyn/plotfig/commit/83d46d7031c49a455ab2648a92193ae5278750f4))
* **deps:** update surfplot dependency info to use GitHub version ([de4ad0c](https://github.com/RicardoRyn/plotfig/commit/de4ad0ce889b418a788659e6f700eebc34a02a33))
* **deps:** use the correct version of surfplot ([7467c20](https://github.com/RicardoRyn/plotfig/commit/7467c200f46af37a7ad0cac6aef464d1e24d9ef8))
* **matrix:** 改成返回None ([b7d1b8d](https://github.com/RicardoRyn/plotfig/commit/b7d1b8d8cabbc0e57bd3245baccbcb71a5edfda8))
* **surface:** 修复函数并非仅返回fig的bug ([e0eb9f7](https://github.com/RicardoRyn/plotfig/commit/e0eb9f7fc2fba3ab02ca880c012445f22fd6c22d))
* **surface:** 修复当值为0的情况下，脑区不显示的bug ([ba792de](https://github.com/RicardoRyn/plotfig/commit/ba792dee52827fa5643adc48934e2155e7dcd1ad))


### Code Refactoring ♻️

* **bar:** mark string input for `test_method` as planned for deprecation ([e56d6d7](https://github.com/RicardoRyn/plotfig/commit/e56d6d7b79104b6079619b73158e21ee284a5304))
* **bar:** Remove the legacy `plot_one_group_violin_figure_old` function ([6d1316d](https://github.com/RicardoRyn/plotfig/commit/6d1316d3050279f849d5c941ff6280c0ce419145))
* **bar:** rename arguments in plot_one_group_bar_figure ([22a19cb](https://github.com/RicardoRyn/plotfig/commit/22a19cb35b46b334ee0498b740d085f3a0591dc8))
* **bar:** replace print with warnings.warn ([3560d64](https://github.com/RicardoRyn/plotfig/commit/3560d64bf41237cbbc9311eb380665133b803d7b))
* **bar:** 将 `test_method` 的字符串输入标记为即将弃用 ([e56d6d7](https://github.com/RicardoRyn/plotfig/commit/e56d6d7b79104b6079619b73158e21ee284a5304))
* **circos:** Temporarily disable circos plot ([a96bb09](https://github.com/RicardoRyn/plotfig/commit/a96bb09cc799ce34785146f6bd855631ae1ad73a))
* **corr/matrix:** function now returns Axes object ([e47cada](https://github.com/RicardoRyn/plotfig/commit/e47cada18a411fe28f7dc8a6ef62dea00acd3888))
* **corr:** change default ax title font size in correlation plots to 12 ([5aab9fe](https://github.com/RicardoRyn/plotfig/commit/5aab9fe082f05894379c90b7e7a4a5a3a4739c49))
* **src:** 重构代码，更加可读，易维护 ([d50e40d](https://github.com/RicardoRyn/plotfig/commit/d50e40d45a20b0c355553f1634eac9bdcca74d39))
* **surface:** Deprecate old functions ([d90dc92](https://github.com/RicardoRyn/plotfig/commit/d90dc927731cd369d2ac1cc0939556b13d54158c))
* **surface:** unify brain surface plotting with new plot_brain_surface_figure ([b566e23](https://github.com/RicardoRyn/plotfig/commit/b566e23cf435197dc4ca4da418f09cdc8641829d))
* **tests:** remove unused tests folder ([b4a2b69](https://github.com/RicardoRyn/plotfig/commit/b4a2b697ed9d5c976bf3cf5858f67d7033cc3aa3))

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
