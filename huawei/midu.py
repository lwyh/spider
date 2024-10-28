


list1 = input()
array1=list1.split()
array2=[]
list2=[]
for i in range(len(array1)):
    array2.append(int(array1[i]))
    array2.sort(reverse=True)
    print(array2.index(array2[0]))


    
#for i in range(list.count()):
    

