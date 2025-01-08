"""
一组数组，平均分成两组，使得每组的评分和的差最小
"""
list =[]
flag = [1,1,1,1,1,1,1,1,1,1]
input  = input()
sum=0
sum0 = 0
minl = []
arr  = input.split(" ")
for i in range(len(arr)):
    list.append(int(arr[i]))
print(list)
for j in range(len(list)):
    sum0 += list[j]
print(sum0)

for j1 in range(len(list)):
    for j2 in range(j1+1,len(list)):
            for j3 in range(j2+1,len(list)):
                    for j4 in range(j3+1,len(list)):
                            for j5 in range(j4+1,len(list)):
                                    sum +=list[j1]+list[j2]+list[j3]+list[j4]+list[j5]
                                    #print(sum)
                                    sum2 = sum0-sum
                                    delta = abs(sum2-sum)
                                    minl.append(delta)
                                    sum =0
m =minl[0]
for k in range(len(minl)):
      if(minl[k]<m):
            m=minl[k]
print(m)






    