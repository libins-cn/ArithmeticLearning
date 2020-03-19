# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       next_greater_elements.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-19 22:20
   SoftWare     :       IntelliJ IDEA
   Description  :       下一个更大元素2[leetcode:503]
-------------------------------------------------
"""


# 暴力求解的办法
def next_greater_elements(nums):
    i = 0
    len_nums = len(nums)
    output = [-1] * len_nums  # 初始化一个所有元素是-1的数组，长度跟输入长度一样
    while i < len_nums:
        for j in range(i, len_nums + i):
            if j >= len_nums:  # 如果当前的j值大于最大的数组下标，则重新0开始遍历
                j = j - len_nums  # 重新定义数组下标
            if nums[j] > nums[i]:
                output[i] = nums[j]
                break
        i += 1
    return output


nums = [3]
ret = next_greater_elements(nums)
print(ret)
