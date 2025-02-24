"""
从总堆内存归固定的空间，已分配的空间 已输入
第一行是新申请空间的内存字节数
输出新申请空间的偏移地址


"""
def memeory():
    N=int(input())
    lst=[]
    while True:
        line = input()    
        if(line.strip()==""):
            break
        lst.append(list(map(int,line.split())))
    print("111",lst)
    used_space=[]
    for i in range(len(lst)):
        used_space.append([lst[i][0],lst[i][0]+lst[i][1]])
    print(used_space)
    split_combination=[ele for sublist in used_space for ele in sublist]
    print("split_combination",split_combination)
    split_combination.append(100)
    print("split_combination",split_combination)
    #此处在去重后由于set的无序性，所以需要重新排下序
    split_combination=sorted(list(set(split_combination)))
    interval_list=[]
    for k in range(len(split_combination)-1):
        interval_list.append([split_combination[k],split_combination[k+1]])
    free_space=[ele for ele in interval_list if ele not in used_space ]
    print(free_space,"free_space")
    avialble_space=[]
    for start,end in free_space:
        if(end-start>=N):
            avialble_space.append(start)
    if(len(avialble_space)==0):
        print(-1)
    if(len(avialble_space)==1):
        print(avialble_space[0])
    if(len(avialble_space)>1):
        print(min(avialble_space))
    return 0
    
    





    
if __name__=="__main__":
    memeory()
        


    
