"""
输入至少有多少个朋友

"""

def minfriends():
    lst=list(map(int,input().split()))
    ele_count=dict()
    for ele in lst:
        if(ele in ele_count):
            ele_count[ele]+=1
        else:
            ele_count[ele]=1
    print(ele_count)
    friends_nums=0
    #社区数*社区的小朋友数
    for key,value in ele_count.items():
        if(value%(key+1)==0):
            friends_nums+=(value//(key+1))*(key+1)
        else:
            friends_nums+=(value//(key+1)+1)*(key+1)
    print(friends_nums)
    return friends_nums
if __name__=="__main__":
    minfriends()
            

            

