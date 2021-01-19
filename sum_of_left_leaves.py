# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		sum_of_left_leaves.py
# CreateDate: 		2021-01-18 19:29:53
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-01-18 19:29:54
# SoftWare:			Visual Studio Code
# Description: 		LeetCode第404题：左叶子之和	
# -------------------------------------------------
'''


def sumOfLeftLeaves(root: list):
    if root is None:
        return 0
    if root.left is None:  # 当前节点的左子节点是空，则返回右子节点的递归
        return self.sumOfLeftLeaves(root.right)
    if root.left.left is None and root.left.right is None:  # 当且仅当子节点的左右子节点都为空时，才取叶子节点的值
        return root.left.val + self.sumOfLeftLeaves(root.right)
    # 当前节点的左右子节点都不为空，且还存在孙子节点时，继续递归
    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
