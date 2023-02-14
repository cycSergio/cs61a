# _*_ coding: utf-8 _*_
# @Time : 2022/2/15 17:32
# @Author : 进击的大饼
# @File : mytry 
# @Project : hw05

class Aa:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __repr__(self):
        return 'Aa(' + str(self.first) + ',' + str(self.rest) + ')'
