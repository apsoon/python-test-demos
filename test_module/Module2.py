import json


# 创建公司的api调用封装
def create_company(addr_id, company_name):
    print("创建公司成功。。。")


# 获取地址id的封装
def get_id_from_file(file_name):
    file = open("./" + file_name + ".json", "r")
    data = json.loads(file.read())
    file.close()
    return data["addr_id"]


# 测试创建公司
def test_create_company():
    company_name = "茶花女"
    create_company(get_id_from_file("addr_id"), company_name)


# 调用测试用例
test_create_company()
