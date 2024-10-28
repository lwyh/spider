"""
描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序

数据范围： 1≤n≤1000 1≤n≤1000  ，元素大小满足 0≤val≤100000 0≤val≤100000 
输入描述：

第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序
输出描述：

输出排好序的数字



"""

import sys

a = input()
arr = input("")    #输入一个一维数组，每个数之间使空格隔开
num = [int(n) for n in arr.split(' ')]    #将输入每个数以空格键隔开做成数组
flag = input()
def rangking():
    if(int(flag)==0):
        num.sort()
        #join后面需要元素类型是str
        out = " ".join(str(i) for i in num)
        return out
    if(int(flag)==1):
        num.sort(reverse=True)
        out = " ".join(str(i) for i in num)
        return out
print(rangking())
 
