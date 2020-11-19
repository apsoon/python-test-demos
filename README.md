# python-test-demos

## 一些教程

- python的菜鸟教程：[菜鸟教程](https://www.runoob.com/python/python-tutorial.html)

## Some Questions

### 绝对路径相对路径问题 \[path]

### 数据库 \[mysql]

- pymysql数据库的使用可以看这个：[Python3 MySQL 数据库连接 - PyMySQL 驱动](https://www.runoob.com/python3/python3-mysql.html)

### 不同模块的数据交互 \[test_module]

不知道我的理解有没有问题，两种情况，
1. 如果是一定要用测试创建那一个地址用例返回的id
   - 如果有接口可以获取唯一的返回值，比如通过名字去差，调用接口返回，就你那种方式差不多的吧
   - 将数据存在一个地方，用的时候读取，可以生成一个文件，如json
   - 可一直接去数据库里面查
2. 如果随便取一个值
   - 调用列表接口随便取一个，取第一个可以呀
