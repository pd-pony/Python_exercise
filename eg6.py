#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg6.py
# @Software: PyCharm
"""
题目：斐波那契数列。
"""
#递归
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input("请输入一个整数：\n"))
print(fib(n))