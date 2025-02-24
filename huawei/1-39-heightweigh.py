"""
输出的按照身高升序，体重升序学生序号

"""
def rankhwightweight():
    N=int(input())
    height=list(map(int,input().split()))
    weight=list(map(int,input().split()))
    lst=[]
    for i in range(len(height)):
        lst.append((height[i],weight[i]))
    ele_dict=dict()
    for idx,ele in enumerate(lst):
        ele_dict[str(idx+1)]=tuple(ele)
    print(ele_dict,"ele_dict")

    sorted_item = sorted(ele_dict,key=lambda item: (ele_dict[item][0],ele_dict[item][1]))
    print(sorted_item)
    index = " ".join(sorted_item)
    print(index)
    return index
if __name__=="__main__":
    rankhwightweight()
