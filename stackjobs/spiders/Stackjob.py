# -*- coding: utf-8 -*-
from scrapy import Spider 
from scrapy.selector import Selector
from stackjobs.items import StackjobItem

import datetime 

class StackjobSpider(Spider):
    name = "Stackjob"
    allowed_domains = ["stackoverflow.com"]
    start_urls = (
        'https://stackoverflow.com/jobs?sort=p',
        'https://stackoverflow.com/jobs?sort=p&pg=2',
        'https://stackoverflow.com/jobs?sort=p&pg=3'
    )

    def parse(self, response):
        jobs = Selector(response).xpath('//div[contains(@class, "-item") and contains(@class, "-job")]')
        results = [] 
        
        t = datetime.date.today()
        
        for job in jobs: 
            item = StackjobItem()    
            item['date'] = t.strftime('%Y-%m-%d')                       
            item['tags'] = job.xpath('div[contains(@class,"tags")]/p/a/text()').extract()
            item['description'] = job.xpath('p[contains(@class,"text") and contains(@class, "description")]/text()').extract()[0]
            item['location'] = job.xpath('ul[contains(@class, "metadata") and contains(@class, "primary")]/li[contains(@class, "location")]/text()').extract()[0].strip()
            item['employer'] = job.xpath('ul[contains(@class, "metadata") and contains(@class, "primary")]/li[contains(@class, "employer")]/text()').extract()[0].strip()
            item['jobid'] = job.xpath('@data-jobid').extract()[0]
            item['title'] = job.xpath('div[contains(@class,"-title")]/h1/a/text()').extract()[0]
            item['url'] = job.xpath('div[contains(@class,"-title")]/h1/a/@href').extract()[0]
                        
            if job.xpath('div[contains(@class,"-title")]/span[contains(@class,"salary")]/text()').extract():
                item['salary'] = job.xpath('div[contains(@class,"-title")]/span[contains(@class,"salary")]/text()').extract()[0].strip()

            results.append(item)
            # yield item

        return results 
