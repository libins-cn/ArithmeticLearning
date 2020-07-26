# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		two_sum.py
# CreateDate: 		2020-07-26 22:58:28
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-07-26 22:58:28
# SoftWare:			Visual Studio Code
# Description: 		leetcode第1题，两数之和	
# -------------------------------------------------
'''


def two_sum(nums: list, target: int) -> list:
    hash_nums = {}
    for i in range(len(nums)):
        num1 = nums[i]
        if num1 in hash_nums:
            hash_nums[num1].append(i)
        else:
            hash_nums[num1] = [i]

    for i in range(len(nums)):
        num1 = nums[i]
        num2 = target - num1
        # 如果能在hash表里能够查到目标的值，直接返å回即可
        if hash_nums.get(num2) is not None:
            for idx in hash_nums[num2]:
                if idx != i:
                    return [i, idx]


nums = [2, 5, 5, 11]
target = 10
ret = two_sum(nums, target)
print(ret)
