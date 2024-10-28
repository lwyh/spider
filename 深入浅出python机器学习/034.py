import requests
import csv
from bs4 import BeautifulSoup
import re

#指定user agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0'

headers = {'User-Agent':user_agent}
#指定requests发送请求
policies = requests.get("https://www.gov.cn/zhengce/zuixin/home.htm",headers=headers)
#指定编码utf-8
policies.encoding = 'utf-8'
print(policies.text)

#创建soup对象
#将lxml修改为html.parser所有问题解决
p = BeautifulSoup(policies.text,'html.parser')

#用正则表达式匹配所有包含”content“d单词的连接
#div_with_class = p.select_one('div',class_ = 'news_box')

print('\n\n\n')
print('====================================================\n')




contents= p.find_all(href =re.compile( 'content'))







#定义一个空列表
rows = []

#设计一个for循环，将每个数据中的链接和文件进行提取
for content in contents:
    href = content.get('href')
    row = ('国务院',content.string,href)
    #将提取出的内容添加到前面定义的空格中
    rows.append(row)








#定义csv的文件头
header = ['发送部门','标题','链接']
#建立一个名叫policies.csv文件

with  open('D:\\spider\\深入浅出python机器学习\\policies1.csv','w',encoding='gb18030') as f:
    f_csv = csv.writer(f)
    #写入文件头
    f_csv.writerow(header)
    #写入列表
    f_csv.writerows(rows)

print('\n\n\n\最新信息已经获取完成\n结果保存在D:\\spider\\深入浅出python机器学习文件夹下\n\n\n')

