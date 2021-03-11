# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		is_one_bit_character.py
# CreateDate: 		2021-03-08 19:46:37
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-03-08 19:46:37
# SoftWare:			Visual Studio Code
# Description: 		LeetCode第717题：1比特与2比特字符	
# -------------------------------------------------
'''


def is_one_bit_character(strings):
    i = 0 
    while i < len(strings):
        # 当前位置为0，且已经是最后一个元素，直接返回True
        if strings[i] == 0 and i == len(strings) - 1 : 
            return True 
        if strings[i] == 1: # 当前位置为1，则说明肯定是2比特的开头
            i += 2 
            continue
        i += 1 # 当前位置为0（一比特），则从下一个位置开始计算
    return False # 所有的元素都遍历完还没返回，说明最后一个字符肯定是2比特


strings =[1, 1, 1, 0]
ret = is_one_bit_character(strings)
print(ret)