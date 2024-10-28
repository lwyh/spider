"""

一组数组，连续多个数组中值相加和为最后一个数，求数的最大个数

"""
list =[]
n= int(input())
sum=0
for i in range(n):
    list.append(int(input()))
print(list)
value =int(input())
m=0
arr= []
for j in range(n):
    sum +=list[j]
    m+=1
    if((sum<=value and   j+1<n and (sum+list[j+1])>value ) or j+1==n):
        print(m)
        arr.append(m)
        m=0
        sum=0
max = arr[0]
for k in range(len(arr)):
    if(arr[k]>max):
        max=arr[k]
print(max)


