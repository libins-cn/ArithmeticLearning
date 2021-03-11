# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		get_importance.py
# CreateDate: 		2021-03-01 20:00:52
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-03-01 20:00:52
# SoftWare:			Visual Studio Code
# Description: 		leetcode第690题：员工的重要性	
# -------------------------------------------------
'''

class Solution:
    def getImportance(self, emps, id: int) -> int:
        emps_dict = {} # 将原始对象转化为hash表
        for emp in emps:
            emps_dict[emp.id] = [emp.importance, emp.subordinates]

        def importances(emps_dict, id): # 自建递归函数
            if (emps_dict[id][1]) == 0: # 递归终止条件：如果没有下属，则获取当前员工的重要性
                return emps_dict[id][0]
            result = emps_dict[id][0] # 如果有下属，则获取自己的重要性并加上每个下属的重要性
            for sub_ids in emps_dict[id][1]:
                result += importances(emps_dict, sub_ids)
            return result 
        return importances(emps_dict, id)
