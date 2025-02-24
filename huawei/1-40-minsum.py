"""
从两对升序的数组中各取出一个元素，组成一队元素，类似的取出k对元素，
输出k对元素的最小求和值


"""
import itertools
import numpy as np
def minsum():
    array1=list(map(int,input().split()))
    array2=list(map(int,input().split()))
    k=int(input())
    array1.sort()
    array2.sort()
    def create_matrix(lst1,lst2):
        matrix=[]
        for i in lst1:
            row=[]
            for j in lst2:
                row.append((i,j))
            matrix.append(row)
        return matrix
    matrix=create_matrix(array1,array2)
    print(matrix)
    #flatten=np.array(matrix).flatten()
    #展平的列表的程度需要多加注意
    flatten = [ele for sublist in matrix for ele in sublist]
    print(flatten)
    all_combinations=itertools.combinations(flatten,k)
    result=[]
    for pair in all_combinations:
        #print(pair,"pair")
        sum_list=sum(sum(t) for t in pair)
        result.append(sum_list)
    print(result)
    minsum=min(result)
    print(minsum)
    return minsum

if __name__=="__main__":
    minsum()