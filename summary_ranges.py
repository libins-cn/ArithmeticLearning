# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		summary_ranges.py
# CreateDate: 		2021-01-03 21:07:01
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-01-03 21:07:01
# SoftWare:			Visual Studio Code
# Description: 	    leetcode第228题：汇总区间		
# -------------------------------------------------
'''


def summary_ranges(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return ["{}".format(nums[0])]
    # 根据区间的起始值到当前值，返回该区间
    def get_cell(start_value, curr_value):
        if curr_value == start_value:
            return "{}".format(curr_value)
        else:
            return "{}->{}".format(start_value, curr_value)

    result = []
    start_value = nums[0] # 每个区间的起始值
    curr_value = start_value # 该区间当前值
    for i in range(1, len(nums)):
        if nums[i] == curr_value + 1: # 如果当前数组元素与当前区间的最大元素+1相等，则说明是连续的
            curr_value = nums[i]
        else:
            result.append(get_cell(start_value, curr_value))
            start_value = nums[i] # 重置下一个区间的起始值
            curr_value = start_value
        if i == len(nums) - 1: # 不要忘了最后一个元素
            result.append(get_cell(start_value, curr_value))
    return result


nums = [1, 3]
ret = summary_ranges(nums)
print(ret)