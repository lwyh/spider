"""
输入小于节点数减去500，插入节点的左子树
输入大于节点数加500，插入节点的右子树
否则，插入节点的中子树
输出树的高度

"""
def threenodesheight():
    N=int(input())
    lst=list(map(int,input().split()))
    height=0
    if(len(lst)==1):
        height=1
    if(len(lst)>1):
        left_node=[]
        medium_node=[]
        right_node=[]
        #注意parent节点在任何的搜索中位置是不变的
        for i in range(1,len(lst)):
            parent=lst[0]
            if(lst[i]<parent and abs(lst[i]-parent)>500):
                left_node.append(lst[i])
            if(abs(lst[i]-parent)<=500):
                medium_node.append(lst[i])
            if(lst[i]>parent and abs(lst[i]-parent)>500):
                right_node.append(lst[i])
            parent=lst[i]
        print(left_node)
        print(medium_node)
        print(right_node)
        height=1+max(len(left_node),len(medium_node),len(right_node))
    print(height)
    return height
if __name__=="__main__":
    threenodesheight()

