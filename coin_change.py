# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       coin_change.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-22 17:39
   SoftWare     :       IntelliJ IDEA
   Description  :       零钱兑换[leetcode:322]
-------------------------------------------------
"""


def coin_change(coins, amount):
    if amount == 0:
        return 0

    def insert_sort(arr):
        for i in range(len(arr)):
            value = arr[i]
            for j in range(i - 1, -1, -1):  # 从当前正在比较的最后一位开始比较
                if value < arr[j]:
                    tmp = arr[j]
                    arr[j] = arr[j + 1]  # 数据移动
                    arr[j + 1] = tmp
                else:
                    break
        return arr

    output = 0
    coins = insert_sort(coins)
    print(coins)
    i = len(coins) - 1
    while i >= 0:
        if amount - coins[i] >= 0:
            amount -= coins[i]
            output += 1
            if amount == 0:
                return output
        else:
            i -= 1
    return -1


# coins = [ 2]
coins = [186, 419, 83, 408]
amount = 6249
ret = coin_change(coins, amount)
print(ret)
