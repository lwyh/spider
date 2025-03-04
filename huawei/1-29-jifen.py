"""
积分任务
第一行为任务处理数
第二行为可用于处理任务的时间
接下来的N行表示两个空格分隔的整数（sla,V)
表示任务的最晚处理时间和积分
输出在可用处理任务的时间内，获取的最多积分

"""
def jifen():
    N=int(input())
    T=int(input())
    jifen=[]
    for i in range(N):
        jifen.append(list(map(int,input().split())))
    print(jifen)
    part_jifen=dict()
    for start,end in jifen:
        if(start<=T and start not in part_jifen):
            part_jifen[start]=[end]
        if(start<=T and start  in part_jifen):
            part_jifen[start].append(end)
    sumjifen=0
    for key,value in part_jifen.items():
        if(len(value)==1):
            sumjifen+=value[0]
        if(len(value)>1):
            sumjifen+=max(value)
    print(sumjifen)
    return sumjifen
if __name__=="__main__":
    jifen()




