"""
从一个点到另一个点的最短时间，dfs深度优先算法
每次选出一条完整的路径出来，然后计算每条路径的通过时间

"""

def minpassportTime():
    list1=list(input().split("]],"))
    matrix=list1[0]
    weight_point=list1[1]
    list2=matrix.strip("[]").split('],')
    lights=[]
    for i in range(len(list2)):
        lights.append(list(map(int,list2[i].strip("[]").split(','))))
    print(lights)
    list3 = list(map(int,weight_point.split(",")))
    timePerRoad,rowStart,colStart,rowEnd,colEnd=list3[0],list3[1],list3[2],list3[3],list3[4]
    
    print(timePerRoad,rowStart,colStart,rowEnd,colEnd)
    if ((colStart==colEnd and abs(rowStart-rowEnd)==1) or (rowStart==rowEnd and abs(colStart-colEnd)==1) ):
        return timePerRoad

    def dfs(lights,rowStart,colStart,rowEnd,colEnd,path,visited,direction):
        path.append((rowStart,colStart))
        timelist=[]
        if ((rowStart,colStart)==(rowEnd,colEnd)):
            time=0
            print("path,direction",path,direction)
            time+=timePerRoad*(len(path)-1)
            #对每次的完整的path以及direction进行下一步的处理
            for i in range(len(direction)-1):

                #右转
                if((direction[i]==(0,1) and direction[i+1]==(1,0))
                or (direction[i]==(0,-1) and direction[i+1]==(-1,0))
                or (direction[i]==(1,0) and direction[i+1]==(0,-1))
                or (direction[i]==(-1,0) and direction[i+1]==(0,1))):
                    time+=0
                #左转或者直行
                else:
                    row,col=path[i+1]
                    time+=lights[row][col]

            print("time",time)
            timelist.append(time)

            return [path.copy()],[direction.copy()],[timelist.copy()]
        visited.add((rowStart,colStart))

        #定义可能的移动方向
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        paths=[]
        directions_paths=[]
        times=[]
        

        for dx,dy in directions:
            nx,ny= rowStart+dx,colStart+dy
            if(nx>=0 and ny>=0 and nx<len(lights) and ny<len(lights[0]) and (nx,ny) not in visited):
                new_direction=(dx,dy)
                new_visited=visited.copy()
                new_path=path.copy()
                new_directions=direction+[new_direction]
                new_paths,new_directions,timelist=dfs(lights,nx,ny,rowEnd,colEnd,new_path,new_visited,new_directions)
                for new_path in new_paths:
                    if new_path:
                        paths.append(new_path)
                for new_direction in new_directions:
                    if new_direction:
                        directions_paths.append(new_direction)
                for time in timelist:
                    if time:
                        times.append(time)

        path.pop()
        visited.remove((rowStart,colStart))
       
        return paths,directions_paths,times


    result= dfs(lights,rowStart,colStart,rowEnd,colEnd,[],set(),[])
    #将方向输出
    if result:
        paths=result[0]
        directions_paths=result[1]
        times=result[2]
        print("paths",paths)
        print("directions_paths",directions_paths)
        print("time",times)
        min_time=min([item for sublist in times for item in sublist])

    print(min_time)
    return min_time
        


if __name__=="__main__":
    minpassportTime()