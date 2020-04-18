# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       min_mum_length_encoding.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-28 22:10
   SoftWare     :       IntelliJ IDEA
   Description  :       单词的压缩编码[leetcode:820]
-------------------------------------------------
"""


def min_mum_length_encoding(words):
    result = [words[0]]
    output = len(result[0])
    for j in range(1, len(words)):
        print(result)
        word = words[j]
        for i in range(len(result)):
            res = result[i]
            min_len = len(res) if len(res) < len(word) else len(word)
            cnt = 0
            while cnt < min_len:
                if res[cnt] == word[cnt] or res[len(res) - cnt - 1] == word[len(word) - cnt - 1]:
                    cnt += 1
                else:
                    cnt -= 1
                    break
            # print(i ,cnt, min_len, len(res), len(word))
            print(cnt, len(word), word, res)
            if cnt == min_len - 1 and len(res) < len(word):
                result[i] = word
                output += len(word) - len(res)
                break
            if i == len(result) - 1 and cnt != min_len:  # 判断是不是result的最后一个元素
                # print('hehe')
                result.append(word)
                output += len(word)
    print(result)
    return output + len(result)


# words = ["time", "me", "bell"]
words = ["time", "atime", "btime"]
ret = min_mum_length_encoding(words)
print(ret)
