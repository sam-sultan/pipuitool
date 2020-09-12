#!/bin/bash

pip uninstall -y pip-gui-tools

python3 setup.py sdist bdist_wheel

pip install dist/pip_gui_tools-0.0.5-py3-none-any.whl

pipuitool
