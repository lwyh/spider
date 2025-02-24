"""
 数组最大N数，最小N数，在数组去重后没有重叠，则输出最大N数与最小N数的和
 如有重叠，则输出-1

"""
def Nsum():
    M=int(input())
    lst = list(map(int,input().split()))
    N=int(input())
    lst = list(set(lst))
    lst.sort()
    print("lst",lst)
    if(N<=M//2):
        minN_list=lst[:N]
        maxN_list=lst[-N:][::-1]
        if any(ele in minN_list for ele in maxN_list):
            print("-1")
            return -1
        else:
            out_sum=sum(minN_list)+sum(maxN_list)
            print(out_sum)
            return 0

    else:
        print("-1")
        return -1
if __name__=="__main__":
    Nsum()


