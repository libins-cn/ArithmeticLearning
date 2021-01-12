# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		can_place_flowers.py
# CreateDate: 		2021-01-03 22:23:03
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-01-03 22:23:03
# SoftWare:			Visual Studio Code
# Description: 		leetcode第605题：种花问题	
# -------------------------------------------------
'''

def can_place_flowers(arr, n):
    result = 0 # 初始值能种入0朵
    # 从第一个花坛开始从前往后放，放到倒数第二个位置，遇到左右两边都是空的位置，直接放入即可
    for i in range(0, len(arr) - 1): 
        # 第一个位置比较特殊：只要第二个花坛里面没有，就可以放
        if i == 0 and arr[i] == 0 and arr[i+1] == 0: 
            result =+ 1
            arr[i] = 1 
            continue
        # 其他位置只需要看当前，前一个，后一个是否是空即可
        if arr[i] == 0 and arr[i + 1] == 0 and arr[i -1 ] == 0:
            result += 1 
            arr[i] = 1
    # 最后一个位置比较特殊：如果它前一个是空，那么它自己也可以放
    if arr[len(arr) -1 ] == 0 and arr[len(arr) -2 ] ==0:
        result += 1
    return result >= n 



flowerbed = [1,0,0,0,1]
n = 2
ret = can_place_flowers(flowerbed, n)
print(ret)

