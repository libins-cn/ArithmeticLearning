# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		find_error_nums.py
# CreateDate: 		2021-02-24 19:48:50
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-02-24 19:48:50
# SoftWare:			Visual Studio Code
# Description: 		leetcoee第645题：错误的集合	
# -------------------------------------------------
'''
def find_error_nums(nums):
    blooms = [0] * (len(nums) + 1)
    for num in nums: # 先找到数组的最大值
        blooms[num] +=1 
    result = [0, 0]
    for i in range(1, len(blooms)):
        if blooms[i] == 0: # 缺少的
            result[1] = i
        if blooms[i] == 2: # 多余的
            result[0] = i 
    return result

nums = [1,1]
ret = find_error_nums(nums)
print(ret)
