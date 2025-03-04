"""
输入指令总和
输入幸运数字
输入指令列表
输出在整个游戏过程中，所处的最大的坐标值


"""
def maxsteps():
    N=int(input())
    lucky=int(input())
    lst=list(map(int,input().split()))
    step=0
    step_list=[0]
    for i in range(len(lst)):    
        if(lst[i]==lucky and lucky>0):
            step+=abs(lucky)+1
            step_list.append(step)
        if(lst[i]==lucky and lucky<0):
            step+=-(abs(lucky)+1)
            step_list.append(step)
        if(lst[i]!=lucky ):
            step+=lst[i]
            step_list.append(step)
    print(step_list)
    result = max(step_list)
    print(result)
    return result
    


if __name__=="__main__":
    maxsteps()