"""

题目描述：

算法工程师小明面对着这样一个问题，需要将通信用的信道分配给尽量多的用户，

信道的条件及分配规则如下：
1) 所有信道都有属性：”阶”。阶为 r 的信道容量为 2^r 比特；
2) 所有用户需要传输的数据量都一样：D 比特；
3) 一个用户可以分配多个信道，但每个信道只能分配给一个用户；
4) 只有当分配给一个用户的所有信道的容量和大于等于D时，用户才能传输数据；
给出一组信道资源，最多可以为多少用户传输数据？


"""

def get_max(list1,need1):
    m = len(list1)-1
    count =0
    for i in range(m+1):
        sum=0
        sum = list1[i]
        while m>=0:
            j=m
            if sum>=need1:
                print(1,sum) 
                count+=1
                break
            else:
                sum+=list1[m]
                if sum>=need1:
                    print(2,sum,m,i)
                    count+=1
                    m-=1
                    break
                else:
                    m-=1
        if m-i<=1:
            break
    print(count)
        

r= int(input()) #信道最大阶数
str1 = input()
num1 = str1.split(" ") #信道数量
for i in range(len(num1)):
    num1[i] = int(num1[i])
num1.reverse()
print(num1)
need = int(input())#需要bite
num2=[]
for i in range(int(r)+1):
    num2.append(pow(2,i))
num2.reverse()
print(num2)
num3=[]
for i in range(len(num2)):
    for j in range(num1[i]):
        num3.append(num2[i])
print(num3)
get_max(num3,30)