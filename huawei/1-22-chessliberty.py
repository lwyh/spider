"""

输入的是黑棋和白棋的坐标

"""
def chessliberty():
    black=list(map(int,input().split()))
    white=list(map(int,input().split()))
    black_nums=[]
    white_nums=[]
    for i in range(len(black)):
        if(i%2==0):
            black_nums.append([black[i],black[i+1]])
    for i in range(len(white)):
        if(i%2==0):
            white_nums.append([white[i],white[i+1]])
    print(black_nums,white_nums)
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    #不重复状态的黑白棋需要分开
    black_visited=black_nums+white_nums
    white_visited=black_nums+white_nums
    black_liberty=0
    white_liberty=0
    for row,col in black_nums:
        for dx,dy in directions:
            nx,ny=row+dx,col+dy
            if(nx>=0 and nx<=18 and ny>=0 and ny<=18 and [nx,ny] not in black_visited ):
                black_liberty+=1
                black_visited.append([nx,ny])
    for row,col in white_nums:
        for dx,dy in directions:
            nx,ny=row+dx,col+dy
            if(nx>=0 and nx<=18 and ny>=0 and ny<=18 and [nx,ny] not in white_visited ):
                white_liberty+=1
                white_visited.append([nx,ny])

    print(black_liberty,white_liberty)
    #分开直行因为black_visited，white_visited已经发生变化，新增了各自的气
    def liberty_nums(lst,directions,visited,liberty):
        for row,col in lst:
            for dx,dy in directions:
                nx,ny=row+dx,col+dy
                if(nx>=0 and nx<=18 and ny>=0 and ny<=18 and [nx,ny] not in visited ):
                    liberty+=1
                    visited.append([nx,ny])
        print(liberty)
        return liberty
    black_liberty=liberty_nums(black_nums,directions,black_visited,0)
    white_liberty=liberty_nums(white_nums,directions,white_visited,0)  
    print(black_liberty,white_liberty)   

   

if __name__=="__main__":
    chessliberty()
    



        


