# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            # absolute_link = f"https://www.worldometers.info{link}"
            # absolute_link = response.urljoin(link)
            # yield {'country_name': name, 'country_link': link}
            yield response.follow(url=link, callback=self.parse_country, meta={"country_name": name})
        # yield response.follow(url="https://www.worldometers.info/world-population/china-population/", callback=self.parse_country, meta={"country_name": "China"})

    def parse_country(self, response):
        # logging.info(response.status)
        # inspect_response(response, self)
        name = response.request.meta["country_name"]
        rows = response.xpath(
            "(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath("./td[1]/text()").get()
            population = row.xpath("./td[2]/strong/text()").get()
            yield {'year': year, 'population': population, 'country_name': name}
