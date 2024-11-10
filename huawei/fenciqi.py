"""
给定一个连续不包含字符串，该字符串仅包含英文小写字母及英文标点符号（逗号，分号，句号）,同时给定词库，对该字符串进行精确分词


"""

import itertools
import re
def fenciqi():
    arr1 = list(re.split(r'[,.;]',input()))
    arr2=list(input().split(","))
    print(arr2)
    #将所有的词库在源字符串中拆分开，并且以词库，出现的位置为key,value按照dict保存
    base_dict={}
    count=0
    #第二种情况是单个字母不在词库中且不成词语则直接输出单个字母
    #to do 第四种情况是itit这种保证输出是i,t,i,t，目前输出是i,i,t,t，有待优化
    def check_no_match(mainstring,check_list):
        #将需要匹配的词库连接成一个正则表达式
        pattern ="|".join(re.escape(word) for word in check_list)

        #编译正则表达式
        regex = re.compile(pattern)
        for j in range(0,len(mainstring)):
            for k in range(j+1,len(mainstring)+1):
                if not regex.search(mainstring[j:k]):
                    if(mainstring[j] in base_dict):
                        base_dict[mainstring[j]].append([j,j+1])
                    else:
                        base_dict[mainstring[j]]=[[j,j+1]]
        return base_dict
                    
                    



        

    def check_in_match(str1,str2):
        for j in range(0,len(str1)):
            for k in range(j+1,len(str1)+1):
                for l in range(len(str2)):
                    if(str1[j:k]==str2[l]):
                        if(str2[l] in base_dict ):
                            base_dict[str2[l]].append([j,k])
                        else:
                             base_dict[str2[l]]=[[j,k]]
        return base_dict
                    

         


     #将dict中所有values值合并成一个大的list
    """
    #使用合并推导式合并列表
    element_list = [item for sublist in base_dict.values() for item in sublist]


    """
        #使用iteratools.chain合并成一个大的list
    """
        list_com=[]
        for i in range(len(element_list)):
            list_com.append(list(element_list[i]))
    """

    final_out=[]
    for i in range(len(arr1)):
        check_in_match(arr1[i],arr2)
        check_no_match(arr1[i],arr2)
        print(base_dict)
        element_list = list(itertools.chain(*base_dict.values()))
        print(element_list)

       
        

        def min_interval_num(element_list):
        
            #先按照区间开始大小排序，再按照区间长度降序排列
            element_list.sort(key=lambda x:(x[0],-(x[1]-x[0])))
            #初始话选择区间
            select_list=[]
            #初始化start
            current_start=0
            current_end=float('-inf')
        
        #这步骤是将最长区间长度的选出来，以最少区间数来表示，确保第一种情况最长字符长度匹配以及不重叠字符拆分
        #第二种情况是单个字母不在词库中且不成词语则直接输出单个字母
        #第三种情况是需要拆分的是长串的带有标点符号的是逗号，分号或者句号的长文本
            for start,end in element_list:
                if( start>=current_end):
                    select_list.append([start,end])
                    current_end=end
            print(select_list)
            return select_list

        final_list = min_interval_num(element_list)
        print(final_list)

        stage_out=[]
        
        for value in final_list:
            for key,dict_values in base_dict.items():
                if(value in dict_values):
                        stage_out.append(key)                   
        print(stage_out)
        base_dict={}
        final_out.append(stage_out)
    out=','.join(item for upout in final_out for item in upout)
    print(out)
    return out
if __name__ == '__main__':
    fenciqi()

