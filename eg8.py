#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg8.py
# @Software: PyCharm
"""
题目：输出 9*9 乘法口诀表。
"""
for i in range(10):
    for j in range(1,i+1):
        print("%d*%d=%d" %(i,j,i*j))