"""
从一个N*M的矩阵中找出第K大的数，矩阵的每一行元素都是从小到大排列的。


"""


import numpy as np
import random



def matrix_complicated():
    in1 = input()
    arr1 = in1.split()
    if len(arr1)== 3:
        N,M,K=  map(int,arr1)
    else:
        print("输入格式错误")

    
    print(N,M,K)
  
    
   # N = int(arr1[0]) #矩阵的行数
   # M = int(arr1[1]) #矩阵的列数
   # K = int(arr1[2])  #第K大数

   # print(N,M,K)
  #初始化空的数组
    matrix=np.zeros((N,M),dtype=int)
    for i in range(N):
        in2=input()
        arr2=in2.split(" ")
        for j in range(M):
            matrix[i][j]=int(arr2[j])


    print(matrix)

    rows = len(matrix)
    cols = len(matrix[0]) if rows>0 else 0
    picked_element = []
    used_rows = set()
    used_cols = set()



    while(len(picked_element)<N):  
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if row in used_rows or col in used_cols:
            continue
        picked_element.append(matrix[row][col])
        used_rows.add(row)
        used_cols.add(col)
    print(picked_element)

    

   
    



    return picked_element

    



if __name__ == '__main__':
    matrix_complicated()

