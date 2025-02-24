"""
从数组中找出众数，众数组成的新数组找出中位数


"""
def zongshu():
    lst=list(map(int,input().split()))
    ele_count=dict()
    for i in range(len(lst)):
        if(str(lst[i]) in ele_count):
            ele_count[str(lst[i])]+=1
        if(str(lst[i]) not in ele_count):
            ele_count[str(lst[i])]=1
    print(ele_count,"ele_count")
    ele_list=[]
    maxnum=max(list(ele_count.values()))
    ele_list=[key for key,value in ele_count.items() if value==maxnum]
    ele_list.sort()
    mediun_list=[]
    if(len(ele_list)%2==0):
        mediun_list.append(ele_list[len(ele_list)//2-1])
        mediun_list.append(ele_list[len(ele_list)//2])
    if(len(ele_list)%2!=0):
        mediun_list.append(ele_list[(len(ele_list)-1)//2])
    print(mediun_list)
    out = " ".join(map(str,mediun_list))
    print(out)
    return out
if __name__=="__main__":
    zongshu()

        
        


