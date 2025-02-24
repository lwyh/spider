"""
输入一个字符串s,字符串串s首位相连成一个环形，请你在环中找出'o'字符出现偶次最长子字符串的长度
输入是遗传小写字母组成的字符串
输出一个整数


"""
def maxlenstring():
    s=input()
    str1=s+s
    char_list=[]
    if(s.count("o")==0):
        print(len(s))
        out=len(s)
    else:
        for i in range(len(s)):
            for j in range(i+1,len(s)+i):
                if(str1[i:j].count("o")%2==0):
                    char_list.append(str1[i:j])
        print("char_list",char_list)
        if(len(char_list)==0):
            out=len(char_list[0])
        else:
            out = max([len(ele) for ele in char_list])
            print(out)


    
    return out
if __name__=="__main__":
    maxlenstring()

    
