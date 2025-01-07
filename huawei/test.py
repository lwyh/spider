import math
def minSUM():
    price=list(map(int,input().split()))
    days=list(map(int,input().split()))
    #先将间隔在30天以内的假期日分组，然后遍历取最小的花销
    current_sequence=[]
    sequences_dict=dict()
    type_list=[1,3,7,30]
    for k in range(len(type_list)):
        current_sequence=[days[0]]
        for i in range(1,len(days)):
            if(days[i]-current_sequence[0]>=type_list[k] and days[i-1]-current_sequence[0]<type_list[k]):
                indx_0=days.index(current_sequence[0])
                print(indx_0)
                current_sequence.append(days[(indx_0+1):i])
                sequences_list=[item for sublist in current_sequence for item in (sublist if isinstance(sublist,list) else [sublist])]     
                if type_list[k] in sequences_dict:
                    sequences_dict[type_list[k]].append(sequences_list)
                else:
                    sequences_dict[type_list[k]]=[sequences_list]
                current_sequence=[days[i]]
            


            
        #追加最后一个连续序列
        if(len(current_sequence)>=1):
            indx_0=days.index(current_sequence[0])
            current_sequence.append(days[(indx_0+1):])
            current_apprex=[item for sublist in current_sequence for item in (sublist if isinstance(sublist,list) else [sublist])]
            if type_list[k] in sequences_dict:
                sequences_dict[type_list[k]].append(current_apprex)
            else:
                sequences_dict[type_list[k]]=[current_apprex]
    print(sequences_dict)
    #获取每个元素组的最小花费
    #首先需要获取每个元素组内每张1，3，7，30票的组合数

if __name__=="__main__":
    minSUM()

