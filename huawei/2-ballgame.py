"""
篮球游戏，入队列时，只能从队列的右边入队，出队时，可以同时从队列右边或左边出队
当队列中只剩最后一个元素时，只能从队列的左边出队
本题的分类讨论情况比较复杂
1.需要先将放入球的情况列表出来
2.然后再从去处球的顺序得出取出球的方向
"""
from collections import deque
def ballgame():
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
      
    def split_combination(split_list,lst1,lst2,i):
        print("lst1",lst1)
        print("ii",i)
        while(lst1!=[]):            
            if(lst2[i] in lst1):
                if(lst1.index(lst2[i])==len(lst1)-1):
                    split_list.append(lst1)
                    break
                else:
                    split_list.append(lst1[:lst1.index(lst2[i])+1])
                    print("split_list1111111111111",split_list)
   
                if(i==len(lst2)-1):
                    break
            else:
                split_list=[]
                break
            for k in range(len(lst1[:lst1.index(lst2[i])+1])): 
                print("11111111",lst2[i+k])  #1         
                if(lst2[i+k] in lst1[:lst1.index(lst2[i])+1] and i+k+1<len(lst2)
                and lst2[i+k+1] not in lst1[:lst1.index(lst2[i])+1] ):
                    lst1 = lst1[lst1.index(lst2[i])+1:]
                    print("333333333333",lst1)
                    i+=k+1
                    #print(lst1,"end","i123456",i,"kkkk",k,"lst1[:lst1.index(lst2[i])+1]",lst1[:lst1.index(lst2[i])+1])
                    break       
        return split_list

    direction_list=[]
    queue=deque()
    
    

    
    split_list=split_combination([],lst1,lst2,0)
    print(split_list,"split_list")
    if(split_list==[]): 
        print("NO")
        return -1
    else:

        k=0
        for j in range(len(split_list)):
            print("queueqqqqqqqqqqqqqq",queue)
            for ele  in split_list[j]:
                queue.append(ele)
                print("queue",queue)
            while(k<len(lst2)):
                #print("queue.pop()",queue.pop())
                if(len(queue)==1 and  k==len(lst2)-1):
                    direction_list.append("L")
                    break
                print("queue111111111111111",queue)
                
                print("lst2[k]",lst2[k])
                print("k",k,"queue.pop()",queue )#0,[1,2,3,4,5]
                if(len(queue)==1  and k!=len(lst2)-1):
                    item = queue.pop()
                    if(lst2[k]==item):
                        direction_list.append("L")
                        print("0--=============",direction_list)
                        k+=1
                        break
                    else:
                        queue.append(item)
                        break          
                if(len(queue)>1 and lst2[k] in queue):
                    itemleft=queue.popleft() 
                    itemright=queue.pop()    
                    if(lst2[k]!=itemleft and lst2[k]!=itemright):
                        direction_list=[]
                        break
                    else:
                        if(itemright==lst2[k] ):
                            direction_list.append("R")
                            print("direction_list",direction_list)
                            queue.appendleft(itemleft)
                        if(itemleft==lst2[k] ):
                            direction_list.append("L")
                            print("direction_list",direction_list)
                            queue.append(itemright)
                        k+=1
                if(len(queue)>1 and lst2[k] not in queue):
                    break

                print("kkkk",k,"queue.pop()",queue )
                #time.sleep(100)

    print(direction_list,"direction_list")
    if(direction_list==[]):
        print("NO")
        return -1
    else:
        out = "".join(direction_list)
        print("out",out)
        return out


 

if __name__=="__main__":
    ballgame()