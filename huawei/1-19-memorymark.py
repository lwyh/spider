"""
内存冷热标记

"""
def memeroymarks():
    N=int(input())
    webs=list(map(int,input().split()))
    threshold=int(input())
    webs_count=dict()
    for ele in webs:
        if(ele in webs_count):
            webs_count[ele]+=1
        else:
            webs_count[ele]=1
    print(webs_count)
    webs_lst=[key for key ,value in webs_count.items() if value >=threshold]
    if(webs_lst==[]):
        result=0
        return -1
    else:
        nums=len(webs_lst)
        print(nums)
        for ele in webs_lst:
            print(ele)
        return 0
if __name__=="__main__":
    memeroymarks()

        
    
    