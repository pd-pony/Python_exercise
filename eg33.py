#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg33.py
# @Software: PyCharm
"""
题目：使用lambda来创建匿名函数。
"""
MAX=lambda x,y:(x>y)*x+(x<y)*y
MIN=lambda x,y:(x>y)*y+(x<y)*x

if __name__=='__main__':
    a=10
    b=20
    print('the larger one is %d'%MAX(a,b))
    print('the smaller one is %d'%MIN(a,b))