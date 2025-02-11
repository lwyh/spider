"""
n颗树，第一行输入为每棵树上蟠桃数量
第二行是守卫员离开蟠桃园的时间H
输出猴子吃蟠桃的速度k
猴子需要在离开的H小时内以最小的速度K吃完所有的蟠桃
"""
def evendistrbutions():
    lst = list(map(int,input().split()))
    H=int(input())
    

    if(H<len(lst)):
        print("0")
        return -1
    if(H==len(lst)):
        k=max(lst)
        print(k)
        return -1
    if(H>len(lst)):
        k_time=dict()
        for k in range(1,max(lst)):
            spent_time=[]
            for i in range(len(lst)):
                if(lst[i]%k==0):
                    spent_time.append(lst[i]//k)
                else:
                    spent_time.append(lst[i]//k+1)
            k_time[k]=sum(spent_time)
        print("k_time",k_time)
        for k in range(1,max(lst)):
            if(k_time[k]>H and k_time[k+1]<=H):
                print("k+1",k+1)
                return 0

if __name__=="__main__":
    evendistrbutions()



