#导入requests库
import requests
#导入beautifulsoup库
from bs4 import BeautifulSoup
#指定user agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0'

headers = {'User-Agent':user_agent}


#requests库请求的语句是requests.get
r = requests.get("https://www.gov.cn/zhengce/content/202407/content_6963543.htm",headers=headers)
r.encoding = 'utf-8'
#打印结果
#print(r.text)


#创建soup对象
soup = BeautifulSoup(r.text,'lxml')
print(soup)

#div_with_class = soup.find_all('div',class_='b12c pages_content#UCAP-CONTENT')
div_with_class = soup.select_one("div.b12c.pages_content#UCAP-CONTENT")
text_content=''
if div_with_class:
    paragraphs = div_with_class.find_all('p')
    for p in paragraphs:
        if not p.find('img'):
            paragraph_text = p.get_text(strip=True)
            if paragraph_text:
                text_content += p.get_text() +'\n'

print(text_content.strip())

link = soup.find_all('a')[3]
print(link)




#指定保存html文件路径，文件名和编码方式
with open('D:\\spider\\深入浅出python机器学习\\requests.html','w',encoding='utf8') as f:
    f.write(r.text)

print('\n\n\n')
print('代码运行结果')
print('===========================================\n')
#使用.encoding查询编码方式
print('编码方式: ',r.encoding)
#使用.'标签名'即可提取这部分内容
#print(soup.title.string)
print(soup.title.get_text())
print(link.get('href'))
print('\n========================================')
print('\n\n\n')