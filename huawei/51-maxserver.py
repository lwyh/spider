"""
矩阵网络中，同一行或同一列中紧相邻的元素值为1的可以构建局域网，求矩阵网络中局域网中包含服务器的最大个数
本题方法：
dfs深度优先搜索算法
先找到最小索引为1的元素，然后以此移动（上下左右）迭代，直至找不到相连的元素为1
将上述访问的所有元素值为1的记录到已访问列表，再与其所有元素为1的列表做对比
将剩余的值依次类推的移动迭代
将上面每一步的访问元素的的个数用列表装下，再比较列表最大值就说最大局域网的服务器数

"""
import numpy as np

def maxserver():
    list1=list(map(int,input().split()))
    n,m=list1[0],list1[1]
    matrix = np.zeros((n,m),dtype=int)
    for i in range(n):
        matrix[i]=list(map(int,input().split()))
    print(matrix)

    
    #使用深度优先算法遍历所有点找到矩阵的连通性
    visited= [[False]*m for _ in range(n)]
    sequences=[]

    def dfs(r,c,value,seq):
        if(r<0 or r>=n or c<0 or c>=m  or visited[r][c] or matrix[r][c] !=value):
            return
        visited[r][c]=True
        seq.append((r,c))
        #向上下左右四个方向搜索
        dfs(r-1,c,value,seq)
        dfs(r+1,c,value,seq)
        dfs(r,c-1,value,seq)
        dfs(r,c+1,value,seq)

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                seq=[]
                dfs(i,j,1,seq)
                if(len(seq)>1):
                    sequences.append(seq)
    print(sequences)
    max_length=0
    for k in range(len(sequences)):
        if(len(sequences[k])>max_length):
            max_length=len(sequences[k])
    print(max_length)





    #list2.sort(list2,key=lambda item:(item[0],item[1]))
    #之前做过单值连续的函数，现在改为元组连续
    #def consecutive_sequences(list2):
       # for start,end in list2:
            
            

    
            


if __name__=="__main__":
    maxserver()