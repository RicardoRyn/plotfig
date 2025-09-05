import numpy as np
from numpy.typing import NDArray


def gen_symmetric_matrix(
    n, mode="nonneg", sparsity: float = 1.0, seed: int = 42
) -> NDArray:
    """
    生成一个对称方阵，可以指定元素范围和稀疏度。

    Args:
        n (int): 方阵的维度。
        mode (str, optional): 元素类型，"nonneg" 表示非负，"all" 表示可为负。默认为 "nonneg"。
        sparsity (float, optional): 稀疏度，取值范围 [0, 1]，1 表示全密集，0 表示全零。默认为 1.0。
        seed (int, optional): 随机种子，默认为 42。

    Raises:
        ValueError: 如果 mode 不是 "nonneg" 或 "all"。

    Returns:
        NDArray: 生成的对称方阵。
    """
    # 创建随机数生成器
    RNG = np.random.default_rng(seed=seed)
    # 生成权重矩阵上三角
    if mode == "nonneg":
        upper = np.triu(RNG.random((n, n)), k=1)
    elif mode == "all":
        upper = np.triu(RNG.uniform(-1, 1, size=(n, n)), k=1)
    else:
        raise ValueError("mode must be 'nonneg' or 'all'")
    # 稀疏化：随机生成mask
    if sparsity < 1.0:
        mask = RNG.random((n, n)) < sparsity
        mask = np.triu(mask, k=1)  # 上三角mask
        upper *= mask
    # 构造对称矩阵
    mat = upper + upper.T
    np.fill_diagonal(mat, 0.0)
    return mat


def is_symmetric_square(matrix: NDArray, tol: float = 1e-8) -> bool:
    """
    判断一个矩阵是否为对称方阵。

    Args:
        matrix (NDArray): 待判断的矩阵。
        tol (float, optional): 判断对称性的容差，默认为 1e-8。

    Returns:
        bool: 如果是对称方阵则返回 True，否则返回 False。
    """
    # 1. 检查是否为方阵
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return False

    # 2. 检查是否对称
    return np.allclose(matrix, matrix.T, atol=tol)
