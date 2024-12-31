"""
二叉树计算从父节点到叶节点所有节点之和的最大值






"""
list = []
str =  input()
arr = str.split(' ')
for i in range(len(arr)):
    list.append(int(arr[i]))
depth=1
for j in range(len(list)): 
    if(j==0):
      depth=1  
    while(j !=0):
        j=(j-1)//2
        depth+=1
    if(list[j]!=-1 and depth==1):
        