#!/usr/bin/python3
import json

import requests
from threading import Lock

from src.framework.src import Global
from src.framework.src.apifuncs import User

"""
request请求工具类
"""

lock = Lock()


def post(url, data=None):
    """
    发送POST请求
    :param url: 请求地址
    :param data: 数据
    :return: Response.text 这里一般都会对返回体做一层分装，这里就略过了。。。
    """

    # """
    # 这里注视掉不真正调用
    header = {
        "content_type": "",  # content_type
        "token": _get_token()  # 调用方法获取token
    }

    # 调用post请求
    print("调用接口：[" + url + "]，data为：[" + data + "]，header：[" + json.dumps(header) + "]，method为：[POST]")
    result = requests.post(url=url, json=data, header=header)

    # 接口状态判断
    if result.status_code != 200:
        print("调用接口失败, 错误码为：[" + str(result.status_code) + "]")
        raise Exception("接口调用失败")
    # 获取数据体
    result_body = json.loads(result.text)
    # 请求成功断言
    assert result_body["code"] != 0

    return result_body
    # """

    # 打印语句代表接口调用了


def _get_token():
    """
    获取token方法
    :return: token
    """

    if Global.TOKEN is None:
        global lock
        lock.acquire()
        if Global.TOKEN is None:
            User.login()
        lock.release()
    return Global.TOKEN
