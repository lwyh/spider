"""
字符串s,最多进行依次变换，返回变换后得到的最小字符串
交换规则：交换字符中任意两个不同位置的字符
"""
def minstring():
    s=input()
    def swap_char(s,i,j):
        s_list=list(s)
        s_list[i],s_list[j]=s_list[j],s_list[i]
        return "".join(s_list)
    #注意不要漏掉字符串本身
    avialble_string=[s]
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            avialble_string.append(swap_char(s,i,j))
    print("avialble_string",avialble_string)
    sorted_string = sorted(avialble_string)
    out=sorted_string[0]
    print(out)
    return out
if __name__=="__main__":
    minstring()
            
