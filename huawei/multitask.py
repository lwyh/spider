"""
任务链，输入任务之间的血缘依赖
输出任务执行的列表

"""
import itertools
def multitask():
    leff_list=[] 
    right_list=[]
    arr1=list(input().split(" "))
    for i in range(len(arr1)):
        leff_list.append(arr1[i].split("->")[0])
        right_list.append(arr1[i].split("->")[1])
    print(leff_list,right_list)
    super_op=list(set(right_list)-set(leff_list))
    infer_op=list(set(leff_list)-set(right_list))
    intersec_op=list(set(leff_list)&set(right_list))
    #此处不能直接在上述的生成的列表直接sort,需要生成列表后才能有此操作
    super_op.sort()
    intersec_op.sort()
    infer_op.sort()
    list1 = super_op+intersec_op+infer_op
    print(list1)

if __name__=="__main__":
    multitask()