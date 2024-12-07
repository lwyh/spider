"""
首尾位都是元音字母的是元音字符串，找到最长长度的子串元音字符串，子串中非元音字母的数量称为瑕疵度
当找不到满足条件的元音符子串时，输出0


"""

def maxyuanyin():
    N=int(input())
    string= input()
    yuan_list=['a','e','i','o','u','A','E','I','O','U']
    yuan_not_site=[]
    count_list=[]
    flaw_list=[]
    flaw_set=set()
    flaw_dict={}
    yuan_end=0
    yuan_start=0
    flaw=[]
    flaw_max={}
    start=0
    end=0
    def is_alpha(str):
        return str.isalpha()
    if(is_alpha(string)):
        for i in range(len(string)):
            if(string[i] not in yuan_list ):
                yuan_not_site.append(i)
        if(len(yuan_not_site)==0):
            if(N==0):
                print(len(string))
            else:
                print(0)
        if(N>len(yuan_not_site)):
            print(0)
        if(N<=len(yuan_not_site)  and N>0):
            #初始化变量存储连续相邻的序列
            consecutive_sequences=[] 
            #遍历列表，找出所有连续相邻的数字序列
            current_sequence=[yuan_not_site[0]]

            for i in range(1,len(yuan_not_site)):
                if(yuan_not_site[i]-yuan_not_site[i-1]==1):
                    current_sequence.append(yuan_not_site[i])
                else:
                    if(current_sequence):
                        consecutive_sequences.append(current_sequence)
                    current_sequence=[yuan_not_site[i]]
            
            if(current_sequence):
                consecutive_sequences.append(current_sequence)

            print(consecutive_sequences)

            #将flaw的所有可能组合输出
            def combine_func(consecutive_sequences):
                for start in range(len(consecutive_sequences)):
                    for end in range(start+1,len(consecutive_sequences)+1):
                        flaw_list=[item for sublist in consecutive_sequences[start:end] for item in sublist]
                        if(len(flaw_list) in flaw_dict):
                            flaw_dict[len(flaw_list)].append(flaw_list)
                        else:
                            flaw_dict[len(flaw_list)]=[flaw_list]         
                #print(flaw_dict)
                return flaw_dict

            #当最后的flaw元素位于字符串尾部时，需要去掉这个元素
            #输出每个flaw点对应的最大的子串的长度
            if(consecutive_sequences[-1][-1]==len(string)-1 and consecutive_sequences[0][0]>0):
                yuan_end=consecutive_sequences[-1][0]
                consecutive_sequences.pop()
                flaw_dict=combine_func(consecutive_sequences)
                print("flaw_dict",flaw_dict)
                flat_list= [item for sublist in consecutive_sequences for item in sublist]
                print("flat_list",flat_list)
                for key,value in flaw_dict.items():
                    for j in range(len(value)):
                        print("min(value[j]",min(value[j]))
                        if(min(value[j])>flat_list[0]):
                            for k in range(len(flat_list)):
                                if(min(value[j])==flat_list[k] ):
                                    start=flat_list[k-1]+1     
                        if(min(value[j])==flat_list[0]):
                            start=0

                        if(max(value[j])<flat_list[-1]):
                            for k in range(len(flat_list)):
                                if(max(value[j])==flat_list[k] ):
                                    end=flat_list[k+1]
                        if(max(value[j])==flat_list[-1]):
                            end=yuan_end
                        print("jk",j,start,end)
                        flaw.append(end-start)
                    flaw_max[key]=max(flaw)
                    flaw=[]
                print("flaw_max",flaw_max)
                for key,value in flaw_max.items():
                    if(key==N):
                        print(value)

                
            
          

            #当最后的flaw元素位于字符串首部时，也需要去掉这个元素
            if(consecutive_sequences[0][0]==0 and consecutive_sequences[-1][-1]<len(string)-1 ):
                yuan_start=consecutive_sequences[0][-1]+1
                consecutive_sequences.pop(0)
                flaw_dict=combine_func(consecutive_sequences)
                flat_list= [item for sublist in consecutive_sequences for item in sublist]
                for key,value in flaw_dict.items():
                    for j in range(len(value)):
                        if(min(value[j])>flat_list[0]):
                            for k in range(len(flat_list)):
                                if(min(value[j])==flat_list[k]):
                                    start=flat_list[k-1]+1
                        if(min(value[j])==flat_list[0]):
                            start=yuan_start

                        if(max(value[j])<flat_list[-1]):
                            for k in range(len(flat_list)):
                                if(max(value[j])==flat_list[k]):
                                    end=flat_list[k+1]
                        if(max(value[j])==flat_list[-1]):
                            end=len(string)-1
                        print("jk",j,start,end)
                        flaw.append(end-start)
                    flaw_max[key]=max(flaw)
                    flaw=[]
                print("flaw_max",flaw_max)
                for key,value in flaw_max.items():
                    if(key==N):
                        print(value)
            
            #当最后的flaw元素位于字符串首部时，同时最开始的flaw元素位于字符串首部
            if(consecutive_sequences[0][0]==0 and consecutive_sequences[-1][-1]==len(string)-1 ):
                yuan_start=consecutive_sequences[0][-1]+1
                yuan_end=consecutive_sequences[-1][0]
                consecutive_sequences.pop(0)
                consecutive_sequences.pop()
                flaw_dict=combine_func(consecutive_sequences)
                flat_list= [item for sublist in consecutive_sequences for item in sublist]
                for key,value in flaw_dict.items():
                    for j in range(len(value)):
                        if(min(value[j])>flat_list[0]):
                            for k in range(len(flat_list)):
                                if(min(value[j])==flat_list[k]):
                                    start=flat_list[k-1]+1
                        if(min(value[j])==flat_list[0]):
                            start=yuan_start

                        if(max(value[j])<flat_list[-1]):
                            for k in range(len(flat_list)):
                                if(max(value[j])==flat_list[k]):
                                    end=flat_list[k+1]
                        if(max(value[j])==flat_list[-1]):
                            end=yuan_end
                        print("jk",j,start,end)
                        flaw.append(end-start)
                    flaw_max[key]=max(flaw)
                    flaw=[]
                print("flaw_max",flaw_max)
                for key,value in flaw_max.items():
                    if(key==N):
                        print(value)


            #当最后的flaw元素不位于字符串首部时，同时最开始的flaw元素不位于字符串首部

            if(consecutive_sequences[0][0]!=0 and consecutive_sequences[-1][-1]<len(string)-1 ):
                flaw_dict=combine_func(consecutive_sequences)
                flat_list= [item for sublist in consecutive_sequences for item in sublist]
                for key,value in flaw_dict.items():
                    for j in range(len(value)):
                        if(min(value[j])>flat_list[0]):
                            for k in range(len(flat_list)):
                                if(min(value[j])==flat_list[k]):
                                    start=flat_list[k-1]+1
                        if(min(value[j])==flat_list[0]):
                            start=0

                        if(max(value[j])<flat_list[-1]):
                            for k in range(len(flat_list)):
                                if(max(value[j])==flat_list[k]):
                                    end=flat_list[k+1]
                        if(max(value[j])==flat_list[-1]):
                            end=len(string)-1
                        print("jk",j,start,end)
                        flaw.append(end-start)
                    flaw_max[key]=max(flaw)
                    flaw=[]
                print("flaw_max",flaw_max)
                for key,value in flaw_max.items():
                    if(key==N):
                        print(value)
                    
           
           


        #瑕疵度为0时的计算
        if(N==0):
            if(yuan_not_site[0] !=0):
                count_list.append(yuan_not_site[0])
            for j in range(1,len(yuan_not_site)):
                if(yuan_not_site[j]-yuan_not_site[j-1] !=1):
                    count_list.append(yuan_not_site[j]-yuan_not_site[j-1]-1)
            print(max(count_list))  
        
  

    return 0
if __name__=="__main__":
    maxyuanyin()