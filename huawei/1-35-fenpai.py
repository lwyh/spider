"""
输入3行，第一行是数组个数
第二行是数组每个人的能力值
第三行是团队的最低能力值

"""
import itertools
def minunits():
    N=int(input())
    lst=list(map(int,input().split()))
    M=int(input())
    pre=[]
    for ele in lst:
        if(ele>=M):
            pre.append(ele)
    #除去一个人一个团队的元素
    lst = [ele for ele in lst if ele not in pre]
    print(pre,lst)
    """
    def all_combinations(lst):
        def helper(index,current):
            if(index==len(lst)):
                result.append(current[:])
                return
            helper(index+1,current)
            current.append(lst[index])
            helper(index+1,current)
            current.pop()

        result=[]
        helper(0,[])
        return result
    result = all_combinations(lst)
    print("result",result)
    
    """
    #剩下的是两个人组合的团队
    
    reminder=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if(lst[i]+lst[j]>=M):
                reminder.append([lst[i],lst[j]])
    print("reminder",reminder)
    result=[]
    numsteams=[]
    #将能组合成团队的整体最长链的组合输出
    for i in range(len(reminder)):
        result=[]
        result.append(reminder[i])  
        for j in range(i+1,len(reminder)):
            flat_list=[ele for sublist in result for ele in sublist]
            print("flat_list",flat_list)
            if(list(set(reminder[j])&set(flat_list))==[]):     
                result.append(reminder[j])
                print(result,"result222222")
        numsteams.append(result)
    print(numsteams)
    two_nums=max(len(numsteams[k]) for k in range(len(numsteams)))
    one_nums=len(pre)
    out=two_nums+one_nums
    print(out)
    return out

if __name__=="__main__":
    minunits()
    
    

    





         