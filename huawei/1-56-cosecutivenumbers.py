"""
一个整数由连续自然数 相加得知


"""
def consecutivecombines():
    T=int(input())
    avialble_list=[]
    #或者avialble_list=[[T]]
    #for i in range(1,T):
    for i in range(1,T+1):
        for k in range(T):
            if((i+i+k)*(k+1)/2==T):
                avialble_list.append([ele for ele in range(i,i+k+1)])
    print("avialble_list",avialble_list)
    sorted_list = sorted(avialble_list,key=lambda x:len(x))
    print("sorted_list",sorted_list)
    #中间有空格
    for i in range(len(sorted_list)):
        print(T,"=","+".join(map(str,sorted_list[i])))
    print("Result",len(sorted_list))
    #中间没有空格
    for i in range(len(sorted_list)):
        print(str(T)+"="+"+".join(map(str,sorted_list[i])))
    print("Result"+str(len(sorted_list)))


    return avialble_list

if __name__=="__main__":
    consecutivecombines()



