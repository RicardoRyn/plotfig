## v1.2.0 (2025-07-24)

### Feat

- **violin**: add function to plot single-group violin fig

### Fix

- **matrix**: changed return value to None

## v1.1.0 (2025-07-21)

### Feat

- **corr**: allow hexbin to show dense scatter points in correlation plot
- **bar**: support gradient color bars and now can change border color

## v1.0.0 (2025-07-03)

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
