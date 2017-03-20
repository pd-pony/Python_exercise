#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg21.py
# @Software: PyCharm
"""
打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
"""
#分析：以中间行为分界进行解析
from sys import stdout
#上半部
for i in range(4):
    #对称左边
    for j in range(2-i+1):
        stdout.write(' ')
    #对称右边
    for k in range(2*i+1):
        stdout.write('*')
    print()

#下半部
for i in range(3):
    # 对称左边
    for j in range(i+1):
        stdout.write(' ')
    # 对称右边
    for k in range(4-2*i+1):
        stdout.write('*')
    print()