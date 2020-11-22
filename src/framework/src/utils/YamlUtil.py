#!/usr/bin/python3

import yaml

from src.framework.src.constants import FileConstants

"""
配置文件操作工具类
"""

_MYSQL = "mysql"


def get_mysql_config():
    """
    获取mysql的配置
    :return: 获取mysql配置，字典
    """
    return get_config(_MYSQL)


def get_config(key):
    """
    获取配置文件
    :param key: key
    :return: 配置文件里面的配置，字典
    """

    fs = open(FileConstants.config)
    data = yaml.load(fs, Loader=yaml.FullLoader)
    if not data.__contains__(key):
        print("key [" + key + "], 不存在")
    fs.close()
    return data[key]
