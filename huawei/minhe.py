"""
座位间隔一人落座，有人坐的标记为1，无人做的标价为0
在不移动人的情况下，最多还可以坐多少人
分3种情况，并且互相排斥，1：前两个字符都是0，可加1
2.从非零位开始到非末尾结束，连续3位都是0 ，可加1
3.末尾两位字符都是0，可加1

"""

str = input()
list = []
count=0

for digit in str:
    print(digit)
    list.append(int(digit))
for i in range(len(list)):
    if(i==0 and  list[i]==0 and list[i+1]==0 ):
        count+= 1
    if(i>=1 and i<=len(list)-4 and list[i]==0 and list[i+1]==0 and list[i+2]==0):
        count+= 1
    if(i==len(list)-2 and list[len(list)-2]==0 and list[len(list)-1]==0):
        count+= 1
print(count)
    



