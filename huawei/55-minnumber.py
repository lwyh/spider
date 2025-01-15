"""
输入一个十进制数m,转化为二进制数，，输出一个数比m大的最小n,满足m和n转化为二进制数中的1的个数相同

"""
from   collections   import deque
import itertools
def minNumber():
    inner  = int(input())
    quoe=inner//2
    reminder = inner%2
    queque = deque()
    queque.append(reminder)
    while quoe!=0:
        reminder = quoe %2
        quoe = quoe//2 
        queque.append(reminder)
    print(queque)
    #分3种情况来分析二进制中含有1的个数
    avialble_m=[]
    avialble_m_list=[]
    avialble_m_perm=[]
    if(queque.count(1)==1):
        queque.appendleft(0)
        print("queque",queque)
        m=2**(len(queque)-1)
        print(m)
        return m
    if(all (x==1 for x in queque)):
        print("1111")
        for j in range(1,len(queque)+1):
            queque_list= list(queque)
            print(queque_list,"queque_list")
            new_list = queque_list[:j]+[0]+queque_list[j:]
            avialble_m.append(new_list) 
        print("avialble_m",avialble_m)
        for k in range(len(avialble_m)):
            avialble_m_decent=0
            avialble_m[k].reverse()
            print(avialble_m[k])
            for l in range(len(avialble_m[k])):   
                avialble_m_decent+=avialble_m[k][l]*(2**l)
            avialble_m_list.append(avialble_m_decent)
            m=min(ele for ele in avialble_m_list if ele>inner)
            print(m)
            return m
    if(0 in queque and queque.count(1)>1):
        permutations= itertools.permutations(queque)
        for perm in permutations: 
            perm_list= list(perm)
            perm_list.reverse()
            print(perm_list,"perm_list")
            print(perm_list[0])
            if(perm_list[0]!=0):
                print(perm_list,"perm_list111111111")
                avialble_m_ele=0
                perm_list.reverse()
                #在进行相加前，需要将倒反放在循环外面
                for m in range(len(perm_list)):
                    avialble_m_ele += perm_list[m]*(2**m)
                    print(avialble_m_ele)
            perm_list=[]
            avialble_m_perm.append(avialble_m_ele)
        print(avialble_m_perm)
        m=min(ele for ele in avialble_m_perm if ele>inner)
        print(m)
        return m
    

    
    


if __name__=="__main__":
    minNumber()


        
