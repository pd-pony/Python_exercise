#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg31.py
# @Software: PyCharm
"""
题目：学习使用auto定义变量的用法。
"""
num=2

def autofunc():
    num=1
    print('internal block nun=%d'%num)
    num+=1

for i in range(3):
    print('the num=%d'%num)
    num+=1
    autofunc()