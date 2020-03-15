# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       reverse_list.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-11 22:06
   SoftWare     :       IntelliJ IDEA
   Description  :       单链表反转[leetcode:206]
-------------------------------------------------
"""


def reverse_list(head):
    cur = head
    pre = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


list_node = [1, 2, 3, 4, 5]
ret = reverse_list(list_node)
print(ret)
