#!/usr/bin/python3
from src.framework.src.constants import Api
from src.framework.src.utils import RequestUtil

"""
地址管理接口调用方法
"""


def create_address(data):
    """
    创建地址
    :param data: 创建地址数据
    :return: id
    """

    result = RequestUtil.post(Api.AddressManage.create_address, data)
    return 10001


def address_detail(address_id):
    """
    获取地址详情
    :param address_id: 地址id
    :return: 地址详情
    """

    # 接口请求数据
    data = {
        "id": address_id
    }
    # 调用接口
    result = RequestUtil.post(Api.AddressManage.address_detail, data)
    # 这里返回假数据
    return _get_address_demo_detail(address_id)


def _get_address_demo_detail(address_id):
    """
    示例地址假数据获取方法
    :param address_id: 地址id
    :return: 返回地址假数据
    """

    # 地址假数据
    demo_details = {
        10001: {
            "id": 10001,
            "code": "0001",
            "name": "地址0001"
        },
        10002: {
            "id": 10002,
            "code": "0002",
            "name": "地址0002"
        },
        10003: {
            "id": 10003,
            "code": "0003",
            "name": "地址0003"
        }
    }

    if demo_details.__contains__(address_id):
        return demo_details[address_id]

    return None
