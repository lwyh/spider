"""
项目排期，M个独立需求，N个开发人员，求完成任务最短时间

"""

from collections import Counter



def canFinish(tasks,k,limit):

        #创建一个数组来记录员工worker的工作量
    workers=[0]*k
        #使用回溯法检验能否完成
    return backtrack(tasks,workers,0,limit)
    
def backtrack(tasks,workers,index,limit):
        #如果所有任务都已分配，则返回true
    if index>=len(tasks):
        return True
        
        #获取当前任务工作量
    current=tasks[index]
        #尝试将当前任务分配给每个员工
    for i in range(len(workers)):
            #如果当前员工可以在限制时间内完成这项任务
        if(workers[i]+current<=limit):
                #分配当前任务给该名员工
            workers[i]+=current
                #继续尝试分配下一个任务
            if(backtrack(tasks,workers,index+1,limit)):
                return True
            #回溯取消
            else:
                workers[i]-=current

            #print(workers[i])
        print(i,workers[i])
        if(workers[i]==0 or workers[i]+current==limit):
                break

    return False
def mininterval(tasks,k):
    tasks.sort(reverse=True)
    l,r=tasks[0],sum(tasks)
    print(l,r)
    while l<r:
        mid = (r+l)//2
        if(canFinish(tasks,k,mid)):
            r=mid
        else:
            l=mid+1
        print(l,r,mid)
    return l


    

    


if __name__=="__main__":
    tasks=list(map(int,input().split()))
    N=int(input())
    print(mininterval(tasks,N))



        

        





        


                















