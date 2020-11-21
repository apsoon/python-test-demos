#!/usr/bin/python

import os

"""
接口地址常量类
"""


class Base:
    # 域名
    domain = "http://demo.com"


# 公司管理相关接口path
class CompanyManage:
    # 基础路径
    _base_url = Base.domain + os.sep + "company"
    # 创建公司
    create_company = _base_url + os.sep + "create"
    # 修改公司
    update_company = _base_url + os.sep + "modify"
    # 获取公司列表
    company_list = _base_url + os.sep + "list"
    # 删除公司
    delete_company = _base_url + os.sep + "delete"
    # 获取公司详情
    company_detail = _base_url + os.sep + "detail"

    def __init__(self):
        pass


# 地址管理相关接口path
class AddressManage:
    # 基础路径
    _base_url = Base.domain + os.sep + "address"
    # 创建地址
    create_address = _base_url + os.sep + "create"
    # 修改地址
    update_address = _base_url + os.sep + "modify"
    # 获取地址列表
    address_list = _base_url + os.sep + "list"
    # 删除地址
    delete_address = _base_url + os.sep + "delete"
    # 获取地址详情
    address_detail = _base_url + os.sep + "detail"

    def __init__(self):
        pass
