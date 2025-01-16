"""
字符串首位相连,找到字符l,o,x出现偶数次的最长子字符串的长度



"""
def max_length():
    string_in = input()
    #本题的巧妙处就是因为 字符串是首位相连的，所以可以将两个相同字符串相连来取子字符串
    string = string_in+string_in
    print(string)
    avialble_lox=[]
    #本题重点是确认符合条件的子字符串的首位的界限，否则会漏掉一些
    for i in range(len(string_in)):
        for j in range(i+1,len(string_in)+i+1):
            if(string[i:j].count('l')%2==0 and string[i:j].count('x')%2==0  and string[i:j].count('o')%2==0):
                avialble_lox.append(string[i:j])
    print(avialble_lox)
    max_length=max(len(item) for item in avialble_lox)
    print(max_length)
    return max_length

if __name__=="__main__":
    max_length()

            



