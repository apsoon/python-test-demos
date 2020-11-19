import json


# addr接口的调用分装 返回地址id
def create_addr():
    return 12312312312312


# 保存id到文件的方法
def save_id_to_file(file_name, addr_id):
    file = open("./" + file_name + ".json", "w")
    file.write(json.dumps({"addr_id": addr_id}))
    file.close()


# 测试地址接口
def test_api1():
    addr_id = create_addr()
    save_id_to_file("addr_id", addr_id)


# 调用测试用例
test_api1()
