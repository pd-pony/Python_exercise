#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg29.py
# @Software: PyCharm
"""
题目：求一个3*3矩阵对角线元素之和。
"""
if __name__=='__main__':
    a=[]
    sum=0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input('input number：\n')))
    for i in range(3):
        sum+=a[i][i]
    print(sum)