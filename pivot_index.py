# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		pivot_index.py
# CreateDate: 		2021-03-09 19:51:32
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-03-09 19:51:32
# SoftWare:			Visual Studio Code
# Description: 		LeetCode第724题：寻找数组的中心下标	
# -------------------------------------------------
'''
# 1.获取从第一个元素开始，截止当前元素的和放到hash表A里，key是当前索引ID，value是从第一个元素到当前元素的值
# 2.获取最后一个元素开始，截止当前元素的和放到hash表B里，key是当前索引ID，value是从最后一个元素到当前元素的值
# 3.从左往右遍历输入的nums，遍历每一个索引ID时，分别从A和B里取出当前ID左边和右边对应的和进行对比，如果相同，则当前ID就是所求
# 4.处理两种特殊情况：第二个元素至最后和为0的情况，倒数第二个元素至第一个元素和为0的情况
def pivot_index(nums):
    maxid = len(nums) - 1
    hdict = {0: nums[0]} # 存放从索引0开始，截止当前索引的值的和
    tdict = {maxid: nums[maxid]} # 存放从最后一个索引开始，截止当前索引的值的和
    for i in range(1, maxid + 1): # 遍历求和
        hdict[i] = hdict[i - 1] + nums[i]
        tdict[maxid - i] = nums[maxid - i] + tdict[maxid - i + 1]
    if tdict[1] == 0: # 处理特殊情况1
        return 0
    for j in range(1, maxid):
        # 如果当前索引前的所有元素之和 与 当前索引后的所有元素之和相等。则直接输出当前ID
        if hdict[j - 1] == tdict[j + 1]: 
            return j
    if hdict[maxid - 1] == 0: # 处理特殊情况2
        return maxid
    return -1


# nums =[1, 7, 3, 6, 5, 6]
# nums = [2, 1, 2,3]
# nums = [2, 1, -1]
# nums = [-1,-1,-1,-1,-1,0]
# nums = [-1,-1,0,1,1,0]
nums = [-1, -1, 1, 1, 0, 0]
ret = pivot_index(nums)
print(ret)
