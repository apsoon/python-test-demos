#!/usr/bin/python3
import json

import requests

from src.framework.src import Global
from src.framework.src.constants import ApiUrl


def login():
    """
    登陆接口, 大概是这个思路，断言什么的就不写了
    :return:
    """

    data = {
        "mobile": "17500000001",  # 电话号码，假设用电话号码登陆
        "password": "dfalkj"  # 密码
    }
    request_result = requests.post(ApiUrl.User.LOGIN, json=data)
    result_body = json.loads(request_result.text)
    Global.TOKEN = result_body["data"]["token"]
