#描述： 实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
#数据范围：输入的字符串长度满足 1≤n≤20 1≤n≤20  ，保证输入的字符串中仅出现小写字母
import sys

k = input()

def delta(a):
    for i in a:
            if(not a.islower()):
                continue
            if(len(a) >20):
                continue
            if(a.islower()) and (len(a) <=20): 
                if(a.count(i)==1):
                     return a.replace(i,'')

            
k = delta(k) 
def beta(a):
     for i in a:
          if(a.count(i) >1): 
            return delta(a) 
print(beta(k))  
     


