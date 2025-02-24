"""
数组去重，去重后，按照出现的次数降序排序，相同出现次数按照第一次出现的位置的先后进行排序

"""
import numpy as np
def duplicationsorted():
    lst=list(map(int,input().split(",")))
    ele_dict=dict()
    for ele in lst:
        #此处容易写成enumerate,不能用的原因是idx会一直变化，此处只需要第一次出现的索引值即可
        if((lst.index(ele),ele) not in ele_dict):
            ele_dict[(lst.index(ele),ele)]=0
        if((lst.index(ele),ele)  in ele_dict):
            ele_dict[(lst.index(ele),ele)]+=1
    print("ele_dict",ele_dict)
    sorted_items=sorted(ele_dict.items(),key=lambda item:(-item[1],item[0][0]))
    key_list=[item[0][1] for item in sorted_items]
    print(key_list)
    return key_list

        

if __name__=="__main__":
    duplicationsorted()
