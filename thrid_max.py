# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		thrid_max.py
# CreateDate: 		2020-07-28 22:29:40
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-07-28 22:29:40
# SoftWare:			Visual Studio Code
# Description: 		LeetCode第414题：第三大的数	
# -------------------------------------------------
'''


def thrid_max(nums: list) -> int:
    channel = {"first": 0, "second": 0, "thrid": 0}

# 小顶堆堆化函数
def heap(nums):
    
