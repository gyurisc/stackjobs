# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import sys

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.ids_seen = set()
        for job in self.collection.find():
            self.ids_seen.add(job['jobid'])
        
        print "Number of jobs in database"
        print len(self.ids_seen)
        
    def process_item(self, item, spider):
        
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
      
        if valid and item['jobid'] not in self.ids_seen:
            self.collection.insert(dict(item))
            self.ids_seen.add(item['jobid'])            
            log.msg("Job added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        else:
            raise DropItem("Job id {0} already exists!".format(item['jobid']))    
            
        return item        
        
        