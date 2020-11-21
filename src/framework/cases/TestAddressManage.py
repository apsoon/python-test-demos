#!/usr/bin/python

from src.framework.apifuncs import AddressManage

"""
地址管理测试用例
"""


def test_create_address():
    """
    创建地址测试用例
    :return: 
    """

    # 测试创建地址的数据
    data = {
        "code": "0004",
        "name": "地址0004"
    }
    # 调用接口
    result = AddressManage.create_address(data)
    # 断言
    assert result == 10004


def test_company_detail():
    """
    修改地址测试用例
    :return: 
    """

    # 调用接口
    result = AddressManage.address_detail(10003)
    # 断言
    assert result["name"] == "地址0003"
