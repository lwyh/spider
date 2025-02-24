"""
输入第一行是AB两组的CPU数量
输入第二行是A组的CPU算力
输入第三行是B组的CPU算力
输出是交换A,B两组的算力，使得交换后两组的算力和相等


"""
def exchangesever():
    lst=list(map(int,input().split()))
    lstA=list(map(int,input().split()))
    lstB=list(map(int,input().split()))
    exchanged=[]
    for i in range(len(lstA)):
        for j in range(len(lstB)):
            if(sum(lstA)-lstA[i]+lstB[j]==sum(lstB)-lstB[j]+lstA[i]):
                exchanged.append([lstA[i],lstB[j]])
    print(exchanged)
    #需要输出最小的交换算力A
    sorted_list=sorted(exchanged,key=lambda item:(item[0]))
    out_list = sorted_list[0]
    result=" ".join(map(str,out_list))
    print(result)
    return result
if __name__=="__main__":
    exchangesever()

