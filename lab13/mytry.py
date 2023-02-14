# _*_ coding: utf-8 _*_
# @Time : 2022/3/28 16:22
# @Author : 进击的大饼
# @File : mytry 
# @Project : lab13
try:
    x = float("abc123")
    print("数据类型转换完成")
except IOError:
    print("This code caused an IOError")
except ValueError:
    print("This code caused an ValueError")