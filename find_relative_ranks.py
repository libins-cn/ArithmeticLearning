# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       find_relative_ranks.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-21 17:21
   SoftWare     :       IntelliJ IDEA
   Description  :       相对名词[leetcode:506]
-------------------------------------------------
"""


# 类似布隆过滤器的原理，获取到最大的分数max之后，申请一个包含max个元素的数组
def find_relative_ranks(nums):
    max = 0  # 获取分数的最大值
    for num in nums:
        if num > max:
            max = num
    nums_index = [-1] * (max + 1)  # 申请一个包含max+1个全是-1的数组
    for i in range(len(nums)):
        nums_index[nums[i]] = i  # 把该元素对应的下标处的值置为在原始数组中的索引下标
    rank = 1  # 排名
    while max >= 0:
        if nums_index[max] >= 0:
            if rank == 1:
                nums[nums_index[max]] = "Gold Medal"
            elif rank == 2:
                nums[nums_index[max]] = "Silver Medal"
            elif rank == 3:
                nums[nums_index[max]] = "Bronze Medal"
            else:
                nums[nums_index[max]] = f"{rank}"
            rank += 1
        max -= 1
    return nums


nums = [1]
ret = find_relative_ranks(nums)
print(ret)
