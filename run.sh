#!/bin/bash

version=$(python -c "import version; print(version.__version__)")

pip uninstall -y pip-gui-tools

python3 setup.py sdist bdist_wheel

pip install dist/pip_gui_tools-$version-py3-none-any.whl

pipuitool
