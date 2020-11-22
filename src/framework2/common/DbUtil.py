#!/usr/bin/python3

import pymysql

"""
数据库工具类
"""


def execute(sql, db):
    mysql_config = {
        "host": "localhost",
        "username": "root",
        "password": "root"
    }
    conn = pymysql.connect(mysql_config['host'], mysql_config['username'], mysql_config['password'], db)
    cursor = conn.cursor()
    result = None
    try:
        result = cursor.execute(sql)
    finally:
        cursor.close()
        conn.close()
    return result


sql = """
SELECT j.id FROM job j 
JOIN company c ON (j.company_id=c.id AND c.name='xxx' AND c.is_del=0)
WHERE (j.name='xxx' AND j.is_del=0)
"""
