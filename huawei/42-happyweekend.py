"""
地图中0表示畅通
1表示障碍物
2表示人，可以化为0，畅通
3表示聚餐地也称目的地
也可以理解1和非1，只要1的地方没有挡住人和目的地就可以聚餐成功


"""
import numpy as np
import itertools
def happyweekend():
    j_col=[]
    arr=list(map(int,input().split()))
    m,n=arr[0],arr[1]
    map1= []
    matrix=np.zeros((m,n),dtype=int)
    for i in range(m):
        map1.append(list(map(int,input().split())))
    map_list=list(itertools.chain(*map1))
    #将map转化为matrix
    for k in range(len(map_list)):
        i=k//m
        j=k%m
        matrix[i][j]=map_list[k]
    print(matrix)
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
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        paths=[]
        directions_paths=[]

        #尝试所有可能的移动方向
        for dx,dy in directions:
            nx,ny = x+dx,y+dy

            #检查新坐标是否在矩阵范围内，未被访问过，且不是障碍物1
            if(nx>=0 and ny>=0 and nx<len(matrix) and ny<len(matrix[0]) and (nx,ny) not in visited and matrix[nx][ny]!=1 ):
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
    starts=[]
    ends=[]
    #值为2表示人的起点，值为3表示聚餐目的地
    for (x,y),item in np.ndenumerate(matrix):
        if(item==2):
            starts.append((x,y))
        if(item==3):
            ends.append((x,y))
    print(starts)
    num_start=len(starts)
    print(ends)
    target=0
    for end in ends:
        num=0
        for start in starts:
            paths =  dfs(matrix,start[0],start[1],end[0],end[1],[],set(),[])
            for path in paths:
                print(path)
            if(len(paths)!=0):
                num+=1
        if(num_start==num):
            target+=1
    print(target)
    return target
if __name__=="__main__":
    happyweekend()


    

        