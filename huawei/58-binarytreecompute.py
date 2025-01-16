"""
输入的是二叉树的中序遍历叫和前序遍历，重组二叉树，每个节点有原二叉树的左子树和右子树之和组成，输出新的二叉树的中序遍历结果
学会如何更新二叉树，以及如何输出二叉树的中序遍历

"""
def binarytreecompute():
    in_order= list(map(int,input().split()))
    pre_order= list(map(int,input().split()))
    class Node:
        def __init__(self,key):
            self.key=key
            self.left=None
            self.right=None
    
    def build_tree(in_order,pre_order):
        if not  in_order or not pre_order:
            return None
        root=Node(pre_order[0])
        root_index=in_order.index(root.key)
        print(root_index)


        #创建左子树
        if(root_index>0):
            left_subtree=build_tree(in_order[:root_index],pre_order[1:(root_index+1)])
        else:
            left_subtree=None

        #创建右子树
        if(root_index < len(in_order)-1):
            right_subtree=build_tree(in_order[(root_index+1):],pre_order[(root_index+1):])
        else:
            right_subtree=None

        root.left=left_subtree
        root.right=right_subtree
        print(left_subtree,"left_subtree")
        print(right_subtree,"right_subtree")

        return root

    #更新二叉树
    def updatetree(root):
        if not root:
            return 0
        left_sum  = updatetree(root.left)
        right_sum = updatetree(root.right)
        print(left_sum,"left_sum")
        print(right_sum,"right_sum")
        #下面的这行代码取决于是否需要包含原节点本身的值
        original_val = root.key
        print(original_val,"original_val")
        root.key = left_sum + right_sum
    
    # 返回当前节点的值（包括其左子树和右子树的和）
        return original_val + left_sum + right_sum
        

            


    #输出新的二叉树的中序遍历
    lst1=[]
    def inner_traverse(root):
        if not root:
            return None
        inner_traverse(root.left)
        lst1.append(root.key)
        inner_traverse(root.right)
        return lst1
    root = build_tree(in_order,pre_order)
    updatetree(root)
    lst1 = inner_traverse(root)
    print("in_order",lst1)


    



            


    



        



if __name__=="__main__":
    binarytreecompute()