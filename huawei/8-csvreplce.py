"""
数据单元的变化替换

将一个 csv 格式的数据文件中包含有单元格引用的内容替换为对应单元格内容的实际值。

comma separated values(CSV) 逗号分隔值，csv 格式的数据文件使用逗号 “,” 作为分隔符将各单元的内容进行分隔。
输入描述

输入只有一行数据，用逗号分隔每个单元格，行尾没有逗号。最多26个单元格，对应编号A~Z。

每个单元格的内容包含字母和数字，以及使用 '<>' 分隔的单元格引用，例如：<A>表示引用第一个单元的值。

每个单元格的内容，在替换前和替换后均不超过100个字符。

引用单元格的位置不受限制，允许排在后面的单元格被排在前面的单元格引用。

不存在循环引用的情况，比如下面这种场景是不存在的：

A单元恪：aCd<B>8U

B单元格：KAy<A>uZq0

不存在多重 '<>' 的情况，一个单元只能引用一个其他单元格。比如下面这种场景是不存在的：

A单元格：aCdOu

B单元格：kAydzco

C单元格：y<<A><B>>d





"""


import re
def shujudanyuan(s):
    s=s.split(',')
    fa = [0 for _ in range(len(s))]
    stack = []
    def dfs(index):
        if len(re.findall(r'<[A-Z]>',s[i])) == 1 and len(re.findall('<',s[i]))==1 and len(re.findall('>',s[i]))==1 or not re.search(r'<',s[i]) and  not re.search(r'>',s[i]):
            valid=1
        else:
            valid=0
        if not valid:
            return 1/0
        fa[index]=1
        if not re.search(r'<[A-Z]>',s[index]):
            return s[index]
        else:
            n,m = re.search(r'<[A-Z]>',s[index]).span()
            newindex = ord(s[index][n+1:m-1])-ord('A')
            stack.append(index)
            temp = dfs(newindex)
            s[index] = re.sub('<[A-Z]>',temp,s[index])
            stack.pop()
            return temp
        
    for i in range(len(s)):
        if not fa[i]:
            try:
                dfs(i)
            except:
                return -1

    return ','.join(s)
print(shujudanyuan('aCd,<A>8U'))
        

