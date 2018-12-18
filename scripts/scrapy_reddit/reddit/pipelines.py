# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class RedditPipeline(object):
    def process_item(self, item, spider):

        if int(item['score']) > 1000:
            return item
        else:
            raise DropItem("too low score")
