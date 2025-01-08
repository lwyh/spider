"""
马跳日，k级马跳的步数是k,如果能在k步内所有马能跳到同一位置，将所有马跳的步数相加即可，如果不能到达同一位置则返回-1
如果第i，j列代表的元素为.，代表此格没有棋子，如果为数字k(1<=k<=9),则代表此格点存在等级为k的马
"""
import numpy as np
from collections import deque
def horsesteps():
    arry1=list(map(int,input().split()))
    m,n=arry1[0],arry1[1]
    string=[]
    nonlist=[]
    matrix=np.zeros((m,n),dtype=int)
    for i in range(m):
        string.append(input())
    for j in range(len(string)):
        for k in range(len(string[j])):
            if(string[j][k]!='.'):
                matrix[j][k]=int(string[j][k])
    print(matrix)
    
    visited=set()
    nonkey_dict=dict()
    endkey_dict=dict()
    avialble_paths=[]
    """
    for i in range(m):
        for j in range(n):#终点位置
    """
     #设置任意两点之间的路径是否存在，并输出所有不重复的路径
    def dfs(matrix,x,y,x2,y2,path,visited,direction):
        #print("(x,y)目前的坐标是",(x,y))
        #将当前坐标添加到路径中
        path.append((x,y))
        
        #如果到达目的地，返回包含当前路径的列表
        if((x,y)==(x2,y2)):
            return [path.copy()]
        #标记当前坐标为已访问
        visited.add((x,y))
        
       

        #定义可能的移动方向（上下左右）
        directions = [(1,2),(2,1),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        paths=[]
        directions_paths=[]

        #尝试所有可能的移动方向
        for dx,dy in directions:
            nx,ny = x+dx,y+dy

            #检查新坐标是否在矩阵范围内，未被访问过，且从起点开始移动的步数不超过k
            if(nx>=0 and ny>=0 and nx<len(matrix) and ny<len(matrix[0]) and (nx,ny) not in visited ):
                #标记当前方向
                new_direction=(dx,dy)
                #复制当前的访问状态
                new_visited=visited.copy()
                #复制当前路径
                new_path=path.copy()
                #记录新的方向
                new_directions=direction+[new_direction]
                #print(new_direction,new_path,new_directions)
                #print(new_visited)
                new_paths = dfs(matrix,nx,ny,x2,y2,new_path,new_visited,new_directions) 
                for new_path in new_paths:
                    if new_path:#确保路径不为空
                        paths.append(new_path)         

        #从当前坐标移除，以便回溯
        path.pop()#确保在回溯是移除最后一个点
        visited.remove((x,y))#确保在回溯时将当前点标记为未访问

        return paths
    for mm in range(m):
        for nn in range(n):
            for (x,y),item in np.ndenumerate(matrix):
                if(item!=0):
                    paths = dfs(matrix,x,y,mm,nn,[],set(),[]) 
                    if(len(paths)==1):
                        nonkey_dict[(x,y)]=0
                    else:
                        for i in range(len(paths)):
                            if(len(paths[i])-1<=item):
                                print(paths[i])
                                avialble_paths.append(paths[i])
                            if(len(avialble_paths)==0):
                                nonkey_dict[(x,y)]=-1
                            if(len(avialble_paths)==1):
                                nonkey_dict[(x,y)]=len(avialble_paths[0])-1
                            if(len(avialble_paths)>1):
                                print(avialble_paths)
                                nonkey_dict[(x,y)]=min(len(avialble_paths[j]) for j in range(len(avialble_paths)))-1
                    avialble_paths=[]
            print(nonkey_dict,"nonkey_dict")
            if(-1 in nonkey_dict.values() ):
                endkey_dict[(mm,nn)]=-1
            else:
                endkey_dict[(mm,nn)]=sum(nonkey_dict.values())
            print(endkey_dict,"endkey_dict")
    filtered_dict = {k: v for k, v in endkey_dict.items() if v != -1}
    if(len(filtered_dict)==1):
        out=filtered_dict.values()
    else:
        out=min(filtered_dict.values())
    print(out,"out")

"""

    for (x,y),item in np.ndenumerate(matrix):
        #print((x,y),item)
        if(item!=0):
            queue=deque([(x,y,0)])#起点以及步数
            visited=set()
            visited.add((x,y))
            while queue :
                print("1",queue)
                print("visited",visited)
                x,y,steps = queue.popleft()
                print(x,y,steps)
                print("nonkey_dict",nonkey_dict)
                #print("(i,j)",i,j)
                if( (x,y)==(0,0) and steps<=item): 
                    print("step01",x,y,steps,item)
                    print("queue1",queue)  
                    if((x,y) not in nonkey_dict):
                        nonkey_dict[(x,y)]=steps
                    else:
                        nonkey_dict[(x,y)]+=steps  
                    # print("pass",x,y,steps)
                    print("pro",nonkey_dict)
                    visited=set()
                    visited.add((x,y))
                    continue
                for dx,dy in directions:   
                    nx,ny= x+dx,y+dy
                    if(nx>=0 and nx<m and ny>=0 and ny<n and (nx,ny) not in visited):
                        visited.add((nx,ny))
                        queue.append((nx,ny,steps+1))


            print("nonkey_dict",nonkey_dict)

       if(-1 in nonkey_dict.values()):
                endkey_dict[(i,j)]=-1
            else:
                endkey_dict[(i,j)]=sum(nonkey_dict.values())
    print("endkey_dict",endkey_dict)
    if(-1 in endkey_dict.values()):
        return -1
    else:
        out = min(endkey_dict.values())
        return out             



"""
     
if __name__=="__main__":
    horsesteps()




