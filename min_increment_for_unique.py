# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       min_increment_for_unique.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-22 15:44
   SoftWare     :       IntelliJ IDEA
   Description  :       使数组唯一的最小增量[leetcode:945]
-------------------------------------------------
"""


# 类似计数排序的原理
def min_increment_for_unique(arr):
        nums = [0] * 80001  # 申请一个全是0的数组
        dup_count = 0  # 原始数组中重复的个数
        for a in arr:  # 计数排序
            nums[a] += 1
            if nums[a] == 2:
                dup_count += 1
        output = 0
        point = 0  # 当前为指针到哪了
        pro_count = 0  # 统计已经处理的重复数
        for i in range(len(nums)):
            n = nums[i]
            if n > 1:  # 如果当前位置的值大于0，则说明是重复数，计数器+1
                pro_count += 1
            while n > 1:
                if point < i:
                    point = i + 1  # point的位置只能大于当前位置，因为题目只允许+1
                if nums[point] == 0:  # 找到离当前最近的0的位置
                    output += point - i  # 需要move的次数就是当前0的下标减去该数据所在的下标
                    n -= 1
                point += 1
            if pro_count == dup_count:  # 如果已经处理的重复数 = 原始数组的重复数，节省时间，直接return
                return output


arr = [3, 2, 1, 2, 1, 7]
ret = min_increment_for_unique(arr)
print(ret)
