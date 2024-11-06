"""
图像像素1，5分别代表两种物体，像素1代表物体的个数，

"""
import numpy as np
def edege():
    M,N = map(int,input().split())
    print(M,N)

    matrix = np.zeros((M,N),dtype=int)
    for i in range(M):
            matrix[i]=list(map(int,input().split()))

    print(matrix)

    position=tuple()
    list_ege=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==5):
                position=(i,j)
                list_ege.append(position)

    print(list_ege)

    count=1
    for i in range(len(list_ege)):
        if(i+1<len(list_ege) and (list_ege[i+1][0]-list_ege[i][0]>=4 or list_ege[i+1][1]-list_ege[i][1]>=4)):
            count +=1

    print(count)
    return(count)



    




if __name__ == '__main__':
    edege()
                
