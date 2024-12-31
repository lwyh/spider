"""
每一步的数字都是往它的上下左右中信号值最好的一步走，求所有走过的路径的最小值


"""
import numpy as np

def maxroute():
    R=int(input())
    C=int(input())
    route=[]
    current=0
    select_mem=0
    matrix= np.zeros((R,C),dtype=int)
    for i in range(R):
        matrix[i]=list(map(int,input().split()))
    print(matrix)

    i=0
    j=0
    dict1=dict()
    dict2=dict()
    filter_dict=dict()
    key_list=[]
    route.append(matrix[0][0])
    dict2[(0,0)]=matrix[0][0]

    if(i==0 and j==0):
        if(matrix[i+1][j]>matrix[i][j+1]):
            route.append(matrix[i+1][j])
            i+=1
        if(matrix[i+1][j]<matrix[i][j+1]):
            route.append(matrix[i][j+1])
            j+=1
    print(route,i,j)
    dict2[(i,j)]=matrix[i][j]
    #print(list(dict2.items())[-2][0])
    while(i==0 and j>0 and j<C-1):
        dict1={(i,j-1):matrix[i][j-1],(i,j+1):matrix[i][j+1],(i+1,j):matrix[i+1][j]}
        filter_dict={key:value for key,value in dict1.items() if  key !=list(dict2.items())[-2][0]}
        key_list=[key for key ,value in filter_dict.items() if value==max(filter_dict.values())]
        i=key_list[0][0]
        j=key_list[0][1]
        route.append(max(filter_dict.values()))
        print(route,i,j)
        dict2[(i,j)]=matrix[i][j]
        print(dict2)
    
    
    if(i==0 and j==C-1):
        dict1={(i,j-1):matrix[i][j-1],(i+1,j):matrix[i+1][j]}
        filter_dict={key:value for key,value in dict1.items() if  key !=list(dict2.items())[-2][0]}
        key_list=[key for key ,value in filter_dict.items() if value==max(filter_dict.values())]
        i=key_list[0][0]
        j=key_list[0][1]
       

        route.append(max(filter_dict.values()))
        print(route,i,j)
        dict2[(i,j)]=matrix[i][j]
    while(i>0 and i<R-1 and j==C-1):
        dict1={(i-1,j):matrix[i][j-1],(i+1,j):matrix[i+1][j],(i,j-1):matrix[i][j-1]}
        filter_dict={key:value for key,value in dict1.items() if  key !=list(dict2.items())[-2][0]}
        key_list=[key for key ,value in filter_dict.items() if value==max(filter_dict.values())]
        i=key_list[0][0]
        j=key_list[0][1]
       

        route.append(max(filter_dict.values()))
        print(route,i,j)
        dict2[(i,j)]=matrix[i][j]

            
    while(i>0 and i<R-1  and j>0 and j<C-1):
        dict1={(i-1,j):matrix[i-1][j],(i,j-1):matrix[i][j-1],(i+1,j):matrix[i+1][j],(i,j+1):matrix[i][j+1]}
        filter_dict={key:value for key,value in dict1.items() if  key !=list(dict2.items())[-2][0]}
        key_list=[key for key ,value in filter_dict.items() if value==max(filter_dict.values())]
        i=key_list[0][0]
        j=key_list[0][1]

        route.append(max(filter_dict.values()))
        print("4444",route,i,j)
        dict2[(i,j)]=matrix[i][j]

    while(i>0 and i<R-1 and j==0):
        dict1={(i-1,j):matrix[i-1][j],(i,j+1):matrix[i][j+1],(i+1,j):matrix[i+1][j]}
        filter_dict={key:value for key,value in dict1.items() if  key !=list(dict2.items())[-2][0]}
        key_list=[key for key ,value in filter_dict.items() if value==max(filter_dict.values())]
        i=key_list[0][0]
        j=key_list[0][1]
        route.append(max(filter_dict.values()))
        print("j=0",route)
        dict2[(i,j)]=matrix[i][j]
    if(i==R-1 and j==0):
        dict1={(i-1,j):matrix[i-1][j],(i,j+1):matrix[i][j+1]}
        filter_dict={key:value for key,value in dict1.items() if  key !=list(dict2.items())[-2][0]}
        key_list=[key for key ,value in filter_dict.items() if value==max(filter_dict.values())]
        i=key_list[0][0]
        j=key_list[0][1]
        route.append(max(filter_dict.values()))
        print(route)
        dict2[(i,j)]=matrix[i][j]
    while(i==R-1 and j>0 and j<C-1):
        dict1={(i-1,j):matrix[i-1][j],(i,j+1):matrix[i][j+1],(i,j-1):matrix[i][j-1]}
        filter_dict={key:value for key,value in dict1.items() if  key !=list(dict2.items())[-2][0]}
        key_list=[key for key ,value in filter_dict.items() if value==max(filter_dict.values())]
        i=key_list[0][0]
        j=key_list[0][1]
        route.append(max(filter_dict.values()))
        dict2[(i,j)]=matrix[i][j]
        if(i==R-1 and j==C-1):
            break      
    print(route)
    route.sort()
    out=route[0]
    print(out)
    return out
if __name__ =="__main__":
    maxroute()



                













    

    












    






