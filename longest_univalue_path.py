# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		longest_univalue_path.py
# CreateDate: 		2020-07-11 23:29:05
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-07-11 23:29:06
# SoftWare:			Visual Studio Code
# Description: 		LeetCode第687题：最长同值路径	
# -------------------------------------------------
'''

#


def longest_univalue_path(arr: list) -> int:
    def node_path(i: int):
        lnum = 0
        rnum = 0
        if 2 * i + 1 < len(arr) and arr[2 * i + 1] == arr[i]:
            lnum = node_path(2 * i + 1) + 1
        if 2 * i + 2 < len(arr) and arr[2 * i + 2] == arr[i]:
            rnum = node_path(2 * i + 2) + 1
        
        return lnum + lnum
        
    maxlen = 1
    for i in range(len(arr)):
        lens = node_path(i)
        if lens > maxlen:
            maxlen = lens
    return maxlen


arr = [4, 4, 5, 4, 4, 5]
ret = longest_univalue_path(arr)
print(ret)
