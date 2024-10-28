#导入request库
import requests
from bs4 import BeautifulSoup
import re
import time

#指定user agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0'
headers = {'User-Agent':user_agent}

#创建一个空列表
all_jokes = []
#设置for循环，让爬虫从第一页爬到第50页
for i in range(1,50):
    content = requests.get('https://www.biedoul.com/wenzi/{}'.format(i),headers=headers)
#去掉网页中的<br>和<br/>
    replaced = content.text.replace('<br>','').replace('<br />','').replace('<br/>','')
#使用BeatifulSoup提取段子的正文
    soup = BeautifulSoup(replaced,'html.parser')
    #print(soup)
    jokes = soup.find_all('dl',class_ = 'xhlist')
    #print(jokes)
    for joke in jokes:
        #title = joke.a.string
        text = joke.get_text('p')
        text = text.replace('p',' ')
        text = text.split("评论")
        #print(text)
        #print('================================================================')
#将段子添加到列表中
       # all_jokes.append(title)
        all_jokes.append(text[0])
        all_jokes.append('\n')
#打印正在爬取的页面
    print('正在爬取第{}页'.format(i))
    #设置每爬取一夜，休眠2s，避免给服务器带来过大负担
    time.sleep(2)


#以写入模式打开txt文件，编码utf-8
with open('D:\\spider\\深入浅出python机器学习\\joke.txt','w',encoding='utf8') as f:
    for j in all_jokes:
        f.write(str(j))
        f.write('\n')


