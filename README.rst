plotfig 简介
============

``plotfig`` 是一个用于认知神经领域科研绘图的 Python 包。

.. image:: https://imgur.com/3CEDdxc.png
   :alt: Plot_figure
   :align: center

使用示例见 ``example.ipynb``。

主要包括图的种类：

1. 单组 bar 图
2. 单组小提琴图
3. 矩阵图
4. 点线相关图
5. 脑图
   1. 人类 Glasser 脑区图
   2. 人类 BNA 脑区图
   3. 猕猴 CHARM5 脑区图
   4. 猕猴 CHARM6 脑区图
   5. 猕猴 BNA 脑区图
6. 圈状图（circos 图）
   1. 对称 circos 图
   2. 不对称 circos 图
7. 大脑连接图
   1. 猕猴大脑连接图


依赖
====

- ``numpy``
- ``pandas``
- ``matplotlib``
- ``scipy``
- ``nibabel``
- ``surfplot``
- ``mne-connectivity``
- ``plotly``


安装
====

通过 ``pip`` 安装：

.. code-block:: bash

   pip install plotfig

