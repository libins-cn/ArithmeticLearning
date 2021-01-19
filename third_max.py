# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		third_max.py
# CreateDate: 		2021-01-13 19:51:35
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-01-13 19:51:36
# SoftWare:			Visual Studio Code
# Description: 		leetcode第414题：第三大的数	
# -------------------------------------------------
'''

def third_max(nums):
    # 先获取一个有序数组
    arr = [nums[0]]
    i = 1
    while i < len(nums):
        print(i)
        for a in arr:
            if a == nums[i]: 
                break 
            else:
                arr.append(nums[i])
        
        if len(arr) >= 3:
            break  
    return arr 
    
    # 建堆

    # 堆化

arr = [1,1,1,1,3,2,1,1,1,3]
ret = third_max(arr)
print(ret)


