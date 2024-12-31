"""

而生成树最重要的两个特性就是：

1、包含所有顶点

2、无环



"""

import sys
#输入获取
n = int(input())  #基站数量(节点数)
m = int(input())  #基站对数量（边数）

#邻接矩阵，初始化默认各点之间互不联通，即i-j边权无限大
graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    x,y,z,p = map(int,input().split())
    if p==0:
        #x-y边权为0
        graph[x][y] = z
        graph[y][x] = z
    else:
        #对应已经联通是两点，可以理解为边权为0
        graph[x][y] = 0
        graph[y][x] = 0

#Prim算法
def prim():
    #记录最小生成树的边权和
    minWeight = 0


    #inTree[i]表示节点i是否在最小生成树中
    inTree = [False]*(n+1)

    #初始时任选一个节点作为最小生成树的初始节点，这里选择节点1
    inTree[1] = True
    #记录最小生成数中点数量
    inTree_count = 1

    #dis[i]表示节点i到最小生成树集合的最短距离
    #初始时，最小生成树集合中只有节点1，因此其他节点到最小生成树的距离，其实就是到节点1的距离
    dis = [0]*(n+1)
    for i in range(1,n+1):
        dis[i]=graph[1][i]

    # 如果最小生成数中点数量达到n个，则结束循环
    while inTree_count<n:
        #现在我们需要从未纳入最小生成树的点中，找到一个距离最小生成树最近的
        minDis = sys.maxsize  # minDis 记录这个最近距离
        print("minDis:",minDis)
        nodeIdx = 0 #idx记录距离最小生成树minDis个距离的节点
        for i in range(1,n+1):
            #从未纳入最小生成树的点中。找到一个距离最小生成树最近的
            if not inTree[i] and dis[i]<minDis:
                minDis = dis[i]
                nodeIdx = i
            
#如果nodeIdx ==0 ,则说明未纳入最小生成树的这些点到最小生成树的距离都是Integer.MAX_VALUE,即不与最小生成树存在关联
        if nodeIdx == 0:
            #则说明，当前所有点无法形成最小生成树
            return -1
        
        inTree[nodeIdx] = True  #最小生成树需要纳入最短距离点nodeIdx
        inTree_count += 1  #最小生成树点数量+1
        minWeight += dis[nodeIdx]   #更新最小生成树的权重和

        #dis[i]初始时记录的是节点i 到节点1的距离 （初始的生成树中只有节点1）
        #现在生成树纳入了新节点nodeIdx,则我们需要更新一下dis[i],即可能某些点到最小生成树中的nodeIdx点的距离更近
        for i in range(1,n+1):
            if not inTree[i] and graph[nodeIdx][i]<dis[i]:
                #注意，这是一个累进过程，初始时dis[i]记录的是节点i 到节点1的距离
                #之后，最小生成树纳入新点后，如果节点i到新点的距离更近，则更新dis[i]为这个更短距离
                #总之，dis[i]记录的是节点i到最小生成树的最短距离
                dis[i] = graph[nodeIdx][i]

    return minWeight

print(prim())

        











