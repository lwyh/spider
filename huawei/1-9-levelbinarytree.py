"""
输入的是二叉树的层次遍历，求每层次的最大值
输出将二叉树每层的节点单独存储，然后输出每层最大值的和
解题思路是先通过层次遍历构建二叉树root
再将二叉树中的每层节点单独存储
"""
class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
#构建二叉树
def build_tree_from_level_order(level_order):
    if not level_order:
        return None
    #根节点
    root = TreeNode(level_order[0])
    queue=[root]
    i=1
    while i<len(level_order):
        #从左至右逐一分解其父节点
        current=queue.pop(0)
        #该current父节点的左子节点
        if(level_order[i] is not None):
            current.left = TreeNode(level_order[i])
            queue.append(current.left)
        i+=1
        #该current每个父节点的右子节点
        if(i<len(level_order) and level_order[i] is not None):
            current.right=TreeNode(level_order[i])
            queue.append(current.right)
        i+=1
    return root
#二叉树的每层节点单独存储
def level_order_traversal_by_level(root):
    if(not root):
        return []
    result=[]
    queue=[root]
    while queue:
        level_values=[]
        level_size=len(queue)

        for _ in range(level_size):
            current=queue.pop(0)
            level_values.append(current.value)

            if(current.left):
                queue.append(current.left)
            if(current.right):
                queue.append(current.right)
        result.append(level_values)
    return result
level_order=list(map(int,input().split()))
#注意此中的-1不能去掉，否则会影响二叉树的结构
#level_order=[ele for ele in level_order if ele !=-1]
root = build_tree_from_level_order(level_order)
result = level_order_traversal_by_level(root)
print("result",result)
time=0
for sublist in result:
    time+=max(sublist)
print(time)


    

    
    
    


    
    