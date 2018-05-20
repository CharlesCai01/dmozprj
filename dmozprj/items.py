# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozprjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field() # 当前网页的所属目录（即URL去掉根域名）
    subcategories = scrapy.Field() # 当前网页包括的子目录（每个目录项的名称和相对路径）
    sites = scrapy.Field() # 当前网页收藏的网页（每个网页项的标题、链接、摘要）