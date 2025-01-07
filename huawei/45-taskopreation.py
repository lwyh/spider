"""
每天只能处理一个任务，第一行是task任务数量，第二行往后每行输入的是任务处理的开始时间和结束时间
输出在规定时间内可以处理的最大的任务数

"""

def taskopreation():
    tasks=int(input())
    durications=[]
    days=[]
    days_list=[]
    for i in range(tasks):
        durications.append(list(map(int,input().split())))
    print(durications)
    #此处主要是两点需要注意，采用的主要是以days为主，只要在这中间期间就能处理完，同时需要表示如果出现断层，需要将days续上
    for j in range(tasks):
        m=j+1
        if(m>=durications[j][0]  and m<=durications[j][1] ):
            days_list.append(m)
        else:
            for k in range(1,durications[j][0]):
                if(j+k==durications[j][0]):
                    m=j+k      
                    days_list.append(m)
        j=j+1
    print(len(days_list))
    return len(days_list)

 
if __name__=="__main__":
    taskopreation()  

    