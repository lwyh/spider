"""
输入averageTime
数组

"""
def minaverageTime():
    averageTime=int(input())
    lst=list(map(int,input().split()))
    interval=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            #需要分两种情况讨论
            if(j+1 <len(lst) and sum(lst[i:j+1])/(j+1-i)<=averageTime):
                interval.append([i,j])    
            if(j+1 >=len(lst) and sum(lst[i:])/(len(lst)-i)<=averageTime):
                interval.append([i,len(lst)-1])
    print(interval)
    #需要对数组进行排序
    sorted_interval= sorted(interval,key=lambda item:(item[0],-(item[1]-item[0])))
    current_end=0
    available_lst=[]
    #过滤掉相同起点时的较短的时间序列
    for start,end in sorted_interval:
        if(start>=current_end):
            available_lst.append([start,end])
            current_end=end
    print("available_lst",available_lst)
    #输出格式
    out_lst=["-".join(map(str,sublist)) for sublist in available_lst ]
    out = " ".join(out_lst)
    print(out)
    return out

if __name__=="__main__":
    minaverageTime()
    exit()










if __name__=="__main__":
    minaverageTime()