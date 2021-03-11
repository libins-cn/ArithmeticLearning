# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		maximum_product.py
# CreateDate: 		2021-02-20 18:48:36
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-02-20 18:48:36
# SoftWare:			Visual Studio Code
# Description: 		LeetCode第628题：三个数的最大乘积	
# -------------------------------------------------
'''

def maximum_product(nums):
    maxnum = 1001
    positives = [0] * maxnum
    negatives = [0] * maxnum
    for num in nums:
        if num >= 0:
            positives[num] += 1 
        if num < 0:
            negatives[-1 * num] += 1 
    # 取正数前3个值
    positive = []
    negative = []
    p = maxnum 
    n = maxnum 
    while p >= 0  and len(positive) < 3:
        if positives[p] > 0:
            positive.append(p)
            positives[p] -=1
            continue
        p -= 1 
    while n >= 0  and len(negative) < 2:
        if negative[n] > 0:
            negative.append(n)
            negative[n] -=1
            continue
        n -= 1 
    if len(negative) == 0:
        return positive[0] * positive[1] * positive[2]
    if len(negative) == 2:
        max1 = 1 
        for num in positive: # 三个
            max1 *= num 
        max2 = negative[0] * negative[1] * positive[0]








nums = [-1,-2,-3,0,2,-5,1]
ret=  maximum_product(nums)
print(ret)