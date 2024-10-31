import numpy as np

"""


"""

def matrix_complicated():
    in1 = input()
    arr1 = in1.split(" ")
    N = int(arr1[0])  #矩阵的行数
    M = int(arr1[1])  #矩阵的列数
    K = int(arr1[2])  # 矩阵的维度

    #print(N,M,K)
  #初始化空的数组
    matrix=np.zeros((N,M),dtype=int)
    for i in range(N):
        in2=input()
        arr2=in2.split(" ")
        for j in range(M):
            matrix[i][j]=int(arr2[j])

    print(matrix)


    return matrix


if __name__ == '__main__':
    matrix_complicated()

