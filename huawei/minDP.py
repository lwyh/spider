"""
地图的N个城市，两两之间只有一条道路，切断某个城市后，剩余的城市联通的会形成城市群，城市群中城市的个数的最大值称为该城市的聚集度
找出这个地图上所有城市聚集度的最小值

如果有多个城市满足条件，都要找出来
编号按照升序输出

"""
from tqdm import tqdm
from collections import defaultdict

def mindp():
    num = int(input())
    join_list=[]
    #将城市之间两两相连的节点用list装下
    for i in range(num-1):
        join_list.append(list(map(int,input().split())))

    print(join_list)
    DP=dict()
    start_set=set()
    end_set=set()
    leaf_list=[]
    combine_list=[]
    path=list()
    current_end=0
    #实现将叶子节点即没有子节点的节点输出
    for start ,end in join_list:
        start_set.add(start)
        end_set.add(end)
    leaf_list=list(set(end_set)-set(start_set))
        #print(leaf_list)
    #此处将join_list反向排序是为了下一步将所有的完整路径找出来
    join_list.sort(reverse=True)
        #print(join_list)
    for i in range(len(leaf_list)):
        for start ,end in join_list:
            if(end==leaf_list[i]):
                path.append(end)
                path.append(start)
                current_end=start
            if(end==current_end):
                path.append(start)
                current_end=start
            #print("path",path)
        combine_list.append(path)
        path=[]

    print(combine_list)

    
        
    over_list=[]
    less_list=[]
    over_set=[]
    less_set=[]
    rank_list_over=[]
    rank_list_less=[]
    over_list_sub=[]
    less_list_sub=[]
    combine_set_less=set()
    combine_set_over=set()
    none_current_set=set()
    none_current_count=0
    keys_with_min_value=0
    min_value=0
    less=0
    over=0



    #实现切断某个节点后剩余部分连通节点数的最大值，此处分为几种情况讨论，
    # 第一种情况是节点1和叶子节点
    # 第二种情况是切断的节点不在某条完整的路径中，需要将不在路径中的列表合并
    # 第三种情况是切断的节点在某条完整的路径中，此时需要知道该条路径大于切断节点的的节点列表以及小于切断节点的的节点列表分别输出，
    # 并将列表中含有其他相同元素的列表合并从而得出含有切断节点的路径的剩余相通节点的数的最大值
    #将以上3种情况的最大值按照列表输出，同时再输出字典中最大值中的最小值
    for j in range(num):
        current=j+1
        if(current in leaf_list or current==1):
            DP[current]=num-1
            print("DP",DP)
        else:
            for l in range(len(combine_list)):
                if(current not in leaf_list and current!=1 and    current not in  combine_list[l]):
                    none_current_set.update(combine_list[l])
                print(current,none_current_set)
                none_current_count=len(none_current_set)
                for m in range(len(combine_list[l])):
                    if(current not in leaf_list and current!=1 and    current in  combine_list[l]  ):
                        if(combine_list[l][m]>current):
                            over_list_sub.append(combine_list[l][m])
                        if(combine_list[l][m]<current):
                            less_list_sub.append(combine_list[l][m])
                    if(m==len(combine_list[l])-1):
                        l+=1
                        over_list.append(over_list_sub)
                        less_list.append(less_list_sub)
                        over_list_sub=[]
                        less_list_sub=[]

      
            #输出大于current的值的列表集合          
            print("over_list",over_list)
            element_to_over_list = defaultdict(list)
            for sublist_index,sublist in enumerate(over_list):
                for element in sublist:
                    element_to_over_list[element].append(sublist_index)
            print(element_to_over_list)
            for element,indices in element_to_over_list.items():
                if(len(indices)>1):
                    #over_set.append([sorted(over_list[i]) for i in indices])
                    for i in indices:
                        over_set.append(over_list[i])
                    print("over_set",over_set)
                    for sublist in over_set:
                        combine_set_over.update(sublist)
                    print("combine_set_over",combine_set_over)
                    rank_list_over.append(len(combine_set_over))
                    over_set=[]
                    combine_set_over=set()
            print(rank_list_over)

            #输出小于current的值的列表集合          
            print("less_list",less_list)
            element_to_less_list = defaultdict(list)
            for sublist_index,sublist in enumerate(less_list):
                for element in sublist:
                    element_to_less_list[element].append(sublist_index)
            print(element_to_less_list)
            for element,indices in element_to_less_list.items():
                if(len(indices)>1):
                    #over_set.append([sorted(over_list[i]) for i in indices])
                    for i in indices:
                        less_set.append(less_list[i])
                    print("less_set",less_set)
                    for sublist in less_set:
                        combine_set_less.update(sublist)
                    print("combine_set_less",combine_set_less)
                    rank_list_less.append(len(combine_set_less))
                    less_set=[]
                    combine_set_less=set()
            print(rank_list_less)
            
            less=len(rank_list_less)
            over=len(rank_list_over)
            DP[current]=max(none_current_count,over,less,max(len(sublist) for index,sublist in enumerate(over_list)))
            over_list=[]
            less_list=[]
            rank_list_less=[]
            rank_list_over=[]
            none_current_set=set()
        print(DP)
        
        min_value = min(DP.values())
        keys_with_min_value = [k for k,v in DP.items() if v==min_value]

    print(keys_with_min_value)
    
    return keys_with_min_value


    
if __name__=='__main__':
    mindp()











                        



                    



                


            
               
                
               
       







        

            
            
        
       
   