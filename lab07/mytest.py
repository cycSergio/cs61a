# _*_ coding: utf-8 _*_
# @Time : 2022/2/11 22:32
# @Author : 进击的大饼
# @File : mytest 
# @Project : lab07

class Link:
    empty = ()

    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
