# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		find_lhs.py
# CreateDate: 		2021-02-02 19:13:13
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-02-02 19:13:13
# SoftWare:			Visual Studio Code
# Description: 		leetcode第594题	
# -------------------------------------------------
'''


def find_lhs(nums):
        result = 0
        nums_counter = {}
        for num in nums:
            if num in nums_counter:
                nums_counter[num] += 1
                continue
            nums_counter[num] = 1
        for num in nums_counter.keys():
            if nums_counter.get(num + 1) is not None \
                and nums_counter[num] + nums_counter[num + 1] > result:
                    result = nums_counter[num] + nums_counter[num + 1]
        return result


nums = [1, 3, 2, 2, 5, 2, 3, 7]
ret = find_lhs(nums)
print(ret)
