"""

而生成树最重要的两个特性就是：

1、包含所有顶点

2、无环

"""
#并查集实现
class UnionFindSet:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.count = n

    def find(self, x):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]
        return x
    
    def union(self, x, y):
        x_fa = self.find(x)
        y_fa = self.find(y)
        if x_fa != y_fa:
            self.fa[x_fa] = y_fa
            self.count -= 1

#输入获取
n = int(input()) #基站数量（节点数）
m = int(input()) #连接线数量（边数）

edges = []
for i in range(m):
    #边起点，边终点，边权重（起点和终点关联代价），起点是由已和终点关联
    x,y,z,p = map(int, input().split())

    if p==0:
        #起点和终点未关联
        edges.append([x,y,z])

    else:
        #起点和终点已关联，则实际关联代价为0
        edges.append([x,y,0])

#Krusakal 算法
def kruskal():
    minWeight =0


    #按照边权升序
    edges.sort(key=lambda x:x[2])
    ufs = UnionFindSet(n+1)
    #最先遍历出来的是边权最小的边
    for x,y,z in edges:
        #如果x节点和y节点是同一个联通分量(即都在生成树中)，则此时会产生环
        #因此只有当x节点和y节点不在同一个联通分量时，合并（纳入最小生成树）
        if ufs.find(x)!= ufs.find(y):
            minWeight += z
            ufs.union(x,y)
            

        # 需要注意的是，上面初始化并查集的节点树为n+1个，因此并查集底层fa数组的大小为n+1，
        # 即索引范围是[0,n],左闭右闭，
        #其中0索引是无用的，1~n索引对应最小生成树各个节点，如果有n个节点可以变为最小生成树，那么1~n节点会北合并成一个联通分量
        #而0索引虽然无用，但是也会自己形成一个联通分量，因此最终如果能形成最小生成树，则并查集中会有两个联通分量
        if ufs.count == 2:
            return minWeight
    return -1 #如果没有形成最小生成树，则返回-1

#算法入口
print(kruskal())