import scrapy
import json


class LaoDongSpider(scrapy.Spider):
    name = 'LaoDong'
    start_urls = ['https://laodong.vn/thoi-su/thu-tuong-tang-cuong-lien-ket-vung-di-dau-trong-phat-trien-kinh-te-so-825152.ldo']
    total_pages = set()


    def parse(self, response):
            data = {
                'Link' :response.url,
                'Title':response.css('h1::text').get(),
                'Tags' :response.css('span.keywords a::text').getall(),
                'Description': response.css('p.abs::text').get(),
                'keywords': [k.strip() for k in response.css('meta[name="keywords"]::attr("content")').get().split(',')],
                'Content': '\n'.join([''.join(c.css('*::text').getall())
                    for c in response.css('div.article-content > p')]),
                }
            f = open('C:/Users/htc/PycharmProjects/Testscarpy/tutorial/tutorial/Output/LaoDong.txt', 'a+', encoding='utf-8')
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
            next_links = response.css('article.article-small.N2 a::attr(href)').getall()
            for link in next_links:
                if len(self.total_pages) <= 200:
                    self.total_pages.add(link)
                    yield scrapy.Request(
                        response.urljoin(link),
                        callback=self.parse
                    )
# Go to /spiders and run in command
# scrapy crawl LaoDong
