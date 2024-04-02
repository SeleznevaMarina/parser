import scrapy
from scrapy_selenium import SeleniumRequest

class SmartphoneSpider(scrapy.Spider):

    name = "oper_system"
    # allowed_domains = ["www.ozon.ru"]
    # start_urls = ["https://www.ozon.ru/category/smartfony-15502/?sorting=rating"]

    def start_requests(self):
        url = "https://divanboss.ru/divany/"
        yield SeleniumRequest(url=url, callback=self.parse)


    def parse(self,response):
        links = response.css('a[class="product__name t-h4"]')
        
        for link in links:
            info = scrapy.Request(response.urljoin(link.attrib['href']), self.get_info)
            yield info


    def get_info(self, response):
        info = response.xpath('//p[text()="Вес"]/following-sibling::p[1]/text()')[0]
        print(f'info = {str(info)}')