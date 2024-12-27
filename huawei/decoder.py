"""
明文中的数字串
密码本是一组二维数组
密文是找出明文中的数字串在密码本中出现的位置的较小字符位置，找不到的返回error


"""
import numpy as np
import itertools
def decoder():
    N=int(input())
    ming = list(map(int,input().split()))
    M=int(input())
    mimaben=np.zeros((M,M),dtype=int)
    arr=[]
    index_list=[]
    for i in range(M):
        arr.append(list(map(int,input().split())))
    arr = list(itertools.chain(*arr))
    print(arr)
    idxdict={}
    for k in range(len(ming)):
        if(ming[k] not in arr):
            #print("error")
            break
        for m in range(len(arr)):
            if(ming[k]==arr[m]):
                i=m//M
                j=m%M
                if(ming[k] not in idxdict):
                    idxdict[ming[k]]=[(i,j)]
                else:
                    idxdict[ming[k]].append((i,j))
        
           
    print(idxdict) 
    if(len(idxdict.keys())<len(ming)):
        print("error")
    else:
        for key ,values in idxdict.items():
            sorted_values = sorted(values,key = lambda item: (item[0],item[1]))
            min_value=sorted_values[0]
            print(f"{key}:{min_value}")
            index_list.append(list(min_value))
        out_list = list(itertools.chain(*index_list))
        #前提需要将列表元素变成字符类型
        print(' '.join(list(map(str,out_list))))


                



    



if __name__=="__main__":
    decoder()

    