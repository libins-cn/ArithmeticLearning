# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       diameter_of_binary_tree.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-10 21:58
   SoftWare     :       IntelliJ IDEA
   Description  :       二叉树的直径[leetcode:543题]
-------------------------------------------------
"""

# 解题思路：采用双递归，先递归求每个结点的左边和右边的最大值，再求出这些最大值中的最大值
class Solution:
    def diameterOfBinaryTree(self, inputRoot: TreeNode) -> int:
        def max_side(root:TreeNode): # 获取该节点的左边和右边的最大值
            if root is None or (root.left is None and root.right is None):
                return 0
            if root.left is None and root.right is not None:
                return max_side(root.right) + 1
            if root.right is None and root.left is not None:
                return max_side(root.left) + 1
            return max(max_side(root.left) + 1, max_side(root.right) + 1)
        
        def run(root:TreeNode): # 依次递归遍历每个节点，并求拿每次递归的最大值进行比较
            if root is None or (root.left is None and root.right is None):
                return 0
            if root.left is None and root.right is not None:
                return max_side(root.right) + 1
            if root.right is None and root.left is not None:
                return max_side(root.left) + 1
            # 返回左子节点、右子节点和当前节点（当前节点需要左子+右子+2）的最大值
            return max(run(root.left), run(root.right), max_side(root.left) + max_side(root.right) + 2)
        return run(inputRoot) 