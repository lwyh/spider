"""
题目描述

LYA开发了一款智能驾驶系统,可以让汽车在 M×NM×N 的地图上从左上角(起点)开往右下角(终点)。地图上的每个位置都有一个数字,表示汽车经过该位置需要消耗的油量。地图上还有一些加油站,汽车经过加油站时可以加满油。

LYA想知道,汽车从起点出发,确保能够到达终点,初始时油箱里至少需要多少油量。

注意:

    汽车可以向上、下、左、右四个方向行驶。
    地图上的数字含义如下:
        −1−1:表示该位置是加油站,汽车经过时可以将油箱加满,油箱容量为100。
        00:表示该位置是障碍物,汽车无法通过。
        正整数:表示汽车经过该位置需要消耗的油量。
    如果无论初始油量多少,汽车都无法到达终点,则输出 −1。
"""
import numpy as np
import itertools
def throughend():
    M,N=list(map(int,input().split(",")))
    matrix = np.zeros((M,N),dtype=int)
    for i in range(M):
        matrix[i]=list(map(int,input().split(",")))
    print(matrix,"matrix")
    #路径函数
    def bfs_short_path(matrix,x1,y1,x2,y2,path,visited,direction):
        path.append((x1,y1))
        if((x1,y1)==(x2,y2)):
            print("path",path)
            return [path.copy()]
        visited.add((x1,y1))
        paths=[]
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for dx,dy in directions:
            nx,ny=x1+dx,y1+dy
            if(nx>=0 and nx<len(matrix) and ny>=0 and ny<len(matrix[0]) and (nx,ny) not in visited and matrix[nx][ny]!=0):
                new_direction=(dx,dy)     
                new_path=path.copy()
                new_visited=visited.copy()
                new_directions=direction+[new_direction]
                new_paths =bfs_short_path(matrix,nx,ny,x2,y2,new_path,new_visited,new_directions)
                for new_path in new_paths:
                    if(new_path):
                        paths.append(new_path)
        
        path.pop()
        visited.remove((x1,y1))

        return paths
    #列表值切分函数
    def split_list_by_value(lst,split_value):
        result=[]
        for key,group in itertools.groupby(lst,key=lambda x:x==split_value):
            if not key:
                result.append(list(group))
        return result

    #输出路径和方向
    paths = bfs_short_path(matrix,0,0,M-1,N-1,[],set(),[])
    print(paths)
    sum_list=[]
    start_list=[]
    for path in paths:
        print(path) 
        #路径中没有-1的加油站
        if all(matrix[path[j][0]][path[j][1]]!=-1 for j in range(len(path)) ):
            sum_list.append(sum(matrix[path[j][0]][path[j][1]]  for j in range(len(path))))
            print("sum_list",sum_list)
            print("paths",len(paths))
            if all(element>100 for element in sum_list):
                paths.remove(path)
            else:
                start_list.append(sum_list[0])
            print("paths",len(paths))
        #路径中含有-1的加油站
        if any(matrix[path[j][0]][path[j][1]] ==-1 for j in range(len(path))):
            print("-111111111111111111111111111",path)
            #路径中有某段路的油耗量大于100，去掉该路径
            value_matrix_list=[matrix[path[j][0]][path[j][1]] for j in range(len(path))]
            result = split_list_by_value(value_matrix_list,-1)
            print("result",result)
            for sublist in result:
                print("sublist",sublist)
                sum_list.append(sum(ele   for ele in sublist ) )
            print("sum_list",sum_list)
            print("paths",len(paths))
            if any(sum_list[m]>100 for m in range(len(sum_list))):
                paths.remove(path)
            else:
                start_list.append(sum_list[0])
            print("paths",len(paths))    
        sum_list=[]
    if(len(start_list)==0):
        print(-1)
        return -1
    else:
        minsum=min(start_list)
        print("minsum",minsum)
        return minsum
            



if __name__=="__main__":
    throughend()

    


                





