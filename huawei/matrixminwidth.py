import numpy as np
import itertools

"""

给定一个矩阵，包含N*M个整数，和一个包含K个整数的数组
现在要求在这个矩阵中找一个宽度最小的子矩阵，要求子矩阵包含数组中所有的整数

"""

arr1=input().split()
if len(arr1)== 2:
    N,M=  map(int,arr1)

matrix = np.zeros((N,M),dtype=int)

for i in range(len(matrix)):
    matrix[i]=list(map(int,input().split()))

print(matrix)

K = int(input())
arr2 = list(map(int,input().split()))

element_dict={}

def matrixminwidth():
    count = 0
    element_positions = {}
    min_diff=0
    value_list=[]
    new_all_combinations=[]
    list1=[]
    #最窄子矩阵宽度转化成j的差值的最小值，
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            position = j
            element=matrix[i][j]
            if(element in arr2):
                if element   in element_positions:
                    element_positions[element].append(position)
                else:
                    element_positions[element]=[position]
            
            

    print(element_positions)
    #统计arr2列表中每个元素出现的次数
    count_dict={}
    for item in arr2:
        if item in count_dict:
            count_dict[item]+=1
        else:
            count_dict[item]=1
    print(count_dict)

    
    def combination_list(key):
            return list(itertools.combinations(element_positions[key],count_dict[key]))

        #if(all(value == 1 for value in count_dict.values())==True):
        #values= list(element_positions.values())
        # *操作符在这里用于解包列表。将列表中每个元素作为单独的参数传递给itertools.product
        #当每个组合只取其中一个元素时，有更简便的方法
        #all_combinations = list(itertools.product(*values ))
        #当k个整数中有重复值时，这时的组合元素就不再是l单个元素了，而是tuple元组，需要再次进行转换成list
    for key in set(arr2):
        value_list.append(combination_list(key))
    #print (value_list)
    all_combinations = list(itertools.product(*value_list ))
    print(all_combinations)
    #将所有组合中的每个元素（元组组合）重新合并成一个新的列表list
    for j in range(len(all_combinations)):
        for k in range(len(count_dict)):
            #print(all_combinations[j][k])
            list1 = [item for tup in all_combinations[j] for item in tup]
            new_all_combinations.append(list1)
    print(new_all_combinations)

        #定义一个函数来计算组合中的最大差值
    def max_difference_in_combination(combination):
        return max(abs(a - b) for a,b in itertools.combinations(combination,2))

        #计算所有组合的最大差值，并求出其中的最小值
    max_diffs = [max_difference_in_combination(combination) for combination in new_all_combinations]
    min_diff = min(max_diffs)
        

        
    print(min_diff+1)
    return(min_diff+1)


if __name__ == '__main__':
    matrixminwidth()
                




                


            
            





