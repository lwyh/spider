"""
找到list中位置为i的之后i第一个比i身高高的朋友位置j，（j>i）
如果没有，则使用0代替位置，输出新的列表为原列表位置的好朋友的位置列表

"""
def findfriends():
    N=int(input())
    lst=list(map(int,input().split()))
    bigger_dict=dict()
    for i in range(len(lst)):
        bigger_list=[]
        for j in range(i+1,len(lst)):
            if(lst[j]>lst[i]):
                bigger_list.append(j)
        if(bigger_list==[]):
            bigger_dict[i]=0
        if(len(bigger_list)==1):
            bigger_dict[i]=bigger_list[0]
        if(len(bigger_list)>1):
            bigger_dict[i]=min(bigger_list)
    out_list=list(bigger_dict.values())
    print(out_list)
    out = " ".join(map(str,out_list))
    print(out)
    return out_list

if __name__=="__main__":
    findfriends()
            


        
        


