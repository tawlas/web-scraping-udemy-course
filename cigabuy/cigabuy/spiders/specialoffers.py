# -*- coding: utf-8 -*-
import scrapy


class SpecialoffersSpider(scrapy.Spider):
    name = 'specialoffers'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/specials.html']

    def start_requests(self):
        yield scrapy.Request(url="https://www.cigabuy.com/specials.html", headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
        })

    def parse(self, response):
        products = response.xpath("//ul[@class='productlisting-ul']/div")
        for product in products:
            yield {
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discounted_price': product.xpath(".//div[@class='p_box_price cf']/span[@class='productSpecialPrice fl']/text()").get(),
                'original_price': product.xpath(".//div[@class='p_box_price cf']/span[@class='normalprice fl']/text()").get(),
                'user_agent': response.request.headers['User-Agent']
            }
        next_page = response.xpath("//a[@class='nextPage']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
            })
