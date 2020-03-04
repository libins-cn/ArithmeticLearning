# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       find_duplicates.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-04 22:44
   SoftWare     :       IntelliJ IDEA
   Description  :       数组中重复的数据[leetcode: 442题]
-------------------------------------------------
"""


# 申请一个长度为len(arr) + 1 ，所有元素都是0的数组b，顺序遍历数组arr。把arr里的每个元素的值当做b元素的下标，
# 并把在b数组里把该下标的值记为1，当记为1之前发现该位置已经是1，则说明该值是重复的。
def find_duplicates(arr):
    ret = []
    arr2 = [0] * (len(arr) + 1)
    for a in arr:
        if arr2[a] == 1:
            ret.append(a)
            continue
        arr2[a] = 1
    return ret


arr = [4, 3, 2, 7, 8, 2, 3, 1, 9]
ret = find_duplicates(arr)
print(ret)
