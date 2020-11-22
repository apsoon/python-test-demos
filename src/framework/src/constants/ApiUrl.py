#!/usr/bin/python3

"""
接口地址常量类
"""


class Base:
    # 域名
    DOMAIN = "http://demo.com"


class User:
    # 基础路径
    _BASE_URL = Base.DOMAIN + "/user"
    # 登陆
    LOGIN = _BASE_URL + "/login"


# 公司管理相关接口path


class CompanyManage:
    # 基础路径
    _BASE_URL = Base.DOMAIN + "/company"
    # 创建公司
    CREATE_COMPANY = _BASE_URL + "/create"
    # 修改公司
    UPDATE_COMPANY = _BASE_URL + "/modify"
    # 获取公司列表
    COMPANY_LIST = _BASE_URL + "/list"
    # 删除公司
    DELETE_COMPANY = _BASE_URL + "/delete"
    # 获取公司详情
    COMPANY_DETAIL = _BASE_URL + "/detail"

    def __init__(self):
        pass


# 地址管理相关接口path
class AddressManage:
    # 基础路径
    _BASE_URL = Base.DOMAIN + "/address"
    # 创建地址
    CREATE_ADDRESS = _BASE_URL + "/create"
    # 修改地址
    UPDATE_ADDRESS = _BASE_URL + "/modify"
    # 获取地址列表
    ADDRESS_LIST = _BASE_URL + "/list"
    # 删除地址
    DELETE_ADDRESS = _BASE_URL + "/delete"
    # 获取地址详情
    ADDRESS_DETAIL = _BASE_URL + "/detail"

    def __init__(self):
        pass
