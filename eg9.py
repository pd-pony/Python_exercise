#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg9.py
# @Software: PyCharm
"""
题目：暂停一秒输出。
"""
import time

myD={1:'a',2:'b'}
for key,value in dict.items(myD):
    print (key,value)
    time.sleep(1) #暂停1s