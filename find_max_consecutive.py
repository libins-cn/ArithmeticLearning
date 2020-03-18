# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       find_max_consecutive.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-18 22:25
   SoftWare     :       IntelliJ IDEA
   Description  :       最大连续1的个数[leetcode:485]
-------------------------------------------------
"""


def find_max_consecutive(arr):
    max = 0
    count = 0
    for a in arr:
        if a == 1:
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    return max


arr = []
ret = find_max_consecutive(arr)
print(ret)
