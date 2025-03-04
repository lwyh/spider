"""
输入第一行是家庭的总成员数
输入第二行是N个空格分隔的数，表示每个家庭成员的财富
接下来的N行表示两个空格分隔的整数（n1,n2）表示N1是N2的父节点
输出所有小家庭的最大财富，小家庭财富和表示该节点与其直接相连的子节点的财富和

"""
def maxtreasure():
    N=int(input())
    treasures=list(map(int,input().split()))
    nodes=[]
    for i in range(N-1):
        nodes.append(list(map(int,input().split())))
    print(nodes)
    parents=dict()
    for start,end in nodes:
        if(str(start) not in parents):
            parents[str(start)]=[end]
        else:
            parents[str(start)].append(end)
    print(parents)
    treasure_dict=dict()
    #计算小家庭的财富和
    for key,value in parents.items():
        treasure_dict[key]=treasures[int(key)-1]+sum(treasures[k-1] for k in value)
    print(treasure_dict,"treasure_dict")
    #由示例得出当父节点只有一个时的情况
    if(len(treasure_dict)==1):
        result=list(treasure_dict.values())[0]
    else:
        result=max(list(treasure_dict.values()))
    print(result)
    return result

if __name__=="__main__":
    maxtreasure()

        
    