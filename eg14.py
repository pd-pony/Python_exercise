#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg14.py
# @Software: PyCharm
"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，60分以下的用C表示
"""
score=int(input('input score:\n'))
if score>=90:
    grade='A'
elif score<90 and score>=60:
    grade='B'
else:
    grade='C'

print('%d belongs to %s'%(score,grade))