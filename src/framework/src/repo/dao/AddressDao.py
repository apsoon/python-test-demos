#!/usr/bin/python3

from src.framework.src.utils import DBUtil


def get_addr_by_code(code):
    """
    通过code获取地址的方法
    :param code:
    :return:
    """

    # 通过code查询数据sql
    sql = "SELECT * FROM t_company WHERE code='%s'" % code
    return DBUtil.execute_sql(sql)
