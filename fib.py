# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		fib.py
# CreateDate: 		2021-02-02 18:49:25
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-02-02 18:49:25
# SoftWare:			Visual Studio Code
# Description: 		leetcode第509题： 斐波那契数	
# -------------------------------------------------
'''
# 传统递归 
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n -1) + fib(n - 2)

n = 4
ret = fib(n)
print(ret)