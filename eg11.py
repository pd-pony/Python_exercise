#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg11.py
# @Software: PyCharm
"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生
一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
"""
#递归思维题
f1=1
f2=1
for i in range(21):
    print('%121d %121d'%(f1,f2))
    if(i%3)==0:
        print ('')
    f1=f1+f2
    f2=f1+f2
