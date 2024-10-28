"""
@Description :kmp算法  
描述
给你一个文本串 T ，一个非空模板串 S ，问 S 在 T 中出现了多少次

数据范围：1≤len(S)≤500000,1≤len(T)≤10000001≤len(S)≤500000,1≤len(T)≤1000000
要求：空间复杂度 O(len(S))O(len(S))，时间复杂度 O(len(S)+len(T))O(len(S)+len(T))
示例1
输入：
"ababab","abababab"
返回值：
2
@Author      :   hermione
@Time        :   2024/05/15 17:43:39
"""
"""
#此处容易误用count,但count在此处是不能用，因为count对于已经统计过的不会重复统计
word = input()
def countNUm():
    list = word.split(',')
    a0 = list[0].replace('"','')
    a1 = list[1].replace('"','')
    ans=0
    for i in range(len(list[1])):
        #本题的另一个易错点就是字符串中输入的双引号是需要去除再统计字符串出现的次数
        if(a1.count(a0)==0):
            break
        else:
            if(a1[i:i+len(a0)]==a0):
                ans +=1
    return ans
print(countNUm())

"""




#class Solution:
 
     
def kmp(self , S , T ):
        def get_next(p):
            n = [-1] * (len(p)+1)
            print(n)
            k = -1
            j = 0
            while j < len(p):
                if k == -1 or p[j] == p[k]:
                    k +=1
                    j +=1
                    n[j] = k
                else:
                    k = n[k]
 
 
            return n
         
        next_arr = get_next(S)
        j = 0
        result = 0
        i = 0
        while i < len(T):
            if j == -1 or T[i] == S[j]:
                i +=1
                j +=1
            else:
                j = next_arr[j]
                 
            if j == len(S):
                result +=1
                j = next_arr[j]
        
        return result
   

