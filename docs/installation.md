# 安装

`plotfig` 支持通过包管理器安装或直接从源码中安装，要求 Python 3.11 及以上版本。

## 使用包管理器安装 (推荐)

=== "uv"

    ``` bash
    uv add plotfig
    ```

=== "pip"

    ``` bash
    pip install plotfig
    ```

## 从源码中安装

首先下载源码到某个目录（例如 `/path/to/plotfig`）：

```bash
git clone https://github.com/RicardoRyn/plotfig.git /path/to/plotfig
```

然后在您的项目目录中执行：

=== "uv"

    ``` bash
    uv add /path/to/plotfig
    ```

=== "pip"

    ``` bash
    pip install /path/to/plotfig
    ```

!!! info

    `/path/to/plotfig` 应替换为实际的路径。

## 贡献

如果您希望体验这些功能或参与 `plotfig` 的开发，可以选择以 开发模式（editable mode） 安装项目。

这种安装方式允许您对本地源码的修改立即生效，非常适合调试、开发和贡献代码。

推荐流程：

1. Fork 本仓库到您的 GitHub 账号
2. 克隆您的 Fork 到本地：
   ```bash
   git clone https://github.com/USERNAME/plotfig.git /path/to/plotfig
   ```
3. 在您的项目目录中以开发模式安装：

=== "uv"

    ``` bash
    uv add --editable /path/to/plotfig
    ```

=== "pip"

    ``` bash
    pip install -e /path/to/plotfig
    ```

!!! info

    `/path/to/plotfig` 应替换为实际的路径。

---

**欢迎提交 Issue 或 PR！**

无论是 Bug 报告、功能建议、还是文档改进。

都非常欢迎在 [Issue](https://github.com/RicardoRyn/plotfig/issues) 中提出。

也可以直接提交 [PR](https://github.com/RicardoRyn/plotfig/pulls)，一起变得更强 💪！
