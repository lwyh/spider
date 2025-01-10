"""
投递员最优路线输出，客户与客户之间不保证有最短距离。没有时的路线均为投递站与客户之间的距离的来回
当有路线时，需要比较两个客户与投递站的来回距离相加跟一个来回加客户之间的距离相加的
最短路线的计算是:若客户之间的距离大于起点到两客户之间的距离和，则放弃此条客户之间过度的路线
本题方法：
分别计算第一最短，第二最短，...第k最短，直至刚好遍历完最后一个点，最后再算一次最后一个点到起始点的最短距离，即为全程最短距离
1.以地点0开始，计算到A,B,C最短距离，例如为C
2.以1步骤中的最短距离点C为起点，计算到剩余节点A,B节点的最短距离，例如为A
3.以2步骤中的最短距离点A为起点，计算到剩余节点B的的最短距离
4.以最后一个计算节点B为起点，计算返回到起点0的最短距离
5.将上述每个步骤中的最短距离分别相加得出遍历所有节点回到原始点的最短距离

2.
"""

import math
from collections import deque
def zuiyouluxian1():
    arr1=[]
    arr2=[]
    nodes=[0]
    all_id_dict={}
    min_values=[]
    arr3= list(map(int,input().split()))
    n,m=arr3[0],arr3[1]
    print(n,m)
    for i in range(n):
        arr1= list(map(int,input().split()))
        value1,value2=arr1[0],arr1[1]
        all_id_dict[(0,value1)]=value2
        all_id_dict[(value1,0)]=value2
        nodes.append(value1)
    for j in range(m):
        arr2= list(map(int,input().split()))
        ele1,ele2,ele3=arr2[0],arr2[1],arr2[2]
        all_id_dict[(ele1,ele2)]=ele3
        all_id_dict[(ele2,ele1)]=ele3
    print(all_id_dict)
    #定义图结构
    graph=dict()
    def add_edge(graph,start,end,weight):
        if(start not in graph):
            graph[start]={}
        if(end not in graph):
            graph[end]={}
        graph[start][end]=weight
        return graph
    for key,value in all_id_dict.items():
        graph = add_edge(graph,key[0],key[1],value)

    print("graph",graph)
    #使用BFS算法找到遍历所有点的最短路径,先定义所有点到其中某个点的最短距离函数
    def bfs_shorttest_path(graph,start):
        #初始化节点以及到起点的距离队列
        queue=deque([(start,0)]) #（node,distance）
        #初始化已访问过的节点集合
        visited=set()
        #初始化节点到起点距离
        distances={node:float('inf') for node in graph}
        distances[start]=0

        while queue:
            #取出栈顶的节点
            current,current_distance=queue.popleft()
            if(current not in visited):
                current_distance=distances[current]
                visited.add(current)
                for neighbor,weight in graph[current].items():
                    new_distance=current_distance+weight
                    if(new_distance< distances[neighbor]):
                        distances[neighbor]=new_distance
                        queue.append((neighbor,new_distance))

        return distances

    visited_columns=set()
    distance_path=0
    visited_columns.add(0)
    item=0
    while(len(visited_columns)<n+1):
        print("visited_columns",visited_columns)
        node_0_distance = bfs_shorttest_path(graph,item) #上一轮最短距离的节点作为下一轮的起点
        print(node_0_distance)
        #去掉已访问过的节点，如果在已访问过的点中将其权重重新赋值为无穷大，这样就不会考虑
        item=min(node_0_distance,key= lambda x: node_0_distance[x] if x not in visited_columns else float('inf'))
        print(item) #3
        visited_columns.add(item)
        distance_path+=node_0_distance[item]
        print("distance_path",distance_path)
    node_0_distance = bfs_shorttest_path(graph,item)
    distance_path+= node_0_distance[0]



    print(node_0_distance,distance_path)

    return distance_path

  
   
if __name__ =="__main__":
    zuiyouluxian1()

                


        




            




    
    




