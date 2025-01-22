"""
妈妈到达宝宝的所有路径中，路径最短，糖果最多
dfs中
-3表示妈妈位置
-2表示宝宝位置
-1表示障碍物
k>=0表示可以通行，0表示没有糖果，k表示可以捡到k颗糖果

"""
import numpy as np
def maxcandy():
    N=int(input())
    matrix=np.zeros((N,N),dtype=int)
    for i in range(N):
        matrix[i]=list(map(int,input().split()))
    print(matrix)
    def dfs_short_path(matrix,x,y,x2,y2,path,visited,direction):
        path.append((x,y))
        if((x,y)==(x2,y2)):
            return [path.copy()]
        visited.add((x,y))


        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        paths=[]
        direction_paths=[]

        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            #需要包括终点位置matrix元素为-2
            if(nx>=0 and nx <len(matrix) and ny>=0 and ny<len(matrix[0]) and (nx,ny) not in visited and (matrix[nx][ny]>=0  or matrix[nx][ny]==-2 )):
                new_direction=(dx,dy)
                new_path=path.copy()
                new_visited=visited.copy()
                new_directions=direction+[new_direction]
                new_paths = dfs_short_path(matrix,nx,ny,x2,y2,new_path,new_visited,new_directions)
                for new_path in new_paths:
                    if(new_path):
                        paths.append(new_path)
        
        path.pop()
        visited.remove((x,y))

        return paths

    for idx,item in np.ndenumerate(matrix):
        if(item==-3):
            start=idx
        if(item==-2):
            end=idx
    print(start,end)
    all_paths = dfs_short_path(matrix,start[0],start[1],end[0],end[1],[],set(),[])
    print("all_paths",all_paths)
    candy_list=[]
    candy_num=[]
    if(len(all_paths)==0):
        print(-1)
        return -1
    elif(len(all_paths)==1):
        path = all_paths[0]
        for i in range(len(path)):
            candy_list.append(matrix[path[i][0]][path[i][1]])
        candy = sum(candy_list)
        print(candy)
        return candy
    else: 
        minpath=min(len(path) for path in all_paths)
        avialble_paths=[sublist for sublist in all_paths if len(sublist)==minpath]
        if(len(avialble_paths)==1):
            candy= sum(matrix(avialble_paths[0][i]) for i in range(len(avialble_paths[0])))
        if(len(avialble_paths)>1):
            for j in range(len(avialble_paths)):
                for i in range(1,len(avialble_paths[j])-1):#起点和终点位置不是糖果的数量，需要去掉
                    print(avialble_paths[j][i],matrix[avialble_paths[j][i][0]][avialble_paths[j][i][1]])
                    candy_list.append(matrix[avialble_paths[j][i][0]][avialble_paths[j][i][1]])
                candy_num.append(sum(candy_list))
                candy_list=[]
            maxcandy= max(candy_num)
            print(maxcandy,"maxcandy")
        return maxcandy

if __name__=="__main__":
    maxcandy()

            


