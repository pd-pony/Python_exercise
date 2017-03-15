#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg5.py
# @Software: PyCharm
"""
输入三个整数x,y,z，请把这三个数由小到大输出。
"""
#利用list
list=[]
for i in range(3):
    x=int(input('integer:\n'))
    list.append(x)
list.sort()
print(list)