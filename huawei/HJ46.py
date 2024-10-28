"""
@Description : 描述
输入一个字符串和一个整数 k ，截取字符串的前k个字符并输出

数据范围：字符串长度满足 1≤n≤1000 1≤n≤1000  ， 1≤k≤n 1≤k≤n 

输入描述：

1.输入待截取的字符串

2.输入一个正整数k，代表截取的长度
输出描述：

截取后的字符串
示例1
输入：
abABCcDEF
6
输出：
abABCc
@Author      :   hermione
@Time        :   2024/05/15 17:32:10
"""

a1 = input()
a2 = input()

def substring():
    return a1[0:int(a2)]
print(substring())
