#!/usr/bin/python33

# -------------------------- #
#      这个里面我没有调过       #
# -------------------------  #


import pymysql
from src.mysql.Model import Company
from pymysql.cursors import Cursor

# 打开数据库连接
conn = pymysql.connect("localhost", "root", "root@MySQL", "demo")

# 创建游标
cursor = conn.cursor()

# ********* 创建表
# 创建表语句
sql_create_table = """
CREATE TABLE company(
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键id',
    name VARCHAR (128) NUT NULL COMMENT '公司名称',
    addr_id BIGINT COMMENT '地址id'
) COMMENT '公司表';
"""

# 执行创建表语句
cursor.execute(sql_create_table)

# ********* 插入数据

# 单条插入 这里用对象做演示
company1 = Company(None, '公司1', 1)
sql_insert_one = "INSERT INTO compnay(name, addr_id) VALUES('%s','%s')" \
                 % (company1.name, company1.addr_id)
cursor.execute(sql_insert_one)

# 批量插入
batch_list = []  # 创建一个列表
sql_part = "('%s','%s')"
for i in range(2, 10):
    batch_list.append(('company' + str(i), i))
sql_bath_insert = "INSERT INTO company(name, addr_id) VALUES(%s,%s,%s)"
cursor.executemany(sql_bath_insert, batch_list)

# ********* 查询一条数据
sql_get_one = "SELECT * FROM company WHERE name = '%s'" % company1.name
cursor.execute(sql_get_one)
one_data = cursor.fetchone()
print(one_data)

# 关闭游标和连接
cursor.close()
conn.close()
