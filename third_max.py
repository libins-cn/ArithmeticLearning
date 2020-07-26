# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		third_max.py
# CreateDate: 		2020-07-15 23:12:05
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-07-15 23:12:05
# SoftWare:			Visual Studio Code
# Description: 		LeetCode：第三大的数	
# -------------------------------------------------
'''
# 维护一个三个元素的小顶堆
# 每来一个元素判断，跟堆顶的值比较，如果比堆顶小，直接忽略，如果比堆顶大， 则将数据插入到，再进行堆化


def third_max(nums):

    def get_max(arr, ignore_value):
        hashs = {}
        max_value = 0
        for a in arr:
            if a == ignore_value:
                continue
            hashs[a] = 1
            if a > max_value:
                max_value = a

        dist_arr = []
        for key in hashs.keys():
            dist_arr.append(key)
        return dist_arr, max_value
    
    max_value = None 
    for i in range(3):
        nums,max_value = get_max(nums, max_value)
        if len(nums) < 3:
            return max_value
    
    return max_value

nums = [2, 2, 3, 1]
ret = third_max(nums)
print(ret)