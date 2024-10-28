"""

当一个字符串满足如下条件时，我们称它是 美丽的 ：

    所有 5 个英文元音字母（'a' ，'e' ，'i' ，'o' ，'u'）都必须 至少 出现一次。
    这些元音字母的顺序都必须按照 字典序 升序排布（也就是说所有的 'a' 都在 'e' 前面，所有的 'e' 都在 'i' 前面，以此类推）

比方说，字符串 "aeiou" 和 "aaaaaaeiiiioou" 都是 美丽的 ，但是 "uaeio" ，"aeoiu" 和 "aaaeeeooo" 不是美丽的 。

给你一个只包含英文元音字母的字符串 word ，请你返回 word 中 最长美丽子字符串的长度 。如果不存在这样的子字符串，请返回 0 。

子字符串 是字符串中一个连续的字符序列。

示例 1：

输入：word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
输出：13
解释：最长子字符串是 "aaaaeiiiiouuu" ，长度为 13 。


"""

word = input()
def longestBeatifulSubstring():
        ans = 0
        i,n = 0,len(word)
        while i<n:
            #没有元音字母a,直接到下一个子字符串
            if word[i] != 'a':
                i+=1
                continue
            #并将第一次出现a的位置记为start,并且创建集合，满足至此开始，之后出现的元音字符都写进set集合中，并且不能重复，且位置越靠后的字母序列越大
            start = i
            i+=1
            print(i)
            g = set()
            g.add('a')
            print(g)
            while i<n and word[i]>=word[i-1]:
                g.add(word[i])
                i+=1
                print(i)
            #在找到所有满足元音升序列后的子字符串后，由于之前说的是必须条件之一是aeiou都必须出现，因此这个集合的长度其实是固定的5，这是隐藏的条件
            if len(g) ==5:
                ans = max(ans,i-start)
        return ans
print(longestBeatifulSubstring())







        


