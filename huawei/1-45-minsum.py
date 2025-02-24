"""
字符串中整数部分的最小和

[+-]?\d+ 表示匹配正负号以及整数部分的正则表达
"""
import re
def minsum():
    s=input()
    patterns=r'[+-]?\d+'
    result=re.findall(patterns,s)
    print(result)
    nums=[]
    for i in range(len(result)):
        if(result[i].count("-")>0):
            nums.append(int(result[i]))
        if(result[i].count("-")==0):
            for ele in result[i]:
                nums.append(int(ele))
    print(nums)
    sums = sum(nums)
    print(sums)
    return sums

if __name__=="__main__":
    minsum()
