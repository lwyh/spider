"""
输入的数组包括矩阵的行和列，以及k
输出最多能获得的黄金克数
"""
import numpy as np
def maxgold():
    lst=list(map(int,input().split()))
    m,n,k=lst[0],lst[1],lst[2]
    matrix=np.zeros((m,n),dtype=int)
    gold=0
    for i in range(m):
        for j in range(n):
            a=i//10
            b=i%10
            c=j//10
            d=j%10
            if(a+b+c+d<=k):
                gold+=1
    print(gold)
    return gold
if __name__=="__main__":
    maxgold()


    
