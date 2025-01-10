"""
N台电脑，有M根线链接任意两台电脑，病毒源从任意一台电脑开始，到病毒传至整个电脑需要的最少时间是多少
此题与38题有点类似，都是需求两点间的最短距离，都可以采用BFS广度搜索算法，只不过这里的距离等价于病毒传染的时间,并且不需要返回起点
"""
from collections import deque
def VirusInfection():
    N=int(input())
    M=int(input())
    path=[]
    all_id_dict=dict()
    nest_list=[]
    nest_set=set()
    for i in range(M):
        path=list(map(int,input().split()))
        #将彼此相连的电脑以及病毒传染时间用dict存储
        ele1,ele2,ele3=path[0],path[1],path[2]
        all_id_dict[(ele1,ele2)]=ele3
        all_id_dict[(ele2,ele1)]=ele3
    k=int(input())#电脑号，与上面的网络链接是同一规则
    print(all_id_dict)
    #还需要将不能链接在一起的两种情况枚举并排除
    nest_set=set()
    print("k",k)
    if all(k not in key for key in all_id_dict):
        print(all_id_dict.keys())
        return -1
    print("k",k)
    for key,value in all_id_dict.items():
        if(k in key):
            nest_set.add(key[0])
            nest_set.add(key[1])
        if(key[0] in nest_set or key[1] in nest_set):
            nest_set.add(key[0])
            nest_set.add(key[1])
    print("nest_set",nest_set)
    
    if(len(nest_set)< N):
        return -1
    #定义图结构
    graph=dict()
    def add_edge(graph, start, end, weight):
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
        graph[start][end] = weight
        return graph

    for key,value in all_id_dict.items():
        graph = add_edge(graph,key[0],key[1],value)
    print(graph)
    print("k",k)
    #使用BFS算法找到遍历所有点的最短路径
    def bfs_shorttest_path(graph,start):
        #初始化队列，用于存储节点及其到起点的病毒传染时间
        queue=deque([(start,0)]) #(node,distance)
        #访问集合，用于记录已访问的节点
        visited=set()
        #存储最短路径的距离（时间）
        distances={node:float('inf') for node in graph}
        distances[start]=0

        while queue:
            #取出栈顶的数据
            print(queue)
            current,current_distance = queue.popleft()
            if(current not in visited):
                visited.add(current)
                distances[current]=current_distance
                for neighbor,weight in graph[current].items():
                    #if(neighbor not in visited):此此处的条件是不能重复计量节点，这会导致直接相连路线大于通过中间路径相连之和的情况不能被过滤，所以此处需要去掉
                    new_distance=current_distance+weight
                    if(new_distance< distances[neighbor]):
                        distances[neighbor]=new_distance
                        queue.append((neighbor,new_distance))
        return distances
    print("k",k)
    shortest_paths = bfs_shorttest_path(graph,k)
    print(shortest_paths)
    out = max(shortest_paths.values())
    print(out)
    return out









    
   


    """
    # 定义图结构
    graph = {
        1: {2: 1, 4: 2},
        2: {1: 1, 3: 1},
        3: {2: 1, 4: 1, 5: 2},
        4: {1: 2, 3: 1, 5: 3},
        5: {3: 2, 6: 1},
        6: {5: 1}
    }
    """



    """
    #初始化时间矩阵，设所有电脑间病毒传染时间为无穷大
    times=[[float('inf')] *len(nodes) for _ in range(len(nodes))]
    #填充时间矩阵
    for (i,j),time in  all_id_dict.items():
        idx_i=nodes.index(i)
        idx_j=nodes.index(j)
        times[idx_i][idx_j]=time
        times[idx_j][idx_i]=time  #确保矩阵对称
    #将对角线上的值赋值为0，即节点自身的传染时间为0
    for m in range(len(nodes)):
        times[m][m]=0
    print(times)
    print(nodes)
    current_time = 0
    paths_time=[]
    row=nodes.index(k)
    print(row)
    
    """
    
    

    

    



if __name__=="__main__":
    VirusInfection()