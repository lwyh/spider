"""
两个数组，其中一个数组比另一个数组的相同位置大的个数越多越好，求这样的数组的排序的种数
先输出第一个数组的所有排列组合，然后跟第二个数组比较，找到符合条件的最多数组元素，

"""
import itertools
def bigger():
    array1=list(map(int,input().split()))
    array2=list(map(int,input().split()))
    all_combinations = itertools.permutations(array1)
    print(all_combinations,"all_combinations")
    num_dict=dict()
    #需要处理特殊情况
    if(max(array1)<min(array2)):
        count=0
        for combinlist in all_combinations: 
            if(max(combinlist)<min(array2)):
                count+=1
                continue
        print(count)
    for combinlist in all_combinations:
        count=0 
        for i in range(len(combinlist)):
            if(combinlist[i]-array2[i]>0):
                count+=1
        if combinlist in num_dict:
            num_dict[combinlist].append(count)
        else:
            num_dict[combinlist]=[count]
        key_available=[key for key,value in num_dict.items() if value == max(list(num_dict.values()))]

    #print("num_list",num_list)
    if(max(array1)<min(array2)):
        out = count
    else:
        out = len(key_available)
    print(out)
    return out

if __name__=="__main__":
    bigger()



