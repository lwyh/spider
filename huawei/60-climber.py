"""
相邻索引位置的高度差，上坡时消耗体力是高度差的2倍，下坡时消耗体力是高度差的1倍，平地不消耗体力
在高度为0 的两个索引之间有多座山峰，攀登者的体力是固定的，问在体力不透支的情况下可以攀登多少座高峰
高峰定义是高度大于左右两边高度，或者是在边界处


"""

def numclimber():
    string = input()
    array = string.split("],")
    power = int(array[1])
    heights=list(map(int,array[0].strip("[]").split(",")))
    print(heights,power)
    mounts=0#统计山峰的个数
    amount_dict=dict()
    for i in range(1,len(heights)-1):
        if((heights[i]-heights[i-1]>0 and heights[i]-heights[i+1]>0 )):
            amount_dict[i]=heights[i]
            mounts +=1
        if(heights[0]>0 and heights[1]>heights[1]):
            amount_dict[0]=heights[0]
            mounts +=1
        if(heights[-1]>0 and heights[-1]>heights[-2]):
            amount_dict[len(heights)-1]=heights[-1]
            mounts +=1
    print(mounts)
    print(amount_dict)
    #孤峰，即每座山脉只有一座山峰
    plain=[idx for idx,value in enumerate(heights) if value==0]
    print(plain)
    mount_info=dict()
    for i in range(len(plain)-1):
        for key,value in amount_dict.items():
            if(key>plain[i] and key<plain[i+1]):
                if(plain[i],plain[i+1]) not in mount_info:
                    mount_info[(plain[i],plain[i+1])]={}  
                mount_info[(plain[i],plain[i+1])][key]=value
                
    print(mount_info)
    mapping=dict()
    mapping["success"]=0
    def avialble_path(lst):
        def dfs(start,end ,current,path,paths):
            if current ==end:
                if(len(path)>1):
                    paths.append(path[:])
                    return
            if current <end:
                next_node = current+1
                if(next_node!=len(lst)-1):
                    path.append(lst[next_node])
                    dfs(start,end,next_node,path,paths)
                    path.pop()
            if(current> start):
                next_node=current-1
                if(next_node !=0):
                    path.append(lst[next_node])
                    dfs(start,end,next_node,path,paths)
                    path.pop()
        #从第一个元素出发，最终回到第一个元素
        start_paths = []
        dfs(0,0,0,[lst[0]],start_paths)

        #从最后一个元素出发回到最后一个元素
        end_paths=[]
        dfs(len(lst)-1,len(lst)-1,len(lst)-1,[lst[-1]],end_paths)


        return start_paths,end_paths


            



    
    for key,value in mount_info.items():
        #孤峰
        if(len(value)==1):
            if((list(value.values())[0])*3<power): mapping["success"]+=1
        #非孤峰
        if(len(value)>1):
            avialble_node=[]
            avialble_node.append(key[0])
            for item in list(value.keys()):
                avialble_node.append(item)
            avialble_node.append(key[1])
            print(avialble_node)
            #经历所有点的路径消耗的体力
            used_power=0
            for l in range(avialble_node[0]+1,avialble_node[-1]):
                if(heights[l]>=heights[l-1]):
                    used_power+=2*(heights[l]-heights[l-1])
                if(heights[l]<heights[l-1]):
                    used_power+=heights[l-1]-heights[l]
            if(used_power<power):
                mapping["success"]+=len(avialble_node)-2
            else:
                start_paths,end_paths=avialble_path(avialble_node)
                for path in start_paths:
                    if(len(path)==3):
                        if(2*heights[path[1]]<power):
                            mapping["success"]+=1
                    if(len(path)>3):
                        


                        





            



           





    
        

    










if __name__=="__main__":
    numclimber()



