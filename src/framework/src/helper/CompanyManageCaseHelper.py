#!/usr/bin/python3

"""
公司测试用例辅助工具
"""
from src.framework.src.repo.dao import AddressDao


def get_address_id(data):
    """
    获取地址id方法封装
    这里做一层封装，外界不用关心地址id是怎么来的，只用关心拿到地址id就可以了
    具体如何拿到地址id，在下面的方法中实现
    
    :param data: 参数
    :return: 地址id
    """

    # 这里选择从数据库中查
    return _get_address_id_from_db(data)


def _get_address_id_from_db(code):
    """
    从数据库中获取
    :param code: 地址编码
    :return: 地址id
    """
    return AddressDao.get_addr_by_code(code)


def _get_address_id_from_json(data):
    """
    从json文件中获取
    :param data: 参数
    :return: 地址id
    """
    pass


def _get_address_id_from_address_list_api(data):
    """
    从地址列表接口返回中获取
    :param data: 参数
    :return: 地址id
    """
    pass
