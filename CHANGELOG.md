## v0.3.0 (2025-07-01)

### Feat

- **brain_connection**: 现在默认不显示没有任何连接的节点
- **brain_connection**: 可为脑连接html文件截图
- **corr**: 增加show_p_value选项，可显示p值
- **bar**: 每个独立的样本点都能够指定颜色

## v0.2.1 (2025-06-13)

### Fix

- **surface**: 修复函数并非仅返回fig的bug

## v0.2.0 (2025-06-13)

### Feat

- **bar**: 增加绘制多组bar图
- **brain_surface**: 增加猕猴D99图集
- **brain_surface_plot文件为主**: 增加函数绘制黑猩猩BNA图集图
- **brain_connection_plot.py**: add brain_connection_plot.py

### Fix

- **brain_surface_plot.py**: 修复0值透明bug

### Refactor

- 重构代码，更加可读，易维护
- migrate project to src layout
- **dependency-and-env**: use uv and remove neuromaps
