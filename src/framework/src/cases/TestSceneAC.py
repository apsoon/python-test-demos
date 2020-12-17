from src.framework.src.apifuncs import CompanyManageFuncs, AddressManageFuncs
from src.framework.src.helper import CompanyManageCaseHelper


def TestAcDependency():
    # step 1 创建地址
    # 测试创建地址的数据
    data = {
        "code": "0004",
        "name": "地址0004"
    }
    # 调用接口
    result = AddressManageFuncs.create_address(data)

    # step 2 创建公司
    # 获取地址id
    address_id = CompanyManageCaseHelper.get_address_id("苏州")
    # 测试创建公司的数据
    data = {
        "code": "0004",
        "name": "公司0004",
        "address_id": address_id
    }
    # 调用接口
    result = CompanyManageFuncs.create_company(data)
    pass
