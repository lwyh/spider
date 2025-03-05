"""
均衡字符串只包含两种字符，且两种字符的个数相同
给定一个均衡字符串，请给出可分隔成新的均衡子串的最大个数

"""
def maxsubsring():
    string=input()
    length_lst=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if(string[i:j].count("X")==string[i:j].count("Y")):
                print("string[i:j]",string[i:j])
                length_lst.append(int(len(string[i:j])/2))
    print(length_lst)
    if(length_lst==[]):
        result=0
    else:
        result=max(length_lst)
    print(result)
    return result
if __name__=="__main__":
    maxsubsring()

