# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		single_non_duplicate.py
# CreateDate: 		2020-09-06 21:31:39
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-09-06 21:31:40
# SoftWare:			Visual Studio Code
# Description: 		LeetCode第540题：有序数组中的单一元素	
# -------------------------------------------------
'''
# 解题思路
# - 超97.68%
# - 其实就是变相的二分查找 + 递归，但是没有用到元素有序的条件
# - 每次递归都判断当前数组的中间元素前半段是否是偶数个元素，如果是，则目标元素肯定在后半段，如果不是偶数个，则目标元素肯定出现在前半段。
# - 直到找出当前数组中间元素跟相邻的两个元素都不相等时，该元素就是目标元素。
# - 或者当前数组中只有一个元素时，该元素就是目标元素
class Solution:
    def singleNonDuplicate(arr:list):
        mid = len(arr) // 2 # 当前数组中间元素的下标
        # 递归终止条件1.如果当前只剩一个元素，则就是目标元素
        if len(arr) == 1:
            return arr[0]
        # 递归终止条件2.如果当前数组中间位置的元素都不等于相邻的两个元素，则该元素就是目标元素
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        # 开始递归
        if arr[mid] == arr[mid - 1]: # 如果当前数组中间元素与前一个元素相等
            if len(arr[: mid + 1]) % 2 == 0:
                # 中间及前面的元素有偶数个，则前半段肯定没有目标元素，直接从后半段里面查找
                return self.singleNonDuplicate(arr[mid + 1:])
            else:
                return self.singleNonDuplicate(arr[:mid + 1])
        else: # 如果当前数组中间元素等于后一个元素
            if len(arr[mid:]) % 2 == 0:
                return self.singleNonDuplicate(arr[:mid])
            else:
                return self.singleNonDuplicate(arr[mid:])

arr = [1]
ret = singleNonDuplicate(arr)
print(ret)
