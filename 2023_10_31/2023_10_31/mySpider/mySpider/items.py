# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 番剧名称
    name = scrapy.Field()
    # 播放开始时间
    start_time = scrapy.Field()
    #可观看渠道
    channel = scrapy.Field()
