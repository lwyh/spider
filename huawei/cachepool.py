"""
内存池的操作分为request和release两种，request表示请求内存的大小，输出是的请求的内存块的首地址
当内存不足或指定请求大小为0时，输出error
release表示释放内存的首地址，释放成功则无需输出，如果释放不存在的首地址则输出error
内存池地址分配必须是连续内存，并优先从低地址分配

"""

def cachepool():
    first_end=[]
    N=int(input())
    arr=[]
    free=[[0,100]]
    used=[]
    current_start=0
    start2=0
    select_list=[]
    for i in range(N):
        arr.append(list(input().split("=")))
    print(arr)
        #输出释放不存在的首地址,地址内存大小为末地址，首尾地址是[start,end]
    for i in range(len(arr)):
        if(arr[0][0]=="RELEASE"):
            print("ERROR")
        if(arr[i][0]=="REQUEST"):
            if(i==0):
                if(int(arr[i][1])>free[0][1] or  int(arr[i][1])==0):
                    print("ERROR")
                else: 
                    used.append([0,int(arr[i][1])])
                    print("used1",used[0][0])
                    free.pop()
                    free.append([int(arr[i][1]),100])
            if(i>0):
                if(int(arr[i][1])>100 or  int(arr[i][1])==0):
                    print("ERROR")
                else:
                    print("free",free)
                    for start ,end in free:
                        if(int(arr[i][1]) <= end-start):
                            select_list.append([start,end])
                            select_list.sort(key=lambda x: x[0])
                    #选出所有可分配的内存后，需要将没有被分配的这个块空间置为空
                    print("select_list",select_list)
                    #当有其他之前释放的更大的空间可申请时，优先是申请较低的存储地址
                    if(len(select_list)==1 and select_list[0][1]!=100):
                        used.append(select_list[0])
                        free.remove(select_list[0])
                        used.sort(key=lambda x: (x[0],x[1]))
                        free.sort(key=lambda x: (x[0],x[1]))
                        select_list=[]
                    #当只有一块空间可用时，需要更新可用内存
                    if(len(select_list)==1 and select_list[0][1]==100):
                        used.sort(key=lambda x: (x[0],x[1]))
                        print("used2",used)
                        print("used3",used[-1][1])
                        used.append([used[(len(used)-1)][1],used[(len(used)-1)][1]+int(arr[i][1])])  
                        #更新可用内存操作
                        start2=used[-1][1]
                        free.pop()
                        free.append([start2,100])
                        select_list=[]
                    #当有其他的可用内存时，优先低地址的内存存储
                    if(len(select_list)>1):
                        used.append(select_list[0])
                        print("used4",select_list[0][0])
                        free.remove(select_list[0])
                        used.sort(key=lambda x: (x[0],x[1]))
                        free.sort(key=lambda x: (x[0],x[1]))
                        select_list=[]

        if(i>0 and arr[i][0]=="RELEASE"):
            for start ,end in used:
                if(start == int(arr[i][1])):
                    used.remove([start,end])
                    free.append([start,end])
                    free.sort(key=lambda x: x[0])
                else:
                    print("ERROR")
            current=free[0][1]
            for start,end in free:
                if(start==current):
                    free.remove([free[0][0],current])
                    free.remove([current,end])
                    free.append([free[0][0],end])

   



    return 1

if __name__ =="__main__":
    cachepool()