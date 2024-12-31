"""
有向图，可能包含环，图使用二维矩阵表示，每一行的第一列是起始节点，第二列表示终止节点。

"""
def orientedcircle():

    node=int(input())
    arr=list(map(int,input().split()))
    start_node=[]
    end_node=[]
    end=set()
    start=set()
    out_list=[]
    out=0
    for i in range(len(arr)):
        if(i %2==0):
            start_node.append(arr[i])
        else:
            end_node.append(arr[i])
    end=set(end_node)-set(start_node)
    start=set(start_node)-set(end_node)
    if(len(end)==0):
        print(-1)
        return -1
    else:
        list(start|end).sort()
        out_list=list(start|end)
    
    print(*out_list)
    print(" ".join(map(str,out_list)))
    return out_list




if __name__=="__main__":
    orientedcircle()
