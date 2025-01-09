"""
所有会议占用同一个会议室,求会议室的占用时间段
"""
import sys
def intervalstatis():
    inner = input()
    sublist= inner.strip("[]").split('],')
    #sublist2=list(map(int,item.strip("[]").split(',') ) for item in inner.strip("[]").split('],'))
    #print(sublist2)
    nest_list=[]
    for substr in sublist:
        nest_list.append(list(map(int,substr.strip("[]").split(','))))
    
    

    nest_list=sorted(nest_list,key=lambda x :(x[0] ,-(x[1]-x[0])))
    print(nest_list)
    current_start=nest_list[0][0]
    current_end=nest_list[0][1]
    nest_list2=[]
    nest_list2.append([current_start,current_end])
    count=0
    print(len(nest_list))
    for start,end in nest_list[1:]:
        #合并1
        if(start ==current_end):
            nest_list2.pop()
            nest_list2.append([current_start,end])
            current_end=end
            count+=1
            continue
        #追加
        if(start >current_end):
            nest_list2.append([start,end])
            current_end=end
            current_start=start
            count+=1
            continue
        #合并2
        if(start <current_end and end >current_end):
            nest_list2.pop()
            nest_list2.append([current_start,end])
            current_end=end
            count+=1
            continue
            
        if(start < current_end and end <=current_end):
            count+=1
        """
        if(count==(len(nest_list)-1)):
            print(count)
            print(len(nest_list)-1)
            break
        """
 
    print(nest_list2,count)
    return nest_list2   

if __name__=="__main__":
    intervalstatis()