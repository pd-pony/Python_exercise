#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg3.py
# @Software: PyCharm
"""
题目：题目：一个10000内的整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
"""
#简单数学思维题，判断开方之后是否为整数即可
import math
for i in range(0,10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if((pow(x,2)==i+100) and (pow(y,2)==i+268)):
        print(i)