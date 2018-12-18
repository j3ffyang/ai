# -*- coding: utf-8 -*-
import scrapy

from reddit.items import RedditItem
from scrapy.http.request import Request

class RedditJobSpider(scrapy.Spider):
    name = 'reddit_job'

    # where to extract data
    allowed_domains = ['reddit.com']
    start_urls = ['http://reddit.com/r/funny/']

    def parse(self, response):
        # how to extract data
        # print(response.css('h2.pd8yw6-0::text').extract())
        # print(response.css('a.SQnoC3ObvgnGjWt90zD9Z::attr(href)').extract())
        # print(response.css('div._1rZYMD_4xY3gRcSS3p8ODO::text').extract())
        title = (response.css('h2.pd8yw6-0::text').extract())
        href = (response.css('a.SQnoC3ObvgnGjWt90zD9Z::attr(href)').extract())
        score = (response.css('div._1rZYMD_4xY3gRcSS3p8ODO::text').extract())

        for item in zip(title, href, score):
            new_item = RedditItem()
            new_item['title'] = item[0]
            new_item['href'] = item[1]
            new_item['score'] = item[2]

            yield  new_item
        # pass
