"""
由3的倍数组成的数组，每3个按照顺序将每组中的最大值和最小值，剩下的数再重新组合成新的列表，列表元素和为S，可以通过
调整数组中元素位置改变结果，每移动一个元素计为移动一次，请计算最少移动次数使得S值最大



"""

arr1= list(map(int,input().split()))
#通过建立一个函数使得每次取出的是剩余元素的最大值，次最大值以及最小值，这样可以使得最终的S最大
"""
def max_item(arr):
    select_arr=[]
    n=len(arr)//3
    while n>0:
        arr.sort(reverse=True)
        select_arr.append(arr[1])
        arr.pop(0)
        arr.pop(1)
        arr.pop()
        n -=1
    print(select_arr)
    return select_arr
"""
        


 
"""
def backtrack(arr): 
    n=len(arr)//3
    slist=[]
    xlist=[]
    per_list=[]
    new_arr=[]
    min=0
    count=0
    for i in range(len(arr)//3):
        for j in range(3*i,3*i+3):
            slist.append(arr[j])
            if(len(slist)==3):
                xlist.append(slist[:])
                slist=[]
    print(xlist)
    for k in range(len(xlist)):
        xlist[k].sort()
        per_list.append((xlist[k])[1])  
    print("per_list",per_list)
    return per_list
"""

def backtrack(arr): 
    count=0
    #使得移动后的S值最大确保每组的最大值和次最大值必须是连续的，剩下的最小的len(arr1)//3的数可以随意落在每组，对最小的数没有限制
    new_arr = sorted(arr,reverse=True)
    #接下来的排序是arr[0]+1,arr[0]+2为随意分派在每组，arr[0]+len(arr)//3，arr[0]+len(arr)//3+1，arr[0]+len(arr)//3+2
    #在一组，arr[0]+2*len(arr)//3，arr[0]+2*len(arr)//3+1，arr[0]+2*len(arr)//3+2在一组，最大的数是
    #最后一种方案思路最清晰，相邻的连续的最大数和次最大数在列表中的位置大于或等于3时，则至少需要移动一次
    for i in range(1,2*len(arr)//3):

        if(abs(arr.index(new_arr[0]-i+1)-arr.index(new_arr[0]-i))>=3):
            count+=1
        i+=2
    print(count)
    return count



    
   
  




    



    
    

if __name__=='__main__':
    backtrack(arr1)
   





