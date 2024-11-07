"""
给定一个连续不包含字符串，该字符串仅包含英文小写字母及英文标点符号（逗号，分号，句号）,同时给定词库，对该字符串进行精确分词


"""

import itertools
def fenciqi():
    arr1 = list(input().split(","))
    arr2=list(input().split(","))
    print(arr2)
    base_dict={}
    count=0
    for l in range(len(arr2)):
        for i in range(len(arr1)):
            for j in range(0,len(arr1[i])):
                for k in range(j+1,len(arr1[i])+1):
                    if(arr1[i][j:k]==arr2[l]):
                        if(arr2[l] in base_dict ):
                            base_dict[arr2[l]].append([j,k])
                        else:
                            base_dict[arr2[l]]=[[j,k]]
    print(base_dict)
    #将dict中所有values值合并成一个大的list
    """
    #使用合并推导式合并列表
    element_list = [item for sublist in base_dict.values() for item in sublist]


    """
    #使用iteratools.chain合并成一个大的list
    element_list = list(itertools.chain(*base_dict.values()))
    print(element_list)

    def min_interval_num(element_list):
        list_com=[]
        for i in range(len(element_list)):
            list_com.append(list(element_list[i]))
            #先按照区间开始大小排序，再按照区间长度降序排列
        list_com.sort(key=lambda x:(x[0],-(x[1]-x[0])))
        #初始话选择区间
        select_list=[]
        #初始化start
        current_start=0
        current_end=1
        select_list.append([current_start,current_end])
        

        for start,end in list_com:
            if( start>=current_end):
                select_list.append([start,end])
                current_end=end
        print(select_list)
        return select_list

    final_list = min_interval_num(element_list)
    print(final_list)

    final_out=[]
    for key,value in base_dict.items():
        for j in range(len(value)):
            for i in range(len(final_list)):
                if(set(value[j]) == set(final_list[i])):
                    final_out.append(key)



    out=','.join(item for item in final_out)


    print(out)

            







    return out








            
            
        





if __name__ == '__main__':
    fenciqi()

