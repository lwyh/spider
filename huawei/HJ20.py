# 密码要求:
#1.长度超过8位
#2.包括大小写字母.数字.其它符号,以上四种至少三种
#3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）
#数据范围：输入的字符串长度满足 1≤n≤100 1≤n≤100 
#issupper 大写字母
#islower 小写字母
#isdigit 数字
#else 特殊字符
import sys

password = input()
def check():
    if len(password)<=8:
        return "NG"
     #判断大小写字母，数字，特殊字符的存在性，首先初始化为0
    a,b,c,d = 0,0,0,0
    #从头开始遍历字符串
    for i in password:
        #若满足条件，则直接退出循环，不需要遍历完
        if a+b+c+d >= 3:
            break
        #三种条件依次判断，其他规则为特殊字符
        if i.isupper():
            a =1
        if i.islower():
            b =1
        if i.isdigit():
            c =1
        else:
            d =1
        #如果不满条件，则不通过
    #此处必须是对密码的所有字符进行判断后的数字再进行相加，否则就是循环体内
    print(a+b+c+d)
    if a+b+c+d <3:
            return "NG"
        #循环遍历，若余下的字符串中存在与自己（长度大于2），则不通过
    for j in range(len(password)-3):
        if password.count(password[j:j+3])>1:
            return "NG"
    return "OK"
print(check())
