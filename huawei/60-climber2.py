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
    #将碰到含有0时重新划为一个新的子列表
    def split_list_by_value(lst,value):
        sublists=[]
        current_sublist=[]
        for item in lst:
            if(item ==value):
                if(len(current_sublist)>1):#如果当前子列表不为空，则添加到结果列表中
                    sublists.append(current_sublist)
                    current_sublist=[]
            else:
                current_sublist.append(item)
        if current_sublist:#添加最后一个子列表
            sublists.append(current_sublist)
        return sublists
    sublists = split_list_by_value(heights,0)
    print(sublists)
    used_power=0
    amount=[]
    mapping=dict()
    mapping["success"]=0
   
   


    for listlist in sublists:
        mapping["left-success"]=0
        mapping["right-success"]=0
        amount=[]
        #第一种情况，左边界处就是山峰
        is_descending = listlist == sorted(listlist, reverse=True)
        if(is_descending):
            if(3*listlist[0]<power):
                mapping["success"]+=1
            continue
        #第二种情况，右边界处就是山峰
        is_ascending = listlist == sorted(listlist)
        if(is_ascending):
            if(3*listlist[-1]<power):
                mapping["success"]+=1
            continue
        print("listlist",listlist)
       #第三种情况，非边界处是山峰
        for i in range(1,len(listlist)-1):
            if(listlist[i]>listlist[i-1] and listlist[i]>listlist[i+1] ):
                amount.append(i)
        #孤峰
        if(len(amount)==1):
            if(3*amount[0]<power):
                mapping["success"]+=1
                print( mapping["success"])
            continue
        #非孤峰，左边起点，左边终点
        original_val=3*listlist[0]
        print(amount,"amount")
        if(len(amount)>1):
            for i in range(1,len(listlist)):
                original_val+=3*abs(listlist[i]-listlist[i-1])
                if(original_val > power and original_val-3*abs(listlist[i]-listlist[i-1])<=power) :
                    for j in range(len(amount)):
                        if( amount[j]<=i-1):
                            mapping["left-success"]+=1
        print(mapping["left-success"],"left-success")
        amount=[]
        #非孤峰，右边起点，右边终点
        listlist.reverse()
        print(listlist,"reverse")
        for i in range(1,len(listlist)-1):
            original_val=3*listlist[0]
            if(listlist[i]>listlist[i-1] and listlist[i]>listlist[i+1] ):
                amount.append(i)
        print(amount,"2")
        if(len(amount)>1):
            for i in range(1,len(listlist)):
                original_val+=3*abs(listlist[i]-listlist[i-1])
                if(original_val > power and original_val-3*abs(listlist[i]-listlist[i-1])<=power) :
                    for j in range(len(amount)): 
                        if( amount[j]<=i-1):
                            mapping["right-success"]+=1
        print(mapping["right-success"],"right-success")
        if(mapping["left-success"]+ mapping["right-success"]>=len(amount)):
            mapping["success"]+=len(amount)
        else:
            mapping["success"]+=mapping["left-success"]
            mapping["success"]+=mapping["right-success"]

        out = mapping["success"]
        print(out)
        return out
  
if __name__=="__main__":
    numclimber()
    

