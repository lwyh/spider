"""
任务链，输入任务之间的血缘依赖
输出任务执行的列表

"""
import itertools
def multitask():
    leff_list=[] 
    right_list=[]
    left_list2=[]
    right_list2=[]
    super_oplist=[]
    infer_oplist=[]
    arr1=list(input().split(" "))
    for i in range(len(arr1)):
        leff_list.append(arr1[i].split("->")[0])
        right_list.append(arr1[i].split("->")[1])
    print(leff_list,right_list)
    super_op=list(set(right_list)-set(leff_list))
    infer_op=list(set(leff_list)-set(right_list))
    intersec_op=list(set(leff_list)&set(right_list))
    print(intersec_op)
    print(arr1)
    #中间任务链包含需要连环的任务血缘
    while (len(intersec_op)>1):
        for j in range(len(arr1)):
            if(len([char for char in arr1[j] if char in intersec_op]) == 2):
                left_list2.append(arr1[j].split("->")[0])
                right_list2.append(arr1[j].split("->")[1])
        print(left_list2,right_list2)
        insuper_op=list(set(right_list2)-set(left_list2))
        ininfer_op=list(set(left_list2)-set(right_list2))
        intersec_op=list(set(left_list2)&set(right_list2))
        insuper_op.sort()
        ininfer_op.sort()
        intersec_op.sort()
        left_list2=[]
        right_list2=[]
        super_oplist=super_oplist+insuper_op
        infer_oplist=ininfer_op+infer_oplist
    print(intersec_op)

        

    #此处不能直接在上述的生成的列表直接sort,需要生成列表后才能有此操作
    super_op.sort()
    infer_op.sort()
    list1 = super_op+super_oplist+intersec_op+infer_oplist+infer_op
    print(list1)

if __name__=="__main__":
    multitask()