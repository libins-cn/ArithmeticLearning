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


def diameter_of_binary_tree(tree):
    max = 0
    i = 0

    def get_paths(i):
        lid = 2 * i + 1
        rid = 2 * i + 2
        if rid >= len(tree) or lid >= len(tree) or (tree[lid] is None and tree[rid] is None):
            return 0
        num = 0
        if get_paths(lid) > 0:
            num += 1
        if get_paths(rid) > 0:
            num += 1
        if num > 1:
            num = 1
        return num

    return get_paths(i)


tree = [1, 2, 3, 4, 5]
ret = diameter_of_binary_tree(tree)
print(ret)
