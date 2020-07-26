# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		merge.py
# CreateDate: 		2020-07-12 17:36:39
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-07-12 17:36:40
# SoftWare:			Visual Studio Code
# Description: 		LeetCode88题，合并两个有序数组	
# -------------------------------------------------
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 定义三个索引
        id = m + n - 1
        id1 = m - 1
        id2 = n - 1
        while id >= 0:
            if id1 < 0:  # 如果第第一个数组已经比较完毕，则直接将第二个数组的元素遍历出来放到对应下标的数组1即可
                for i in range(0, id2+1):
                    nums1[i] = nums2[i]
                break
            if id2 < 0:  # 如果第二个数组已经比较完毕，则说明合并完毕，则直接返回
                break
 # 如果第一个元素的当前最大值小于第二个数组的当前最大值，则将第二个元素的当前最大值放到此处，同时更新第二个元素的索引、以及合并比较的ID往前一位，
            if nums1[id1] <= nums2[id2]:
                nums1[id] = nums2[id2]
                id2 -= 1
                id -= 1
                continue
            if nums1[id1] > nums2[id2]:
                nums1[id] = nums1[id1]
                id1 -= 1
                id -= 1
                continue
        return nums1


solution = Solution
nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
ret = solution.merge(nums1, m, nums2, n)
print(ret)
