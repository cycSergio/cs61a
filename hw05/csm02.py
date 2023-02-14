# _*_ coding: utf-8 _*_
# @Time : 2022/1/27 18:33
# @Author : 进击的大饼
# @File : csm02 
# @Project : hw05

def list_of_lists(lst):
    r = []
    for i in range(len(lst)):
        r += [[v for v in range(lst[i])]]
    return r

def stepper(num):
    def step():
        nonlocal num
        num = num + 1
        return num
    return step
