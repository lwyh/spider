"""
描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。


提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：

先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开
输出描述：

输出合并后的键值对（多行）


输入：

4
0 1
0 2
1 2
3 4

输出：

0 3
1 24

3 4



总结为：
1.去重id  
2.通过去重id生成count值为空的dict
3.先循环目标数据，再循环去重后的dict 通过if判断，相同则相加，不同则跳过，这样就达到了dict相加的目的
"""

n =int(input())
arr = []
lid = []
res = []
for i in range(n):
    arr.append(list(map(int,input().split())))
#统计list中的key,将不同的key放在一个list中
for j in range(len(arr)):
        if arr[j][0] not in lid:
            lid.append(arr[j][0])
#结果列表res[]
for k in lid:
     res.append([k,0])
#将相同的key对应的values相加,追加到结果列表中res[]中
for k in range(len(arr)):
     for l in range(len(res)):
          if arr[k][0]==res[l][0]:
               res[l][1] = arr[k][1] +res[l][1]
print(res)
               
               

     

