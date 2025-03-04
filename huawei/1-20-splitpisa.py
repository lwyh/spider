"""
分批萨的算法原理跟56题的从首位两端取出较大值的原理类型，只不过本题更简单化，因为所有的列表元素不相同


"""
def splitpisa():
    N=int(input())
    splits=[]
    for i in range(N):
        splits.append(int(input()))
    print(splits)
    splits_combines=[]
    splits_combines.append(splits)
    sum_lst=[]
    for j in range(1,len(splits)):
        nestes_lst=splits[j:]+splits[:j]
        splits_combines.append(nestes_lst)
    print("splits_combines",splits_combines)
    for k in range(len(splits_combines)):
        count=0
        jia_lst=[]
        jia_lst.append(splits_combines[k][0])
        splits_combines[k].pop(0)
        print("splits_combines[k]",splits_combines[k])
        while(splits_combines[k] !=[]):      
            if(splits_combines[k][0]>splits_combines[k][-1] ): 
                #注意在此处需要捞取较大值，若在内层中if条件成立时再添加元素由于整个列表因为已经变化，会报错取数异常     
                start = splits_combines[k].pop(0)
                count+=1
                if(count %2==0):
                    jia_lst.append(start)
            if(splits_combines[k][0]<splits_combines[k][-1]  ):  

                end=splits_combines[k].pop()
                count+=1
                if(count%2==0):
                    jia_lst.append(end)
            #因为是奇数块披萨，吃货先选，所以最后一块披萨也是吃货的，题目中的隐含条件需要清楚
            if(len(splits_combines[k])==1):
                jia_lst.append(splits_combines[k][0])
                break
        print("jia_lst",jia_lst)
        sum_lst.append(sum(jia_lst))
    result=max(sum_lst)
    print(result)
    return result
if __name__=="__main__":
    splitpisa()
        
                





