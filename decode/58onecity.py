from bs4 import BeautifulSoup
import requests
import xlwt
import re
from openpyxl import Workbook  
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
#这是创建一个excel，并创建一个sheet表，设置属性
workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('My Worksheet')
worksheet.col(0).width = 14000
worksheet.col(5).width = 24000
#发送请求
url = 'http://sz.58.com/ershoufang/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d30000c-0000-4591-0324-370565eccba8&ClickID=1'
res = requests.get(url = url,headers= headers)
con = res.text
#实例化一个对象
soup  = BeautifulSoup(con,'lxml')
#li_list = soup.find(class_ = 'property')
#获取第一页的所有房产
first = soup.find('section', class_ = "list")
print(first)
second_filter = first.find_all('div', class_ = "property") 
#获取每个页面的信息



#li_list=ss.find_all('li')
#print(li_list)
#ss = soup.find('i',class_ = 'wuba-list')
#li_list = ss.find_all('li') #这是拿到了所有的li标签
#print(li_list)
patter = re.compile(r'\s',re.S)
#这是循环每个li标签，这里拿到的每个li标签还是一个beatifulsoup对象，一样拥有find，find_all等方法，对每个li表圈处理拿到每个房源的各种信息，然后写入 excel中
for num in range(len(second_filter)):
    worksheet.write(num,0,label = second_filter[num].find('a',class_="property-ex").text.strip())
    worksheet.write(num,1,label = second_filter[num].find('h3',class_="property-content-title-name").text.strip())
    pl = second_filter[num].find_all('p')[0]
    span_list = pl.find_all('span')
    worksheet.write(num,2,label=patter.sub('',span_list[0].text))
    worksheet.write(num,3,label=patter.sub('',span_list[1].text))
    worksheet.write(num,4,label=patter.sub('',span_list[2].text))
    worksheet.write(num,5,label=patter.sub('',span_list[3].text))
    worksheet.write(num,6,label=patter.sub('',second_filter[num].find('div',class_ = 'property-content-info').text))
    worksheet.write(num,7,label=patter.sub('',second_filter[num].find('div',class_ = 'property-content-info property-content-info-comm').text))
    worksheet.write(num,8,label=second_filter[num].find('p',class_ = 'property-content-info-comm-name').text)
    worksheet.write(num,9,label=second_filter[num].find('p',class_ = 'property-content-info-comm-address').text)
    worksheet.write(num,10,label=patter.sub('',second_filter[num].find_all('div',class_ = 'property-content-info')[2].text))
    worksheet.write(num,11,label=second_filter[num].find('p',class_ = 'property-content-info-text').text)
    worksheet.write(num,12,label=second_filter[num].find('p',class_ = 'property-price-total').text)
    worksheet.write(num,13,label=second_filter[num].find('p',class_ = 'property-price-average').text)
    workbook.save('MyWorksheet2.xlsx')
    

     

    





