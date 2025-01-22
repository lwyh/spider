"""
子串中只包含一个字母，其余全是数字，求最长的子串的长度

"""
def maxsubstring():
    string = input()
    def check_letter(s):
        letter_count=0
        digit_count=0
        for sub in s:
            if(sub.isalpha()):
                letter_count+=1
            elif(sub.isdigit()):
                digit_count+=1
            else:
                return False
        #必须在包含了一个字母的同时，数字的个数必须要有，并且个数还要满足要求
        return letter_count==1 and digit_count> 0 and digit_count==len(s)-1

    avialble_s=[]
    if(string.isalpha() or string.isdigit()):
        print(-1)
        return -1
    else:
        for i in range(len(string)):
            for j in range(i+1,len(string)+1):
                if(check_letter(string[i:j])):
                    avialble_s.append(string[i:j])
        print("avialble_s",avialble_s)
        if(len(avialble_s)==1):
            out=len(avialble_s[0])
        if(len(avialble_s)>1):
            out = max([len(sublist) for sublist in avialble_s ])
        print(out)
        return out
               
            
            


if __name__=="__main__":
    maxsubstring()