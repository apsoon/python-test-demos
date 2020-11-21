#!/usr/bin/python
from src.framework.constants import Api
from src.framework.utils import RequestUtil

"""
地址管理接口调用方法
"""


# 创建公司
def create_address(data):
    RequestUtil.post(Api.AddressManage.create_address, data)
    pass


# 获取公司详情
def address_detail(address_id):
    pass
