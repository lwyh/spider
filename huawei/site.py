"""
输入是[93,95,97,100,103,123,135]
110
输出是:6

list的输入格式是str
循环的正确使用

"""
list = []
input1 = input()
input2 = input()
arr = input1.split(" ")
for i in range(len(arr)):
        list.append(int(arr[i]))
print(len(list))
for k in range(len(list)):
        if(list[k]<int(input2) and int(input2) <list[k+1]):
                print(k+2)





