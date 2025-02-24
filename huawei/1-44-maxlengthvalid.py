"""
所有数字，计算结果不能超过long
如果由多个长度一样的，请返回第一个表达式结果
数学表达式，必须是最长的，合法的
操作符不能连续出现，如+..+1是不合法的



"""
import re
import sys
import ast
def maxlengthvalid():
    s=input()
    pattern=r'[0-9+\-]+'
    result=re.findall(pattern,s)
    valid_expression=[expr for expr in result
    if re.search(r'\d',expr) and not re.search(r'[+\-]{2,}',expr)
    and re.search(r'\d$',expr)]
    print(valid_expression)
    if(len(valid_expression)==0):
        print(0)
    if(len(valid_expression)==1):
        #此处的解析表达式需要使用eval
        result= eval(valid_expression[0])
    if(len(valid_expression)>1):
        valid_expression[0]=longest_string
        for string in valid_expression:
            if(len(string)>len(longest_string)):
                longest_string=string 
                result= eval(longest_string)
    print(result)
    return result
    

if __name__=="__main__":
    maxlengthvalid()
    sys.exit()









if __name__=="__main__":
    maxlengthvalid()