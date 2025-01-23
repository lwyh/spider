"""
题目描述

K小姐是一位伐木工人，她有一根长度为 XX 米的原木。为了获得最大的收益，她需要将原木切割成若干段，每一段的长度都必须是正整数。

木材交易价格为每根木头长度的乘积，也可以不切割，拿整根原木进行交易，其交易价格等于原木长度。

现在，请你帮助K小姐计算，要想获得最大收益，并且切割次数尽量少，她应该如何切割这根原木？

输入格式

输入仅一行，包含一个正整数 XX，表示原木的长度。
输出格式

输出若干个正整数，表示切割后每一段木材的长度。你需要按照长度从小到大的顺序输出，相邻两个数之间用一个空格隔开。

如果有多种切割方案都能获得最大收益，你可以输出任意一种。

"""

n = int(input())
f = [0]*(n+1)
for i in range(1,n+1):
    f[i] = i
    for j in range(1,i):
        f[i] = max(f[i],max(j*f[i-j],j*(i-j)))

res = []
m=n
while m>=1:
    if f[m] == m:
        res.append(m)
        break
    for k in range(m-1,0,-1):
        if k*(m-k) ==f[m]:
            res.append(k)
            res.append(m-k)
            m=0
            break
        elif k*f[m-k] == f[m]:
            res.append(k)
            m -=k
            break

res.sort()
print(*res)