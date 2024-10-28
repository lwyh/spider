#导入re模块
import re
#指定匹配模型为从开始位置匹配数字
pattern = re.compile(r'\d+')
print('\n\n\n')
print('代码运行结果')
print('===========================\n')
#第一句话前面是文本，后面是数字
result = re.search(pattern,'你说什么是呢23333')
#如果匹配成功，打印匹配的内容
if result:
    print(result.group())
else:
    print('匹配失败')
#第二句话前面是数字，后面是文本
result2 = re.match(pattern,'2333333你说什么呢')
#如果匹配成功，则打印匹配结果
if result2:
    print(result2.group())
else:
    print('匹配失败')

#使用.split()将数字之间的文本拆分出来
print(re.split(pattern,'你说双击666都是对的23333哈哈'))
#使用.findall()将所有数字提取出来
print(re.findall(pattern,'你说双击666都是对的23333哈哈'))


print('\n==========')
print('\n\n\n')