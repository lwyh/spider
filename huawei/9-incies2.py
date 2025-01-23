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

"""
import numpy as np
def maxamount():
    inner=input()
    N=int(inner.strip())
    out_dict=dict()
    out_list=tuple()
    value_list=[]
    out=0
    split_combine=[]
    def split(N,split1,count):
        for k in range(1,N-1):
            count=1
            split1.append(k)
            for i in range(1,N-k):
                split1.append(i)
                split1.append(N-k-i)
                count+=1
                split_combine.append(N)
                split_combine.append(split1[:])
                print("split_combine",split_combine)
                if(N%2==0 and N-k-i==0):
                    amount=np.prod(split_combine[0])
                    index=0
                    for j in range(len(split_combine)):
                        if(np.prod(split_combine[j])>amount):
                            amount=np.prod(split_combine[j])
                            index=j
                    print("amount",amount)
                    out_dict[tuple(split_combine[index])]=(amount,count)
                    print("out_dict",out_dict)
                    count-=1
                if(N%2==1 and N-i-i==1):
                    amount=np.prod(split_combine[0])
                    for j in range(len(split_combine)):
                        if(np.prod(split_combine[j])>amount):
                            amount=np.prod(split_combine[j])
                    print("amount",amount)
                    out_dict[tuple(split1)]=(out,count)
                    print("out_dict",out_dict)
                    count-=1
                split1.pop()
                split1.pop()
            split1=[] 
        split(N-k,split1,count)              
        print(out_dict)
        value_list=list(out_dict.values())
        sorted_date = sorted(value_list,key=lambda item:(-item[0],item[1]))
        out_list=[key for key,value in out_dict.items() if value ==sorted_date ]
        print(out_list)
        return out_list
    out_list = split(N,[],0)
    return out_list

if __name__=="__main__":
    maxamount()


        

        
        
        




if __name__=="__main__":
    maxamount()


