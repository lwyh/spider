import numpy as np
import random

"""
待优化，从48----->24

"""

in1 = input()
arr1 = in1.split()
if len(arr1)== 3:
    N,M,K=  map(int,arr1)
else:
    print("输入格式错误")

    
print(N,M,K)

matrix=np.zeros((N,M),dtype=int)
for i in range(N):
    in2=input()
    arr2=in2.split(" ")
    for j in range(M):
        matrix[i][j]=int(arr2[j])

def extract_elements(matrix, n):
    if len(matrix) < n or len(matrix[0]) < n:
        return []  # 如果矩阵的行数或列数小于n，则无法选择n个元素

    #select_rows = []
    #select_cols = []
    result = []
    ans = []
    def is_valid(r, c, selected_rows, selected_cols):
        return r not in selected_rows and c not in selected_cols

    def backtrack(select_rows, select_cols,row, col,result):
        if len(result) == n:
            ans.append(list(result))  # 添加result的副本到ans
            return
        
        for r in range(row,len(matrix)):  # 遍历所有行
            for c in range(col,len(matrix[0])):  # 遍历所有列
                if is_valid(r,c,select_rows,select_cols):
                    result.append(matrix[r][c])
                    select_rows.append(r)
                    select_cols.append(c)
                    backtrack(select_rows,select_cols,r, c +1,result+[matrix[r][c+1]])  # 递归调用，注意这里的参数调整
                    result.pop()  # 回溯
                    select_cols.pop()
                    select_rows.pop()
                        

    
        backtrack([0],[0],0,0,[])
            

    
        print(ans)
        return ans


    out=0
    for i in range(len(ans)):
        min = sum(ans[0])
        if(sum(ans[i])<min):
            min=sum(ans[i])
            ans[i].sort(reverse=True)
            out = ans[i][K-1]
    print(out)
    return out
    



                    
      
if __name__ == '__main__':
    extract_elements(matrix, N)

