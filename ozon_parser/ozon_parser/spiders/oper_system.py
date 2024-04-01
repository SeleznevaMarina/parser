import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ozon_parser.items import DataItem
# selenium 4
from selenium import webdriver
from scrapy_selenium import SeleniumRequest
# from selenium.webdriver.chrome.service import Service as ChromiumService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType

# options = webdriver.ChromeOptions()
# options.add_argument("--disable-notifications")
# driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
# driver = webdriver.Chrome(chrome_options=options)


# driver.get("https://www.ozon.ru/category/smartfony-15502/?sorting=rating")
# driver.get("https://divanboss.ru/divany/")
# chrome_remote = webdriver.Remote('http://hostname:4444/wd/hub', options.to_capabilities())


class SmartphoneSpider(scrapy.Spider):

    name = "oper_system"
    # allowed_domains = ["www.ozon.ru"]
    # start_urls = ["https://www.ozon.ru/category/smartfony-15502/?sorting=rating"]

    # allowed_domains = ["divanboss"]
    # start_urls = ["https://divanboss.ru/divany/"]

    # rules = (
    #     # Rule(SgmlLinkExtractor(allow=('divany\.php\?.+')), follow=True),
    #     Rule(LinkExtractor(allow='divanboss.ru/divany/'), callback='parse_item'),
        # )
    def start_requests(self):
        url = "https://divanboss.ru/divany/"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self,response):

        for a in response.xpath('//a[@class="u-center fixed-menu-item"]'):
            tkan = a.xpath('text()').get()
            item = {'tkan': tkan}
            yield
            
        print('test_2')
