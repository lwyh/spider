"""
headers = {
        #'x-devtools-emulate-network-conditions-client-id': "5f2fc4da-c727-43c0-aad4-37fce8e3ff39",
        'upgrade-insecure-requests': "1",
        #'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'dnt': "1",
        'accept-encoding': "gzip, deflate, br, zstd",
        'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        'cookie': "lastCity=101280600; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1712027666; YD00951578218230%3AWM_NI=FRSEwPqVrV14soqUtNhoVpclFiqBCxp9jWlS1CFrg5Hz%2BEMf1w0IT9%2BPEdWntVlMc2%2B8Xh09iMVujBBDjOXmwmenthZQiE5HgVHQmnCVmgQtEQ5KaTG0WSnPX4UZpjRsWnk%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee83f44494b1c099c73f8bb08eb2d15a968b9badc4729c9c9dbae6608ebaafd5f92af0fea7c3b92a868e9da6f65cb38abeb7b440b1b1bfb6f746acb19a91e26886b7bfa3c274b4e7a6b8ef59f39d8a93e63f8ca6e5a6d06ef3a900aad733e9908b85d666b88aa4aee23ae9e89889b333ab939a96e94a829ca6b0db67b5b3ab8ff7649a8fa7a6b844a58a88b2f066818aa388d480878ffbace46085f099b4ed5c9cec9bbbf36292ad998fea37e2a3; YD00951578218230%3AWM_TID=37XMklKZyp1FVQFVQQbQfAcoC%2FdXj5Hp; ab_guid=e585d591-583c-4aa5-aac9-1c35f661a8f4; wt2=D9-l0UZ_t0yyiDu1IgCgzr_Yhdu8Qkyofe42CIBUcMxZOgkjBAXFKk6AgBkZEV2WJVJRNofeP59va4T3pE6U4Pw~~; wbg=0; zp_at=mRYnMAFOHKfD0aWTSxOMbXDeJkkUdZMT7tyi2XewcDw~; __zp_seo_uuid__=9d9f1a0c-864b-4ce0-9ae3-2ab4b4f12e0a; __zp_stoken__=31a7fw5ZUwoAYPxMSXBENwoFSYlJtWcKAwrtswr9Rw4BKc3hMwrrCqcK7wqHCucKqwrnCn1LCqW7Ch2TCscKtworCu8KKwrTDgVbCvcKtwqbCtcKewqjCncShw6vCucaCxIHCocOAwp5GLxMQExEQChEKEBEKEQoQEQ4VDhEQFAcUFhZCMcKzw5c3QUNDL1VOVRVLaFxQXE8OYk1YQTxdCRBaPC5Awr5JQEPDhcKzw4XCiMK%2Bw4DCvwnDhcODwrwLQUhDQMOExIUpNXMPw4HDpg%2FDgMOnFcOAw4IMw4PDgQzDk2Vtw7haw4QnJ0M6w4PEvUBGHj03RDw3REhERi5ELMOTXHbDslrDhBcnQxc8Rjc5OURGNzc3PjI3Oyk2RkAzQwsJDBAMMTfCuU%2FDgMOoRjc%3D; __g=-; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob&s=3&g=&friend_source=0&s=3&friend_source=0; __c=1733194139; __a=78498822.1635231234.1732072477.1733194139.389.21.30.101",
        'cache-control': "no-cache",
        #'postman-token': "76554687-c4df-0c17-7cc0-5bf3845c9831"
    }
"""




# -*- coding: utf-8 -*-
import json
import time
import winsound

import requests
import scrapy

from items import WwwZhipinComItem
import sys
sys.path.append('d:/spider')

class ZhipinSpider(scrapy.Spider):

    handle_httpstatus_list = [302]

    name = 'zhipin'

    allowed_domains = ['www.zhipin.com']

    start_urls = [
        "http://www.zhipin.com/",
    ]

    # positionUrl = 'https://www.zhipin.com/c101050100/?query=python'
    positionUrl = 'https://www.zhipin.com/web/geek/job?query=BI%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101280600'
    # 当前省份的下标
    currentProv = 0
    # 当前页码
    currentPage = 1
    # 当前城市的下标
    currentCity = 0

    cityListUrl = "https://www.zhipin.com/wapi/zpgeek/common/data/city/site.json"

    cityList = []


    
    headers = {
        'Host': "www.zhipin.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        'Accept': "application/json, text/plain, */*",
        'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'X-Requested-With': "XMLHttpRequest",
        'traceId': "F-348b0fxcrkZJFXBi",
        'Connection': "keep-alive",
        'Referer': "https://www.zhipin.com/web/geek/job?query=BI%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101280600",
        'Cookie': "lastCity=101280600; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1712027666; YD00951578218230%3AWM_NI=FRSEwPqVrV14soqUtNhoVpclFiqBCxp9jWlS1CFrg5Hz%2BEMf1w0IT9%2BPEdWntVlMc2%2B8Xh09iMVujBBDjOXmwmenthZQiE5HgVHQmnCVmgQtEQ5KaTG0WSnPX4UZpjRsWnk%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee83f44494b1c099c73f8bb08eb2d15a968b9badc4729c9c9dbae6608ebaafd5f92af0fea7c3b92a868e9da6f65cb38abeb7b440b1b1bfb6f746acb19a91e26886b7bfa3c274b4e7a6b8ef59f39d8a93e63f8ca6e5a6d06ef3a900aad733e9908b85d666b88aa4aee23ae9e89889b333ab939a96e94a829ca6b0db67b5b3ab8ff7649a8fa7a6b844a58a88b2f066818aa388d480878ffbace46085f099b4ed5c9cec9bbbf36292ad998fea37e2a3; YD00951578218230%3AWM_TID=37XMklKZyp1FVQFVQQbQfAcoC%2FdXj5Hp; ab_guid=e585d591-583c-4aa5-aac9-1c35f661a8f4; __zp_seo_uuid__=9d9f1a0c-864b-4ce0-9ae3-2ab4b4f12e0a; __zp_stoken__=7fdbfOjrDn8K5ScK4NyoCAggECDItPTotGDU6LjU%2BMTo6OzwzOjozHj0qbsK6AVZiVMOMLTovOjsxOjo0Oz43Hzo3xLjCvTs7IAbCuwVWY1DDjQlVCBQJWsK6LcOywroJRDAsw7nCuj08MT0FwrnCvMKwBcK5wr3CtXHCucKtwrQ8OUXCtD0lPVYGCFY9PU5MWQtPUk1TUUMPREVALz02Oj7Dl8KtIDkJBAQEBQwICQkIAAQEBAUNCQkJCAQAAAABJjrClsK9ScKdw6zCrsOuxJrCmELCksK2wq7CvcKXwqbCul%2FCo8Kzw79ewrJhwqxSwoVYwpNPwrbCscKZwq%2FCuMK8XMK0wrlFwqhpRsK4SsK3wq5Lwrdiwr1%2BBlNTVQI4AcO6w7rDjA%3D%3D; __g=-; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3DBI%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%26city%3D100010000&s=3&g=&friend_source=0&s=3&friend_source=0; __c=1733194139; __a=78498822.1635231234.1732072477.1733194139.412.21.53.124",
        'Sec-Fetch-Dest': "empty",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Site': "same-origin",
        'TE': "trailers"
    }

    def parse(self, response):

        print(response.status)
        if response.status == 302:
            winsound.MessageBeep()
            # 等待用户输入验证码
            input('please input verify code to continue:')
            # self.crawler.engine.close_spider(self, 'done!' % response.text)
        print("request->" + response.url)
        is_one_page = response.css('div.job-list-wrapper>div.search-job-result').extract()
        is_end = response.css(
            'div.job-list-wrapper>div.search-job-result>a[class*="disabled"]::attr(class)').extract()
        job_list = response.css('div.search-job-result>ul>li')
        for job in job_list:
            # 数据获取
            item = WwwZhipinComItem()
            # job_primary = job.css('div.job-primary')
            item['pid'] = job.css(
                'div.company-info>h3>a::attr(href)').extract_first().split('/gongsi/')[1].split('.html')[0]
            item['positionName'] = job.css(
                'div.job-title::text').extract_first().strip()
            item['salary'] = job.css(
                'div.job-info>span::text').extract_first().strip()

           # info_primary = job.css('div.info-primary>p::text').extract()
            item['city'] = job.css('div.job-area::text').extract_first().strip()
            item['workYear'] = job.css('ul.tag-list>li:nth-child(1)::text').extract_first().strip()
            item['education'] = job.css('ul.tag-list > li:nth-child(2)::text').extract_first().strip()


            item['companyShortName'] = job.css('div.company-info > h3.company-name a::text').get().strip()
            company_info = job.css('div.company-info ul.company-tag-list li::text').extract()
            if len(company_info) == 3:
                item['industryField'] = company_info[0].strip()
                item['financeStage'] = company_info[1].strip()
                item['companySize'] = company_info[2].strip()

           
           
            item['interviewer'] = job.css('div.info-public em::text').extract_first().strip()

            item['updated_at'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
        yield item
        self.currentPage+=1
        time.sleep(5)
        yield self.next_request(0,0)

        

        # 下一页不可点击则表示到底，退出
        # print(len(is_end))
        # print(len(is_one_page))
        if len(is_end) != 0 or len(is_one_page) == 0:
            # self.crawler.engine.close_spider(self, 'done!' % response.text)
            #     todo: 城市id变化，是否变化传入next_request的参数中，预先导入城市列表，然后循环
            self.currentCity += 1
            self.currentPage = 0
            prov_index = self.currentProv
            # 跨省
            # print(len(self.cityList[prov_index]['subLevelModelList']))
            if self.currentCity >= len(self.cityList[prov_index]['subLevelModelList']):
                self.currentProv += 1
                self.currentCity = 0
                self.currentPage = 0

        if self.currentProv == 34:
            self.crawler.engine.close_spider(self, 'done!' % response.text)
        # 翻页
        self.currentPage += 1
        time.sleep(2)
        yield self.next_request(self.currentProv, self.currentCity)

    def start_requests(self):
        # start_requests 只调用一次,初始化时获取city列表
        res = requests.get(self.cityListUrl, headers=self.headers).content
        city = json.loads(res)

        # 调试用
        self.cityList = city['zpData']['siteList']

        return [self.next_request(self.currentProv, self.currentCity)]

    def next_request(self, current_prov, current_city):
        print("current_prov"+str(current_prov))
        print("current_city"+str(current_city))
        cur_city_id = 'c' + \
            str(self.cityList[current_prov]
                ['subLevelModelList'][current_city]['code'])
        print(cur_city_id)
        # 这里url写想要查找什么职业
        return scrapy.http.FormRequest(
            self.positionUrl + cur_city_id + (
                "?query=python&page=%d&ka=page-%d" % (self.currentPage, self.currentPage)),
            headers=self.headers,
            callback=self.parse)



"""
if __name__=="__main__":
    #创建类的实例
    hadler=ZhipinSpider()
    hadler.start_requests()
    hadler.next_request(0,0)
    response = requests.get(url = hadler.positionUrl,headers= hadler.headers)
    print(response.text)
    

"""



