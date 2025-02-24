"""
机器图形面积，


"""
def mainji():
    lst1=list(map(int,input().split()))
    N,E=lst1[0],lst1[1]
    lst2=[]
    for i in range(N):
        lst2.append(list(map(int,input().split())))
    mianji=0
    height=0
  #前面n-1个offet的面积
    for j in range(len(lst2)-1):
        height+=lst2[j][1]
        mianji+=(lst2[j+1][0]-lst2[j][0])*(abs(height))
  #最后一个offset的面积
    mianji+=(E-lst2[-1][0])*abs(height+lst2[-1][1])
    print(mianji)
    return mianji
if __name__=="__main__":
    mainji()
    
