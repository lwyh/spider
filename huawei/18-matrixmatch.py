import numpy as np
import random

"""


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

def extract_elements(matrix,n):
    select_rows=[]
    select_cols=[]
    result=[]
    ans=[]
    def backtrack(row,col,result):
        if(len(result)==n):
            
            
            ans.append(result[:])
           


           # print(result)
           # print(select_rows)
           # print(select_cols)
            return ans
        for r in range(row,len(matrix)):
            for c in range(col,len(matrix[0])):
                if r not in select_rows and c not in select_cols:
                    result.append(matrix[r][c])
                    select_rows.append(r)
                    select_cols.append(c)
                   # print("add: ",select_rows)
                    #print("add: ",select_cols)
                    backtrack(row,col+1,result)
                    result.pop()
                    select_cols.pop()
                    select_rows.pop()
                  #  print("pop: ",result)
                  #  print("pop: ",select_rows)
                  #  print("pop: ",select_cols)

    
    backtrack(0,0,result)       
    print(ans)

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

