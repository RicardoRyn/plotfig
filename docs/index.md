# plotfig

`plotfig` 是一个面向认知神经科学研究者的 Python 绘图工具包。[^1]
封装了 `matplotlib` 的各种 API，简化了复杂绘图流程。
可扩展，容 `matplotlib` 与 `seaborn`。

希望它能让你专注于数据本身而不是琐碎的图形参数调试🥵。

![plotfig](./plotfig.png)

# 功能

画图种类：
1. 单组柱状/小提琴图
1. 多组柱状图
1. 相关图
1. 矩阵图
1. 脑区图
   1. 人类Glasser脑区图
   1. 人类BNA脑区图
   1. 猕猴CHARM 5-level脑区图
   1. 猕猴CHARM 6-level脑区图
   1. 猕猴BNA脑区图
1. 连线图（circos图）
   1. 对称circos图
   1. 不对
   2. 称circos图
2. 脑连接图