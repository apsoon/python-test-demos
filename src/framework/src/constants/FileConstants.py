#!/usr/bin/python3

import os

from src.framework.src.constants import FileExtension

"""
文件相关常量
"""

_SRC = "src"
_FRAMEWORK = "framework"
_RESOURCE = "resource"
_CONFIG = "config"
_DATA = "data"
_PROJECT_NAME = "python-test-demos"

_cur_path = os.path.abspath(os.path.dirname(__file__))
_root_path = _cur_path[:_cur_path.find(_PROJECT_NAME) + len(_PROJECT_NAME)]
# 项目（framework这个demo）的根路径
_PROJECT_BASE_PATH = os.path.join(_root_path, _SRC, _FRAMEWORK)
# 代码根路径
_SRC_PATH = os.path.join(_PROJECT_BASE_PATH, _SRC)
# 资源根路径
_SOURCE_PATH = os.path.join(_PROJECT_BASE_PATH, _RESOURCE)
# 配置文件根路径
_CONFIG_PATH = os.path.join(_SOURCE_PATH, _CONFIG)
# 数据文件根路径
_DATA_PATH = os.path.join(_SOURCE_PATH, _DATA)

# 配置文件路径
config = os.path.join(_CONFIG_PATH, "config" + FileExtension.YAML)
