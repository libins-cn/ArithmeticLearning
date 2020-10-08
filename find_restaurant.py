# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		find_restaurant.py
# CreateDate: 		2020-10-08 22:11:26
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2020-10-08 22:11:26
# SoftWare:			Visual Studio Code
# Description: 		leetcode第599题： 两个列表的最小索引总和	
# -------------------------------------------------
'''


def find_restaurant(list1: list, list2: list) -> list:
    list1_dict = {}
    min_sum_idx = len(list1) + len(list2)  # 初始索引和为两个list之和
    for i in range(len(list1)): # 将第一个数组放到一个hash表里，key是元素，value是索引值
        list1_dict[list1[i]] = i
    sum_idxs = {} # 存放两个list相同的元素（key是索引之和，value是相同的元素）
    # 遍历第二个数组，一边遍历一边从hash表里查找是否存在相同的元素，如果相同就求索引和
    for j in range(len(list2)):
        if list1_dict.get(list2[j]) is not None: 
            sum_idx = list1_dict.get(list2[j]) + j
            if sum_idxs.get(sum_idx) is not None:
                sum_idxs[sum_idx].append(list2[j])
            else:
                sum_idxs[sum_idx] = [list2[j]]
            if sum_idx <= min_sum_idx: 
                min_sum_idx = sum_idx # 标记当前最小索引和到哪个位置了
    return sum_idxs[min_sum_idx] # 返回当前最小索引和对应的数组


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
ret = find_restaurant(list1, list2)
print(ret)
