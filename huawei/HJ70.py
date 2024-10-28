"""
@Description : 矩阵乘法计算量估算

描述

矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：

A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵

计算A*B*C有两种顺序：((AB)C)或者(A(BC))，前者需要计算15000次乘法，后者只需要3500次。
编写程序计算不同的计算顺序需要进行的乘法次数。

数据范围：矩阵个数：1≤n≤15 1≤n≤15 ，行列数：1≤rowi,coli≤100 1≤rowi​,coli​≤100 ，保证给出的字符串表示的计算顺序唯一。
进阶：时间复杂度：O(n) O(n) ，空间复杂度：O(n) O(n) 


输入描述：

输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则
计算的法则为一个字符串，仅由左右括号和大写字母（'A'~'Z'）组成，保证括号是匹配的且输入合法！
输出描述：

输出需要进行的乘法次数

示例1
输入：

3
50 10
10 20
20 5
(A(BC))

输出：

3500

@Author      :   hermione
@Time        :   2024/05/15 17:46:41
"""


"""
    (A (BC)) DE (FG) HIJK

    A B(C (DE)) (FG)HI JK

    50 10
10 20
20 5
(A (BC))
首先处理矩阵信息，存储在arr中，arr = [[50, 10], [10, 20], [20, 5]]
(A (BC))
\[ShortUpArrow]
 遍历指针
1. 没有遇到右括号，入栈矩阵A
2. 没有遇到右括号，入栈矩阵B
3. 没有遇到右括号，入栈矩阵C
4. 遇到右括号，取出栈顶2元素，计算
D = BC = [10, 5]
res = 10*20*5 = 1000
D重新入栈
5. 遇到右括号，取出栈顶2元素，计算
E = AD = [50, 5]
res = 1000 + 50*10*5 = 3500
返回最终结果res = 3500


"""
def maxplus():
    n= int(input())
    arr = []
    order = []
    res = 0
    for i in range(n):
        arr.append(list(map(int,input().split()))) #处理输入的矩阵行
        print(arr)
    f = input()
    for i in f:
        if i.isalpha():
            order.append(arr[ord(i)-65])  #将字母转换成第几个矩阵的处理信息
        elif i ==')' and len(order) >=2:
            b = order.pop()
            a = order.pop()
            res +=a[1]*b[1]*a[0]    #累计到res中
            order.append([a[0],b[1]])          #并将栈顶的矩阵的行列更新
    return res

print(maxplus())