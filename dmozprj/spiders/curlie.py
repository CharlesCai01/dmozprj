# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dmozprj.items import DmozprjItem

class CurlieSpider(CrawlSpider):
    name = 'curlie'
    allowed_domains = ['curlie.org']
    start_urls = ['https://curlie.org/Arts/']
    rules = (
        Rule(
            LinkExtractor(  # 限定爬取子目录各项中的链接
                restrict_xpaths=('//section[@class="children"]//div[@class="cat-item"]'), 
                allow_domains=('curlie.org')
                ), 
            callback='parse_item', 
            follow=True
            ),
        )

    def parse_item(self, response):
        item = DmozprjItem()
        
        # 爬当前网页所属目录
        category = response.url.lstrip('https://curlie.org')
        item['category'] = category
        
        
        # 爬当前网页中的子目录
        subcategory_list = list()
        for web in response.xpath('//section[@class="children"]//div[@class="cat-item"]'):
            i = {}
            i['category_name'] = web.xpath('a/div/text()').extract()[1].strip()
            i['category_path'] = web.xpath('a/@href').extract_first()
            subcategory_list.append(i)
        item['subcategories'] = subcategory_list

        
        # 爬当前网页中的列出的网页信息
        site_list = list()
        for web in response.xpath('//div[@class="site-item "]/div[3]'):
            i = {}
            i['name'] = web.xpath('a/div/text()').extract_first().strip()
            i['link'] = web.xpath('a/@href').extract_first()
            i['descrip'] = web.xpath('div/text()').extract_first().strip()
            site_list.append(i)
        item['sites'] = site_list
        return item