# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        data = {
            "email":"2054510095@qq.com",
            "password":"**********"
        }
        request = scrapy.FormRequest(url=url, formdata=data, callback=self.parse_page)
        yield request

    def parse_page(self,response):
        with open("renren.html",'w',encoding='utf-8') as fp:
            fp.write(response.text)

    # def parse_profile(self, response):
    #     pass


