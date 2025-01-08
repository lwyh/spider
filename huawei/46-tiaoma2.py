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
    directions = [(1,2),(2,1),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    nonkey_dict=dict()
    endkey_dict=dict()
    avialble_paths=[]
    


    
    for i in range(m):
        for j in range(n):#终点位置
            visited=set()
            #这个外层循环标志的位置也很重要，之前放在i最外层，导致每次只取一个非零值就到最外层了
            outer_break = False
            for (x,y),item in np.ndenumerate(matrix):
                print("00000",(x,y),item)
                if(item !=0):
                    queue=deque([(x,y,0)])#起点位置以及步数
                    visited.add((x,y))
                    while queue :
                        print("1",queue)
                        print("visited",visited)
                        #从队列的栈顶拿出数据进行下一步跳马行动
                        x,y,steps = queue.popleft()
                        print(x,y,steps)
                        print("nonkey_dict",nonkey_dict)
                        #print("(i,j)",i,j)
                        
                        #只将符合条件的最早到达终点的路径的步数相加，就继续走下一个非零的马点
                        if( (x,y)==(i,j) and steps<=item): 
                            print("step01",x,y,steps,item)
                            print("queue1",queue)  
                            if((x,y) not in nonkey_dict):
                                nonkey_dict[(x,y)]=steps
                            else:
                                nonkey_dict[(x,y)]+=steps  
                            # print("pass",x,y,steps)
                            print("pro",nonkey_dict)
                            visited=set()
                            break
                        if( (x,y)==(i,j) and steps>item):
                            nonkey_dict[(x,y)]=-1
                            outer_break = True  #外层循环标志
                            break

                        for dx,dy in directions:   
                            nx,ny= x+dx,y+dy
                            if(nx>=0 and nx<m and ny>=0 and ny<n and (nx,ny) not in visited):
                                visited.add((nx,ny))
                                queue.append((nx,ny,steps+1))
            
                        
                    if(outer_break):
                        break
                         
                

                        
    #nonkey_dict 这个就存储了到达不同终点的所有马跳步数之和最小值
    #还需要补充nonkey_dict中永远也到达不了的点的值
    for (x,y),item in np.ndenumerate(matrix):
         if((x,y) not in nonkey_dict):
            nonkey_dict[(x,y)]=-1
            print('===========')
    
    print("nonkey_dict",nonkey_dict)

    filtered_dict = {k: v for k, v in nonkey_dict.items() if v != -1}
    out = min(filtered_dict.values())
    print(out)           



     
if __name__=="__main__":
    horsesteps()




