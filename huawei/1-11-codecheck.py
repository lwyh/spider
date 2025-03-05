"""
输入密码验证是否符合要求
密码安全要求如下：
1.密码长度=8：
2.密码至少需要包含1个大写字母
3.密码至少需要包含1个小写字母，
4密码至少需要包含1个数字
5.密码至少需要包含1个字母和数字以外的非空白特殊字符
 
"""
import re
def codecheck():
    string=input()
    def check_things(s):
        has_upper = re.search(r'[A-Z]',s) is not None
        has_lower = re.search(r'[a-z]',s) is not None
        has_digit = re.search(r'[0-9]',s) is not None #正则表达式的方式不能错，否则无法做判断
        has_special = re.search(r'[^\sA-Za-z0-9]',s) is not None and "<" not in s
        return has_upper and has_lower and has_digit and has_special

    result=""
    for i in range(len(string)):
        
        #首个字符是<
        if(i==0  and string[i:i+1]=="<"):
            string=string[1:]
        #中间字符有<
        
        if(i>0 and string[i:i+1]=="<"):  
            print(string[i:i+1])  
            string=string[:i-1]+string[i+1:]
            print(string)
        #末尾字符是<
        if(i>0 and string[-1:]=="<"):
            print(string,"string")
            string=string[:-2]
            print(string,"string")
          
    print(string,"werfg")
    if(string==[]):
        result=" "+","+"false"
    else:
        if(not check_things(string)):
            result=string+",false"
        if(check_things(string)):
            result=string+",true"
    print(result)
    return result
if __name__=="__main__":
    codecheck()
