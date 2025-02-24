"""
S字符串中每个字符在L字符串的顺序一致，可以不连续，则输出最后一个字符在L只出现的的位置
否则判断为不一致，输出-1


"""
def subString():
    str1=input()
    str2=input()
    def is_lower_and_is_alpha(s):
        return s.islower() and s.isalpha()

    char_index=[]
    if(is_lower_and_is_alpha(str1) and is_lower_and_is_alpha(str2)):
        for char in str1:
            if(char not in str2):
                print("-1")
                return -1
            if(char in str2):
                char_index.append(str2.index(char))
        print("char_index",char_index)
        sort_index=sorted(char_index)
        print("sort_index",sort_index)
        if(sort_index ==char_index and  len(char_index)==len(str1)):
            print(char_index[-1])
            return 0
        else:
            print("-1")
            return -1
if __name__=="__main__":
    subString()

            

        
