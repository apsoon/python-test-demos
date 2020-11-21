#!/usr/bin/python

from src.framework.constants import Api
from src.framework.utils import RequestUtil

"""
公司管理接口调用方法
"""


def create_company(data):
    """
    创建公司
    :param data: 公司数据
    :return: 创建的公司id
    """

    # 这里设置一些额外数据, 这里用area举例可能不太好
    data["area"] = "CHINA"

    # 调用创建公司接口
    result = RequestUtil.post(Api.CompanyManage.create_company, data)
    # 这里返回假数据
    return 10004


def company_detail(company_id):
    """
    获取公司详情
    :param company_id: 公司id
    :return: 公司数据
    """

    # 接口请求数据
    data = {
        "id": company_id
    }
    # 调用获取公司详情接口
    result = RequestUtil.post(Api.CompanyManage.company_detail, data)
    # 这里返回假数据
    return _get_company_demo_detail(company_id)


def _get_company_demo_detail(company_id):
    """
    示例公司假数据获取方法
    :param company_id: 公司id
    :return: 返回公司假数据
    """

    # 预置的数据
    demo_detail = {
        10001: {
            "id": 10001,
            "code": "0001",
            "name": "公司0001"
        },
        10002: {
            "id": 10002,
            "code": "0002",
            "name": "公司0002"
        },
        10003: {
            "id": 10003,
            "code": "0003",
            "name": "公司0003"
        }
    }

    if demo_detail.__contains__(company_id):
        return demo_detail[company_id]

    return None
