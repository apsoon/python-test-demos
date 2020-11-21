#!/usr/bin/python

from src.framework.apifuncs import CompanyManage
from src.framework.helper import CompanyManageCaseHelper

"""
公司管理测试用例
"""


# 测试创建公司
def test_create_company():
    # 获取地址id
    address_id = CompanyManageCaseHelper.get_address_id("苏州")
    # 测试创建公司的数据
    data = {
        "code": "0004",
        "name": "公司0004",
        "address_id": address_id
    }
    # 调用接口
    result = CompanyManage.create_company(data)
    # 断言
    assert result == 10004


# 测试修改公司
def test_company_detail():
    # 调用接口
    result = CompanyManage.company_detail(10003)
    # 断言
    assert result["name"] == "公司0003"
