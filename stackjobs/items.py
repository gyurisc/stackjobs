# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class StackjobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    url = Field()
    jobid = Field()
    employer = Field()
    description = Field()    
    location = Field()
    equity = Field()
    salary = Field()
    tags = Field()    
    date = Field()
    weeknum = Field()
    pass

