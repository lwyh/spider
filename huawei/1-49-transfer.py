"""
第一个数字是十进制数，第二个数是幸运数字，第三个数字是改异国转换数字


"""
import math

input = input()
arr =input.split(" ")

k = int(arr[0])
n =int(arr[1])
m =int(arr[2])
out = 0
while(k / m != 0):
    if(k % m == n):
        out+=1
    k =k / m
if(k==n):
    out+=1
print(out) 
