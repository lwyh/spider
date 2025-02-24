"""
输入第一行是GPU一次直行的任务个数
第二行是数组的任务数组长度
第三行是任务数组
输出直行完所有任务的耗时，在GPU不空闲的情况下
"""
def GPUtime():
    N=int(input())
    length=int(input())
    lst=list(map(int,input().split()))
    time=0
    reminder=0
    #分情况讨论各任务数组的秒数
    for i in range(len(lst)):  
        reminder+=lst[i]  
        if(reminder<N):
            time+=1
            continue
        if(reminder>=N):
            time+=1 
            reminder-=N
            continue
    #最后一组reminder数会影响消耗time数
    if(reminder%N==0):
        time+=reminder//N
    else:
        time+=reminder//N+1
    print(time)
    return time
if __name__=="__main__":
    GPUtime()


