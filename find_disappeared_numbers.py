# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       find_disappeared_numbers.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-05 21:43
   SoftWare     :       IntelliJ IDEA
   Description  :       找到所有数组中消失的数字[leetcode:448题]
-------------------------------------------------
"""


# 类似布隆过滤器
def find_disappeared_numbers(arr):
    nums = [0] * (len(arr) + 1)  # 申请一个长度为输入数组+1 ，且所有元素都是0的数组
    target_nums = []  # 最终需要返回的数组
    for a in arr:
        nums[a] = 1  # 把原数组的值当做新申请数组的下标，并且该下标的值在申请的数组里置为1
    for i in range(1, len(nums)):
        if nums[i] == 0:  # 如果发现有值为0，则该值对应的下标就是原数组缺失的元素
            target_nums.append(i)
    return target_nums


arr = [4, 3, 2, 7, 8, 2, 3, 1]
# arr = [1, 1]
ret = find_disappeared_numbers(arr)
print(ret)
