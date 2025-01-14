"""
每组的结对中员工的职级是不同的，并且是升序或者降序排列，不能是乱序，输出所有的小组组合可能

"""
def jieduicoding():
    N=int(input())
    array=list(map(int,input().split()))
    count=0
    combine_list=[]
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            for k in range(j+1,len(array)):
                if((array[i]<array[j] and array[j]<array[k]) or (array[i]>array[j] and array[j]>array[k])):
                    count+=1
                    combine_list.append([array[i],array[j],array[k]])
    print(count,combine_list)
    




if __name__=="__main__":
    jieduicoding()