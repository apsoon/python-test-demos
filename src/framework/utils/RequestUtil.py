#!/usr/bin/python

# import requests

"""
request请求工具类


"""


def post(url, data=None, header=None):
    """
    发送POST请求
    :param url: 请求地址
    :param data: 数据
    :param header: header
    :return: Response.text 这里一般都会对返回体做一层分装，这里就略过了。。。
    """

    """
    # 这里注视掉不真正调用
    if header is None:
        # 这里设置默认header信息
        pass

    # 调用post请求
    result = requests.post(url=url, json=data, header=header)
    
    # 接口状态调用
    if result.status_code != 200:
        print("调用接口失败, 错误码为：["+ result.status_code +"]")
        raise Exception("接口调用失败")
    return result.text
    """

    # 打印语句代表接口调用了
    print("调用接口：[" + url + "]，data为：[" + data + "]，json为：[" + json + "]，method为：[POST]")
