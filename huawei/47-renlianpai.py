"""
人力分配，本质就是保证人力分派的需求个数在2m内，同时需要保证M个月的人力分配是平均趋向的，然后取其最大值即可
此题跟25题目类似，都可以二分法回溯来实现

"""


def canFinish(tasks,k,limit):
    #创建一个数组来初始化每个月的任务量分配
    months=[0]*k
    #使用回溯法检测能完成任务在limit的人力分配下
    return backtrace(tasks,months,0,limit)

def backtrace(tasks,months,index,limit):
    if(index>=len(tasks)):
        return True
    #记录当前任务量大小
    current=tasks[index]
    #将当前任务分配给每一个月
    for i in range(len(months)):
        if(months[i]+current<=limit):
            months[i]+=current
            if(backtrace(tasks,months,index+1,limit)):
                return True
                #当mid值为10，8时，直接返回true了，else后面的不再执行跟if并齐的也不再执行
                #当mid值为7时，因为不满足if后面的条件，所以会继续else以及后面的模块。直至跳出循环
            else:
                months[i]-=current
            print("i,months[i]",i,months[i],limit)
        if(months[i]==0 or months[i]+current==limit):
            break
        


def meanlabordispatch():
    M=int(input())
    requirements=list(map(int,input().split()))
    N=len(requirements)
    if(N>2*M):
      return -1
    else:
        requirements.sort(reverse=True)
        l,r=requirements[0],sum(requirements)
        while l<r:
            print("l,r",l,r)
            mid=(l+r)//2
            if(canFinish(requirements,M,mid)):
                r=mid
            else:
                l=mid+1
        print(l)
        return l

if __name__=="__main__":
    meanlabordispatch()