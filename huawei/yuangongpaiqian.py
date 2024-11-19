"""
员工派遣规则：代号x的倍数不能去x国家，找到最小的k满足的连续的员工号满足所有国家派遣的规则
"""



def fenpai():
    arr=list(map(int,input().split()))
    x,y,cntx,cnty=arr[0],arr[1],arr[2],arr[3]

    
    listx=[]
    listy=[]
    l=cntx+cnty
    for i in range(l):
        if((i+1) % x!=0):
            listx.append((i+1))
        else:
            if((i+1) % y!=0):
                listy.append((i+1))
    while l>=cntx+cnty:
        if(len(listx)>=cntx and len(listy)>=cnty):
            print(l)
            break
        else:
            l+=1
            if(l%x!=0):
                listx.append(l)
            if(l%y !=0):
                listy.append(l)
    return l

if __name__=="__main__":
    fenpai()
        
    