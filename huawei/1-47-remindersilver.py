"""
x==y==z 3块银饰都会被融掉
x==y 且 y!=z 则剩下z-y的银块无法融掉
x!=y 且 y==z 则剩下y-x的银块无法融掉
x!=y 且 y!=z 则剩下y-x 与z-y的差值的银块无法融掉
如果最后只剩下两块，则返回较大质量的银块（如果两块质量相同，则返回任意一块），
如果只剩下最后一块，则返回该块质量，
如果没有剩下，则返回0


"""
def remindersilver():
    N=int(input())
    lst= list(map(int,input().split()))
    sorted_list = sorted(lst,reverse=True)
    while(len(sorted_list)>=3):
        z,y,x=sorted_list[0],sorted_list[1],sorted_list[2]
        print("sorted_list",sorted_list)
        if(x==y and y==z):
            sorted_list.pop(0)
            sorted_list.pop(0)
            sorted_list.pop(0)
        print(sorted_list)
        if(x==y and y!=z):
            sorted_list.pop(0)
            sorted_list.pop(0)
            sorted_list.pop(0)
            sorted_list.append(z-y)
        print(sorted_list)
        if(x!=y and y==z):
            sorted_list.pop(0)
            sorted_list.pop(0)
            sorted_list.pop(0)
            sorted_list.append(y-x)
        print(sorted_list)
        if(x!=y and y!=z):
            sorted_list.pop(0)
            sorted_list.pop(0)
            sorted_list.pop(0)
            sorted_list.append(abs((y-x)-(z-y)))
        print(sorted_list)
    if(len(sorted_list)==0):
        print(0)
    if(len(sorted_list)==1):
        print(sorted_list[0])
    if(len(sorted_list)==2):
        print(max(sorted_list))
    return 0
    

if __name__=="__main__":
    remindersilver()