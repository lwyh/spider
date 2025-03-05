"""
输入数据的每个坐标
输出多线段的起点，转折点以及终点

"""
def multidatazip():
    lst=list(map(int,input().split()))
    sites=[]
    for i in range(len(lst)):
        if(i%2==0):
            sites.append((lst[i],lst[i+1]))
    print(sites)
    zip_lst=[]
    zip_lst.append(sites[0]) #坐标起点
    for i in range(len(sites)-2):
        #由平到斜
        if(sites[i+2][0] != sites[i+1][0] and sites[i+1][0] == sites[i][0]):
            zip_lst.append(sites[i+1])
        #由斜到平
        if(sites[i+2][0] == sites[i+1][0] and sites[i+1][0] != sites[i][0]):
            zip_lst.append(sites[i+1])
        #由斜到斜
        if((sites[i+2][0] != sites[i+1][0]) and sites[i+1][0] != sites[i][0] and (sites[i+2][1]-sites[i+1][1])/(sites[i+2][0]-sites[i+1][0])!=
        (sites[i+1][1]-sites[i][1])/(sites[i+1][0]-sites[i][0])):
            zip_lst.append(sites[i+1])
    zip_lst.append(sites[-1]) #坐标终点
    print(zip_lst)
    zip_lst=[ele for sub in zip_lst for ele in sub] 
    print(zip_lst)
    result=" ".join(map(str,zip_lst ))
    print(result)
    return result
if __name__=="__main__":
    multidatazip()
    






