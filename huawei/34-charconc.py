"""
字符串拼接，从一个字符串中抽出任意N长度的字符串 ，输出给定的字符列表能拼出多少种满足条件的字符串

"""
import itertools
def charconc():
    arr=input().split()
    string,N=arr[0],int(arr[1])
    word_list=[]
    combinations_list=[]
    combinations_list2=[]
    perm_set=set()
    perm_list=[]
    delete_index=[]
    delete_ele=[]
    #判断输入是否是只包含小写字母
    def is_lowercase_alpha(s):
        return s.isalpha() and s.islower()
    #将字符中取出任意N字符 
    stat_boolean=[True]*(len(string))
    print(stat_boolean)
    def rank_categories():
        for word in string:
            word_list.append(word)
        #将所有的字符的组合全部输出
        combinations_list=list(itertools.combinations(word_list,N))
        print(combinations_list)
        #将所有的字符组合的全部排列输出，并且排列相同的字符组合集合去重
        for i in range(len(combinations_list)):
            permutations = itertools.permutations(combinations_list[i])
            for perm in permutations:
                perm_str = ''.join(perm)
                perm_set.add(perm_str)
                print(perm_str)
        perm_list=list(perm_set)
        #将所有相邻字符的组合单独组合成一个列表，并从原列表中去除
        for j in range(len(perm_list)):
            for k in range(len(perm_list[j])-1):
                if(perm_list[j][k]==perm_list[j][k+1]):
                    delete_ele.append(perm_list[j])
        select_ele = [item for item in perm_list if item not in delete_ele ]
        combinations_num=len(select_ele)
        print(select_ele,combinations_num)
        return combinations_num
    

    if(N==len(string) and  is_lowercase_alpha(string)):
        return 1
    if(N>len(string) or not is_lowercase_alpha(string)):
        return 0
    if(N< len(string) and is_lowercase_alpha(string)):
        return rank_categories()
         
if __name__=="__main__":
    charconc()   
    


   
                


            

            

            






     

