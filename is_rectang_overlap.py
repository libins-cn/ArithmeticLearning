# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       is_rectang_overlap.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-18 14:34
   SoftWare     :       IntelliJ IDEA
   Description  :       矩形重叠[leetcode:836]
-------------------------------------------------
"""


# 解题思路
# 同时满足以下两个条件即可视为两矩形相交
# 1.第二个矩形的左下角坐标要小于第一个矩形右上角的坐标
# 2.第二个矩形的右上角坐标要大于第一个矩形左下角的坐标
def is_rectlang_overlap(rec1, rec2):
    return rec2[0] < rec1[2] \
           and rec2[1] < rec1[3] \
           and rec2[2] > rec1[0] \
           and rec2[3] > rec1[1]


rec1 = [0, 0, 1, 1]
rec2 = [1, 0, 2, 1]
ret = is_rectlang_overlap(rec1, rec2)
print(ret)
