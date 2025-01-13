"""
二叉树，后序遍历（左孩子->右孩子->父节点），中序遍历（左孩子->父节点->右孩子），
通过输入后序遍历，中序遍历结果
26个大写字母组成二叉树的父子节点，输出二叉树的层次遍历结果
https://blog.csdn.net/sinat_30324577/article/details/82688414  参考链接

层次遍历列表是不区分左右子树的，所以重建二叉树递归时，左右子树的递归时，层次遍历列表不变
层次遍历的第一个元素就说根节点，前序遍历也是一样
中序遍历的根节点的位置不确定，但是根节点左边的是左子数，右边是右子树
后序遍历的根节点是最后一个元素是根节点
"""
def binarytree():
    array=list(input().split())
    post_order=[]
    in_order=[]
    for item in array[0]:
        post_order.append(item)
    for ele in array[1]:
        in_order.append(ele)
    print(post_order,in_order)
    class Node:
        def __init__(self,key):
            self.key = key
            self.left=None
            self.right=None





    #重建二叉树
    def build_tree(post_order,in_order):
        if not  post_order or not in_order:
            return None
        root = Node(post_order[-1]) #根节点是后序遍历的最后一个元素
        root_index= in_order.index(root.key)
        #left_subtree = build_tree(post_order[1:post_order.index(in_order[0]), 1:])
        #构建左子树
        if (root_index>0):
            left_subtree = build_tree(post_order[:root_index],in_order[:root_index])
        else:
            left_subtree = None

        #构建右子树
        if(root_index <len(in_order)-1):
            right_subtree  = build_tree(post_order[root_index:len(post_order)-1],in_order[root_index+1:])
        else:
            right_subtree = None

        
        root.left = left_subtree
        root.right = right_subtree
        return root
    #输出二叉树结构
    binarytree=build_tree(post_order,in_order)
    print(binarytree.key)

    #输出二叉树层次遍历结果
    def level_order_traversal(root):
        if not root:
            return []
        queue=[root]
        result=[]
        while queue:
            node1=queue.pop(0)
            result.append(node1.key)
            if(node1.left):
                queue.append(node1.left)
            if(node1.right):
                queue.append(node1.right)
        return result

    out = level_order_traversal(binarytree)
    print(level_order_traversal(binarytree))

    lst2=[]
    #输出叶节点
    def leaf(root):
        if not root:
            return None
        if not root.left and not root.right: #直到节点不存在左右子数，则为叶节点
            lst2.append(root.key)
        leaf(root.left)
        leaf(root.right)
        return lst2

    leaf = leaf(binarytree)
    print(leaf)

    
    lst1=[]
    #输出前序遍历结果

    def pre_traverse(root):
        if not root:
            return None
        lst1.append(root.key)
        pre_traverse(root.left)
        pre_traverse(root.right)
        return lst1
    pre_order = pre_traverse(binarytree)
    print("pre_order",pre_order)

    return out



if __name__=="__main__":
    binarytree()







