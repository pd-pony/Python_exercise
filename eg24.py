#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg24.py
# @Software: PyCharm
"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
a=int(input('请输入一个数字：\n'))
x=str(a)
flag=True

for i in range(int(len(x)/2+1)):
    if x[i]!=x[-i-1]:
        flag=False
        break

if flag:
    print('%d是一个回文数！'%a)
else:
    print('%d不是一个回文数！' % a)