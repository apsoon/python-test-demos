from src.test_case_token.common import global_value

"""
公司测试用例
"""


class TestTag:

    def test_create_tag(self):
        print("[TestTag] ===== test_create_tag >>> 测试了创建Tag, token 为[%s]" % global_value.TOKEN)
        assert 1 == 1
