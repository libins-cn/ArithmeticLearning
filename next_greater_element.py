# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       next_greater_element.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-18 22:46
   SoftWare     :       IntelliJ IDEA
   Description  :       下一个更大的元素I[leetcode:496]
-------------------------------------------------
"""

def next_greater_element(nums1, nums2):
    mapping = {}  # 把nums2的每个元素当做key，索引当做value放到hash表里面
    for i in range(len(nums2)):
        mapping[nums2[i]] = i
    output = [-1] * len(nums1)  # 初始化一个长度为nums1的全是-1的数组
    for n in range(len(nums1)):  # 一次遍历nums1中的每个元素
        j = mapping[nums1[n]]  # 获取该元素在nums2中的位置，并从该位置开始往后遍历
        while j < len(nums2):
            if nums2[j] > nums1[n]:  # 遇到比当前大的数， 直接在对应的output里填此时nums2的数
                output[n] = nums2[j]
                break
            j += 1
    return output


# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
ret = next_greater_element(nums1, nums2)
print(ret)
