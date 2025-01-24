"""
数据单元的变量替换

将一个 csv 格式的数据文件中包含有单元格引用的内容替换为对应单元格内容的实际值。

comma separated values(CSV) 逗号分隔值，csv 格式的数据文件使用逗号 “,” 作为分隔符将各单元的内容进行分隔。
输入描述

输入只有一行数据，用逗号分隔每个单元格，行尾没有逗号。最多26个单元格，对应编号A~Z。

每个单元格的内容包含字母和数字，以及使用 '<>' 分隔的单元格引用，例如：<A>表示引用第一个单元的值。

每个单元格的内容，在替换前和替换后均不超过100个字符。

引用单元格的位置不受限制，允许排在后面的单元格被排在前面的单元格引用。

不存在循环引用的情况，比如下面这种场景是不存在的：

A单元恪：aCd<B>8U

B单元格：KAy<A>uZq0

不存在多重 '<>' 的情况，一个单元只能引用一个其他单元格。比如下面这种场景是不存在的：

A单元格：aCdOu

B单元格：kAydzco

C单元格：y<<A><B>>d

# ASCII 码中，A 是 65，Z 是 90
char(i+65)
# ASCII 码中，a 是 97，z 是 122
ord(<C>)-ord('A')
1.将循环引用的排除
2.将嵌套引用的排除
"""
def variablereplace():
    inner=list(input().split(","))
    char_dict=dict()
   

    #循环使用，需要去除
    def find_extract_bracket_content_with_level(text):
        stack=[]
        result=[]
        for i ,char in enumerate(text):
            if(char=='<'):
                if (stack):
                    current_level=stack[-1][1]+1
                else:
                    current_level=0
                stack.append((i,current_level))
            elif(char=='>'and stack):
                start,level=stack.pop()
                substring=text[start:i+1]
                content = text[start+1:i]
                result.append((start,i+1,content,level))
            #遇到右括号，但栈为空，说明没有匹配的左括号，
            elif(char=='>'and not stack):
                print(f"warning:unmatched '>' at position {i} ")
                return -1
        #索引已搜索完，但还是有不能匹配的左括号
        if( stack):
            for start,level in stack:
                print(f"warning:unmatched '<' at position {start} ")
                return -1
        return result


    
       
    out=""
    for i in range(len(inner)): 
        print("====================================")
        
        result= find_extract_bracket_content_with_level(inner[i])
        #引用格式报错
        if(result==-1):
            print(-1)
            return -1
        #嵌套引用报错
        if any(result[k][3]>0 for k in range(len(result))):
            print(-1)
            return -1
        
        state=False   
        for j in range(len(inner)):
            if(i<j):
                print("inner[i]",inner[i])
                print("inner[j]",inner[j])
                result_i=find_extract_bracket_content_with_level(inner[i])
                result_j=find_extract_bracket_content_with_level(inner[j])
                #两个都存在引用
                if(len(result_i)>0 and len(result_j)>0):
                    for k in range(len(result_i)):
                        for l in range(len(result_j)):
                            #循环引用报错
                            if((ord(result_i[k][2])-ord('A')==j and ord(result_j[l][2])-ord('A')==i)):
                                print(-1)
                                return -1
                            #嵌套层次为0 ，且不符合循环引用才能提取
                            else:
                                if(result_i[k][3]==0 and result_j[l][3]==0):
                                    print(result_i,"result_i")
                                    print(result_j,"result_j")
                                    while(len(result_i)>0):
                                        inner[i]=inner[i][:result_i[0][0]]+inner[ord(result_i[0][2])-ord('A')]+inner[i][result_i[0][1]:]
                                        print("resulti",result_i[0],inner[i])
                                        result_i = find_extract_bracket_content_with_level(inner[i])
                                        print(inner[i],"11111111111111",result_i)
                                    print(inner[i],"2345")
                                    while(len(result_j)>0):
                                        inner[j]=inner[j][:result_j[0][0]]+inner[ord(result_j[0][2])-ord('A')]+inner[j][result_j[0][1]:]
                                        print("resulti",result_j[0],inner[j])
                                        result_j = find_extract_bracket_content_with_level(inner[j])
                                        print(inner[j],"11111111111111",result_j)
                                    print(inner[j],"2345")
                                    out="".join(inner[i])+","+"".join(inner[j])
                                    print("out",out,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                    state=True
                            if(state):
                                break
                        if(state):
                            break
                if(state):
                    break
                
                #其中有一个不存在引用
                if(len(result_i)>0 and len(result_j)==0):
                    if all(result_i[k][3]==0 for k in range(len(result_i))):
                        while(len(result_i)>0):
                            inner[i]=inner[i][:result_i[0][0]]+inner[ord(result_i[0][2])-ord('A')]+inner[i][result_i[0][1]:]
                            print("resulti",result_i[0],inner[i])
                            result_i = find_extract_bracket_content_with_level(inner[i])
                            print(inner[i],"22222222222222222",result_i)
                        print(inner[i],"2345")
                        out ="".join(inner[i])+","+"".join(inner[j])
                        print("out",out,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        state=True
                if(state):
                    break
                
                
                
                if(len(result_i)==0 and len(result_j)>0):
                    if all(result_j[k][3]==0 for k in range(len(result_j))):
                        while(len(result_j)>0):
                            inner[j]=inner[j][:result_j[0][0]]+inner[ord(result_j[0][2])-ord('A')]+inner[j][result_j[0][1]:]
                            print("resulti",result_j[0],inner[j])
                            result_j = find_extract_bracket_content_with_level(inner[j])
                            print(inner[j],"33333333333333333333333333333",result_j)
                        print(inner[j],"2345")
                        if(i==0):
                            out="".join(inner[i])+","+"".join(inner[j])
                        else:
                            out +=","+"".join(inner[j])
                        print("out",out,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        state=True 
                if(state):
                    break
                if(len(result_i)==0 and len(result_j)==0):
                        print(inner[i],"2345")
                        if(i==0):
                            out="".join(inner[i])+","+"".join(inner[j])
                        else:
                            out +=","+"".join(inner[j])
                        print("out",out,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        state=True
                if(state):
                    break       
            if(state):
                break

    print("-----------------------",out)
    return out
                                      



if __name__=="__main__":
    variablereplace()


"""
 #嵌套使用，嵌套层次大于0，需要去除
    def detect_nested_brackets(text):
        stack=[]
        nested=[]
        for i ,char in enumerate(text):
            if(char =='<'):
                stack.append(i)#将左括号的位置压入栈
            elif(char=='>' and stack):
                start=stack.pop()
                #弹出最近的左括号位置
                if (text[start+1]=='<'):#检查是否为嵌套的<<>>
                    nested.append((start,i+1))
        return nested

"""

