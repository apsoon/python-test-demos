from src.test_case_token.common import global_value

"""
公司测试用例
"""


class TestAddress:

    def test_create_address(self):
        print("[TestAddress] ===== test_create_address >>> 测试了创建地址, token 为[%s]" % global_value.TOKEN)
        assert 1 == 1
