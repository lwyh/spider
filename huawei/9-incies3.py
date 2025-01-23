"""
题目描述

K小姐是一位伐木工人，她有一根长度为 XX 米的原木。为了获得最大的收益，她需要将原木切割成若干段，每一段的长度都必须是正整数。

木材交易价格为每根木头长度的乘积，也可以不切割，拿整根原木进行交易，其交易价格等于原木长度。

现在，请你帮助K小姐计算，要想获得最大收益，并且切割次数尽量少，她应该如何切割这根原木？

输入格式

输入仅一行，包含一个正整数 XX，表示原木的长度。
输出格式

输出若干个正整数，表示切割后每一段木材的长度。你需要按照长度从小到大的顺序输出，相邻两个数之间用一个空格隔开。

如果有多种切割方案都能获得最大收益，你可以输出任意一种。

解题思路：
本题新思路，先将树打碎，即本题中的ss_list,然后从任意位置进行切分，然后得出所有的组合，然后继续进行计算加和求积

"""
import numpy as np
def maxamount():
    inner=input()
    N=int(inner.strip())
    ss_list=[1]*N
    print(ss_list)
    def split_combination(ss_list):
        def backtrack(start,path):
            if(start==len(ss_list)):
                result.append(path[:])
                return
            
            for i in range(start+1,len(ss_list)+1):
                path.append(ss_list[start:i])
                backtrack(i,path)
                path.pop()
        result=[]
        backtrack(0,[])
        return result

    all_combinations =split_combination(ss_list)
    star=dict()
    for sublist in all_combinations:
        sum_list=[sum(sublist[i]) for i in range(len(sublist))]
        print("sum_list",sum_list)
        amount=np.prod(sum_list)
        print(amount,"amount")
        count=len(sum_list)-1
        #由于列表是可变化的，所以不能作为字典的key,可以将列表转化成tuple
        star[tuple(sum_list)]=(amount,count)
    print("star",star)
    value_list=list(star.values())
    #此处主要是对交易价格进行降序，同时对切割次数进行升序
    sorted_date = sorted(value_list,key=lambda item:(-item[0],item[1]))
    print("sorted_date===================",sorted_date)
    out_list=[key for key,value in star.items() if value ==sorted_date[0] ]
    print((out_list))

    # 对每个元组排序后去重，元组中的元素是不可变化的，所以之后的去重只是针对元组去重了，不会对元组中的元素也去重了
    unique_combinations = list(set(tuple(sorted(item)) for item in out_list))

    print(unique_combinations)

    #输出的格式
    print( " ".join(map(str,unique_combinations[0])))


    
    


if __name__=="__main__":
    maxamount()


        

        
        
        




