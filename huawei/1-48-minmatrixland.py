"""
矩阵中的相同非零数字所覆盖的最小矩阵的面积中的最大值

"""
import numpy as np
def minmatrixland():
    lst=list(map(int,input().split()))
    m,n=lst[0],lst[1]
    matrix=np.zeros((m,n),dtype=int)
    for i in range(m):
        matrix[i]=list(map(int,input().split()))
    print(matrix)
    ele_dict=dict()
    for idx,ele in np.ndenumerate(matrix):
        if(ele !=0):
            if(ele in ele_dict):
                ele_dict[ele].append(idx)
            else:
                ele_dict[ele]=[idx]
    print(ele_dict)
    mianji=dict()
    if all(len(value)==1  for key,value in ele_dict.items()):
        print(1)
        return 1
    else:
        for key,value in ele_dict.items():
            start_list=[]
            end_list=[]
            if(len(value)>1):
                for i in range(len(value)):
                    start_list.append(value[i][0])
                    end_list.append(value[i][1])
            mianji[key]=(max(start_list)-min(start_list)+1)*(max(end_list)-min(end_list)+1)
    if(len(mianji)==1):
        opt=list(mianji.values())[0]
    else:
        opt = max(list(mianji.values()))
    print(opt)
    return 0
 
if __name__=="__main__":
    minmatrixland()