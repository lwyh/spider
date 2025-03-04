"""
整数的分解

"""


def numssplit():
    N=int(input())
    avialble_lst=[]
    for i  in range(1,N//2+1):
        for j in range(1,N):
            if((i+i+j)*(j+1)/2<N and (i+i+j+1)*(j+2)/2==N):
                avialble_lst.append([ele for ele in range(i,i+j+2)])
                break
            #注意当分解只有两个连续的整数之和时，需要另作讨论
            if((i+i+j)*(j+1)/2==N):
                avialble_lst.append([ele for ele in range(i,i+j+1)])
                break
    print(avialble_lst)
    if(avialble_lst==[]):
        result="N"
        print(result)
    else:
        length = min(len(ele) for ele in avialble_lst)
        for ele in avialble_lst:
            if(len(ele)==length):
                right="+".join(map(str,ele))
                print(str(N)+"="+right)
    return 0
if __name__=="__main__":
    numssplit()
    



