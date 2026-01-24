# Installation

`plotfig` supports installation via package managers or directly from source, requiring Python 3.11 or higher.

## Install via Package Manager (Recommended)

=== "uv"

    ```bash
    uv add plotfig
    ```

=== "pip"

    ```bash
    pip install plotfig
    ```

## Install from Source

First, download the source code to a directory (e.g., `/path/to/plotfig`):

```bash
git clone https://github.com/RicardoRyn/plotfig.git /path/to/plotfig
```

Then execute the following in your project directory:

=== "uv"

    ```bash
    uv add /path/to/plotfig
    ```

=== "pip"

    ```bash
    pip install /path/to/plotfig
    ```

!!! info

    `/path/to/plotfig` should be replaced with the actual path.

## Contributing

If you wish to experience these features or participate in `plotfig` development, you can choose to install the project in editable mode.

This installation mode allows your modifications to the local source code to take effect immediately, making it very suitable for debugging, development, and contributing code.

Recommended workflow:

1. Fork this repository to your GitHub account
2. Clone your fork locally:
   ```bash
   git clone https://github.com/USERNAME/plotfig.git /path/to/plotfig
   ```
3. Install in editable mode in your project directory:

=== "uv"

    ```bash
    uv add --editable /path/to/plotfig
    ```

=== "pip"

    ```bash
    pip install -e /path/to/plotfig
    ```

!!! info

    `/path/to/plotfig` should be replaced with the actual path.

---

**We welcome Issues and PRs!**

Whether it's bug reports, feature suggestions, or documentation improvements.

Feel free to open an [Issue](https://github.com/RicardoRyn/plotfig/issues).

You can also submit a [PR](https://github.com/RicardoRyn/plotfig/pulls) directly to help us grow stronger 💪!
