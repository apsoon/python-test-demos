#!/usr/bin/python3

import pymysql

"""
数据库工具类
"""

# 数据库连接信息
data_base_info = {

}


def _get_connect():
    """
    获取数据库连接
    :return:
    """
    return pymysql.connect(data_base_info['host'], data_base_info['username'], data_base_info['password'])


def _get_cursor(conn: pymysql.Connection):
    """

    :param conn:
    :return:
    """
    return conn.cursor()


def execute_sql(sql):
    """
    数据库执行方法
    :param sql: sql
    :return:  结果
    """

    conn = None  # 数据库连接
    cursor = None  # 游标
    result = None  # 结果

    try:
        conn = _get_connect()
        cursor = _get_cursor(conn)
        result = cursor.execute(sql)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
    return result
