"""
地图的N个城市，两两之间只有一条道路，切断某个城市后，剩余的城市联通的会形成城市群，城市群中城市的个数的最大值称为该城市的聚集度
找出这个地图上所有城市聚集度的最小值

如果有多个城市满足条件，都要找出来
编号按照升序输出

"""
from tqdm import tqdm

def mindp():
    num = int(input())
    join_list=[]
    for i in range(num-1):
        join_list.append(list(map(int,input().split())))

    print(join_list)
    DP=dict()

    
    
    minValue=0
    mindp=0
    count=0

    start_set=set()
    end_set=set()
    leaf_list=[]
    combine_list=[]
    path=list()
    current_end=0
    stage_list=[]
    for start ,end in join_list:
        start_set.add(start)
        end_set.add(end)
    leaf_list=list(set(end_set)-set(start_set))
        #print(leaf_list)
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

    
        
    current_list=[]
    for j in range(num):
        current=j+1
        for l in range(len(combine_list)):
            for m in range(len(combine_list[l])):
                for n in range(len(leaf_list)):
                    if(current==leaf_list[n] or current==1):
                        DP[current]=num-1
                print(combine_list[l].split(current))


            
               
                
               
        #DP[current]=max(stage_list)
        #print(DP)
    #mindp=min(DP,key=lambda k: DP[k])







        

            
            
        
       
    #min_value = min(DP.values())
    #keys_with_min_value = [k for k,v in DP.items() if v==min_value]

    #print(keys_with_min_value)
    print(mindp)
    return mindp


    
if __name__=='__main__':
    mindp()
