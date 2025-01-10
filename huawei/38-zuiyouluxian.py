"""
投递员最优路线输出，客户与客户之间不保证有最短距离。没有时的路线均为投递站与客户之间的距离的来回
当有路线时，需要比较两个客户与投递站的来回距离相加跟一个来回加客户之间的距离相加的
最短路线的计算是:若客户之间的距离大于起点到两客户之间的距离和，则放弃此条客户之间过度的路线
本题的方法：
1.将小于两边来回的客户之间的路线过滤出来
2.通过距离矩阵将能连通的每一步最短路径输出，当不能连通时直接返回原点再次出发走完剩余没有访问过的节点，直至遍历所有节点再返回起点
"""

import math
def zuiyouluxian1():
    arr1=[]
    arr2=[]
    nodes=[0]
    all_id_dict={}
    min_values=[]
    arr3= list(map(int,input().split()))
    n,m=arr3[0],arr3[1]
    print(n,m)
    for i in range(n):
        arr1= list(map(int,input().split()))
        value1,value2=arr1[0],arr1[1]
        all_id_dict[(0,value1)]=value2
        nodes.append(value1)
    for j in range(m):
        arr2= list(map(int,input().split()))
        ele1,ele2,ele3=arr2[0],arr2[1],arr2[2]
        #将小于两边来回的客户之间的路线过滤出来
        if(all_id_dict[(0,ele1)]+all_id_dict[(0,ele2)]>=ele3):
            all_id_dict[(ele1,ele2)]=ele3
    print(all_id_dict)
    #当客户之间没有捷径可走时，则不存在最短距离，每个客户之间都需要从投递站出发回到投递站再送往下一客户
    if(len(all_id_dict)==n):
        print(-1)
    else:

        #初始化距离矩阵，所有距离设置为无穷大
        distances = [[float('inf')]*len(nodes) for _ in range(len(nodes))]
        print(distances)
        #填充距离矩阵
        for (i,j),dist in all_id_dict.items():
            #将节点编号转换为列表索引
            idx_i = nodes.index(i)
            idx_j = nodes.index(j)
            distances[idx_i][idx_j]=dist
            distances[idx_j][idx_i]=dist  #确保矩阵是对称的
        #将节点自身的距离设置为0 
        for i in range(len(nodes)):
            distances[i][i]=0


        print(distances)
        print(nodes)
        visited_columns = set()
        current_length = 0
        row=0
        while len(visited_columns)<=len(nodes)-1:
            min_values = [(item,idx) for idx, item in  enumerate(distances[row])  if idx not in visited_columns and idx !=0 and item !=float('inf')]
            #print("min_values",min_values)
            if(len(min_values)==0):
                current_length = current_length+distances[row][0]
                print(distances[row][0])
                if(len(visited_columns)==len(nodes)-1):
                    break
                row=0          
            else:
                min_value=min(min_values)
                print(min_value)
                row=min_value[1]
                current_length = current_length+min_value[0]
                visited_columns.add(min_value[1])     
            print(len(visited_columns))
        print(visited_columns)
        print(current_length)

                
                
                




    












    """
    def minDp():
        min_values ={k:min(v)   for k,v in Dp.items()  }
        print("min_values",min_values)
        min_key_value = min(min_values.items(),key = lambda item: item[1])
        print("min_key_value",min_key_value)
        print(min_key_value[0])
    Dp.pop(min_key_value[0])

    """





   
if __name__ =="__main__":
    zuiyouluxian1()

                


        




            




    
    




