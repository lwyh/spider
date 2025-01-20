"""
分月饼的规则：m个员工，n个月饼，问有多少种分月饼的方法，
人不做特定标记，每人分到的月饼个数不超过3，输出所有的组合

公平分配，随机分配，按需分配：点击链接查看和 Kimi 智能助手的对话 https://kimi.moonshot.cn/share/cu4iq6g7aa3b8p9lped0


"""
def splitmooncake():
    list1=list(map(int,input().split()))
    m,n = list1[0],list1[1]
    distribution_set=set()
    set_ele=set()
    def distribution(m,n):
        def helper(remaining,index,current_distribution):
            #所有物品分发完毕,记录当前分配方式
            if(remaining==0):
                result.append(current_distribution[:])
            #已经分发到m人,但是还有剩余物品
            if(index==m):
                return
            #对当前人的分发剩余的物品数量
            for i in range(remaining+1):
                current_distribution[index]+=i
                helper(remaining-i,index+1,current_distribution)
                current_distribution[index]-=i #进行回溯
        result=[]
        helper(n-m,0,[1]*m)
        print(result)
        return result

    all_distribution = distribution(m,n)
    print(all_distribution)
    distribution_set =  {frozenset(distribution)  for distribution in all_distribution} 
    print(distribution_set)
    #还需要加层过滤
    #元素中相邻元素相差不超过3
    list_unique=[]
    list_unique = [list(s) for s in distribution_set]
    print(list_unique,"list_unique")
    types=0
    for i in range(len(list_unique)):
        count=0
        if(len(list_unique[i])==1):
                types+=1
        else:
            list_unique[i].sort() #这样方便将第一小，第二小，升序排序，后序判断方便
            for j in range(1,len(list_unique[i])):
                if(list_unique[i][j]-list_unique[i][j-1]>3):
                    break
                else:
                    count+=1
                if(count==len(list_unique[i])-1):
                    types+=1

    print(types)
    return types




if __name__=="__main__":
    splitmooncake()