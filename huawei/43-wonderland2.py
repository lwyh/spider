"""
消费最低，玩的日期是固定的，售票方式也是固定的，1日票，3日票，7日票，30日票


"""
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
    #发现一种已经不需要杂交混合了，因为混合的都是介于两个纯的中间，比如既有单日票的又有3日票的会介于只有单日票的和只有3日票的中间
    #只需要对每种进行饱和度的判断即可
    #只有3日票时，如果有组合中的元素长度小于3，则需要降为1日票
    #只有7日票时，如果有组合中的元素长度小于6时，则需要降为1日票 和3日票的组合.如果有连续的3日的话
    #只有30日票时，如果组合中的元素长度小于20时，则需要降为1日票 3日票，7日票的组合，如果有连续的3日或者7日的话
    """
    {1: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [29]], 
    3: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19], [29]], 
    7: [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [29]], 
    30: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 29]]}
    
    
    
    """
    def consecutive_sequences(days):
        sequences=[]
        current_sequence=[days[0]]
        for i in range(1,len(days)):
            if(days[i]==days[i-1]+1):
                current_sequence.append(days[i])
            else:
                if(len(current_sequence)>1):
                    sequences.append((current_sequence[0],current_sequence[-1],len(current_sequence)))
                    current_sequence=[days[i]]
            print(current_sequence)

                
        #追加最后一个连续序列
        if(len(current_sequence)>1):
            sequences.append((current_sequence[0],current_sequence[-1],len(current_sequence)))

        print(sequences)
        return sequences



    consumer=dict()
    #代码中的数字限定主要是根据price之间的关系决定的，还可以进一步泛化
    for key,value in sequences_dict.items():
        consumer[key]=0
        if(key==1):
            for l in range(len(value)):
                consumer[key]+=price[0]*len(value[l])
        if(key==3):
            for l in range(len(value)):
                if(len(value[l])>1 and len(value[l])<3 ):
                    consumer[key]+=price[0]*2
                if(len(value[l])==1):
                    consumer[key]+=price[0]
                if(len(value[l])==3):
                    consumer[key]+=price[1]
        if(key==7):
            for l in range(len(value)):
                if(len(value[l])>=7):
                    consumer[key]+=price[2]
                if(len(value[l])==6):
                    consumer[key]+=price[1]*2
                if(len(value[l])<=5 and len(value[l])>1):
                    num_conseq= consecutive_sequences(value[l])
                    if(len(num_conseq)==0):
                        consumer[key]+=(price[0]*(len(value[l])))
                    else:
                        print(num_conseq)
                        num_list=[item[2] for item in num_conseq]
                        if(3 in num_list  or 4 in num_list or 5 in num_list):
                            consumer[key]+=(price[1]*1+price[0]*(len(value[l])-3))
                        else:
                            consumer[key]+=(price[0]*(len(value[l])))
                if(len(value[l])==1):
                    consumer[key]+=(price[0]*(len(value[l])))

                    
        if(key==30):
            for l in range(len(value)):
                if(len(value[l])>=20):
                    consumer[key]+=price[3]
                if(len(value[l])<20 and len(value[l])>1):
                    num_conseq= consecutive_sequences(value[l])
                    if(num_conseq==0):
                        consumer[key]+=(price[0]*(len(value[l])))
                    else:
                        num_list=[item[2] for item in num_conseq]     
                        for n in range(len(num_list)):
                            num_7=num_list[n]//7
                            num_3=(num_list[n]-7*num_7)//3
                            num_1=num_list[n]-7*num_7-3*num_3
                            consumer[key]+=(price[2]*num_7+price[1]*num_3+price[0]*num_1)
                        consumer[key]+=(price[0]*(len(value[l])-sum(num_list)))
                if(len(value[l])==1):
                    consumer[key]+=(price[0]*(len(value[l])))
    print(consumer)
    minValue=min(consumer.values())
    print(minValue)
    return minValue
 

if __name__=="__main__":
    minSUM()


        