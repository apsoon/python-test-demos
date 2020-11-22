import pytest

from src.test_case_token.common import global_value

"""
登陆测试用例类
"""


@pytest.fixture(scope="session", autouse=True)
def login():
    print("[TestLogin] ===== test_login >>> 调用登陆测试用例")
    # 登陆获取token
    token = "token"
    global_value.TOKEN = token
    print("[TestLogin] ===== test_login >>> 当前token为[%s]" % global_value.TOKEN)
