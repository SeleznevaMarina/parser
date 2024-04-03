import scrapy
from scrapy_selenium import SeleniumRequest
import numpy as np
import pandas as pd
from scrapy.utils.defer import deferred_to_future

class SmartphoneSpider(scrapy.Spider):

    name = "oper_system"
    info = []
    # allowed_domains = ["www.ozon.ru"]
    # start_urls = ["https://www.ozon.ru/category/smartfony-15502/?sorting=rating"]

    def start_requests(self):
        url = "https://divanboss.ru/divany/"
        yield SeleniumRequest(url=url, callback=self.parse)


    def parse(self,response):
        links = response.css('a[class="product__name t-h4"]')
        
        for link in links:
            data = scrapy.Request(response.urljoin(link.attrib['href']), self.get_info)
            yield scrapy.Request(data, self.save_data)

        # sort_info = info.sort_data
        # print(f'sort_info = {sort_info}')
        # return sort_info
            
    def save_data(self, response):
        filename = response.data.split('\n')
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('saved file %s' % filename)


    def get_info(self, response):
        data = response.xpath('//p[text()="Ткань"]/following-sibling::p[1]/text()')[0]
        # return self.data
        # self.info.append(data)
        # print(f'INFO = {data}')
        

    def sort_data(self, data):
        s = pd.Series(data)
        # .sort_values(ascending=False).head(100)
        