import scrapy
import json


class LaoDongSpider(scrapy.Spider):
    name = 'FPT'
    allowed_domains = ['fptshop.com.vn']
    start_urls = ['https://fptshop.com.vn/may-tinh-bang/ipad-pro-129-2020-wi-fi-4g-256gb',
                  'https://fptshop.com.vn/may-tinh-xach-tay/macbook-pro-16-touch-bar-23ghz-core-i9',
                  'https://fptshop.com.vn/dien-thoai/samsung-galaxy-z-flip']
    total_pages = set()

    def parse(self, response):
       # Em định test cho đi các link nhưng code của FPT shop không đồng nhất giữa các trang nên chưa được ạ
       # if response.status == 200 and response.css('body input[type="hidden"]::attr("value")').get() != None :
            data = {
                'Link':response.url,
                'Title':response.css('h1::text').get(),
                'Current Price':response.css('p.fs-dtprice::text,span.fs-gsocit strong::text').get(),
                'Original Price':response.css('p.fs-dtprice del::text').get(),
                'Rate':response.css('div.fs-dtrt-col.fs-dtrt-c1 h5::text').get(),
                'Image':response.css('meta[property="og:image"]::attr("content")').get(),
                'Specifications': response.css('div.fs-tsright label::text').getall(),
                'Description':response.css('div.fs-dtctbox.fsdtcts.clearfix p::text').getall()

            }

            f = open('C:/Users/htc/PycharmProjects/Testscarpy/tutorial/tutorial/Output/FPT.txt', 'a+', encoding='utf-8')
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')

            for href in response.css('div.owl-carousel.fsicte.otherlazy.fsdsamesc a.related_item::attr(href)').getall():
                if len(self.total_pages) <= 200:
                    self.total_pages.add(href)
                    yield response.follow(href, callback=self.parse)
# Go to /spiders and run in command
# scrapy crawl FPT