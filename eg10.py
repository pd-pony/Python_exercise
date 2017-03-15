#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg10.py
# @Software: PyCharm
"""
题目：暂停一秒输出，并格式化当前时间。
"""
import time

#输入当期时间
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

#暂停1s输出
time.sleep(3)

#输入当期时间
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

