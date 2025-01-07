"""
字符串全排列，相同的字符排列交换顺序可以视为一种组合，最终排列按照字母升序输出



"""
def  charRank():
    N=int(input())
    arry = list(input().split())
    combine_list=[]
    combine_char_list=set()
    for i in range(len(arry)):
        for j in range(len(arry) ):
            if(j!=i):
                for k in range(len(arry)):
                    if(k!=j and k!=i):
                        combine_list.append([arry[i],arry[j],arry[k]])
    print(combine_list)
    for l in range(len(combine_list)):
        combine_char_list.add(''.join(combine_list[l]))
    sorted_list = sorted(list(combine_char_list))
    for element in sorted_list:
        print(element)


if __name__=='__main__':
    charRank()

             