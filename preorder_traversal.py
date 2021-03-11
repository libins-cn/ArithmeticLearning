# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		preorder_traversal.py
# CreateDate: 		2021-02-05 12:04:58
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-02-05 12:04:58
# SoftWare:			Visual Studio Code
# Description: 		leetcode 144. 二叉树的前序遍历	
# -------------------------------------------------
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: # 递归终止条件，当节点无任何子节点时，返回自己的值(注意是list类型)
            return []
        if root.left is None and root.right is None:
            return [root.val]
        # 返回当前左子节点+右子节点的列表（需转换成list并合）
        return [root.val]+list(self.preorderTraversal(root.left)) + list(self.preorderTraversal(root.right))
