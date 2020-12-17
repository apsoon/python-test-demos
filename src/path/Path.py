import os

# 这里是一些获取路径的常用方法
print()
print("----------------- 获取文件当前工作目录的绝对路径 ------------------")
print(os.getcwd())

print()
print("----------------- 获取文件所在的绝对路径 ------------------")
print(os.path.abspath(__file__))

print()
print("----------------- 获取文件所在的绝对路径 ------------------")
print(os.path.realpath(__file__))

print()
print("----------------- 将文件的路径分成目录和文件名组成的二元元组 ------------------")
print(os.path.split(os.path.realpath(__file__)))

# 这里是怎么用
print()
print("----------------- 文件路径示例 ------------------")
root_path = os.getcwd()
print("----------------- 工作目录的路径为")
print(root_path)
fileRelatePath = "/path/Path.py"
print("----------------- 文件的相对路径为")
print(fileRelatePath)
# fileAbsPath就存储了文件的绝对路径，可以当作参数传了
fileAbsPath = root_path + fileRelatePath
print("----------------- 文件的绝对路径为")
print(fileAbsPath)

print()
print("----------------- 获取系统文件分隔符示例 ------------------")
print("当前系统的文件分隔符为 " + os.sep)
fileRelatePath = os.sep + "path" + os.sep + "Path.py"
print("文件的路径为 " + fileRelatePath)

print("----------------- BASE_DIR ------------------")
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
print(BASE_DIR)
