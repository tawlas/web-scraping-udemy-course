# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = ["https://www.livecoin.net/en"]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_path = "/Users/lastaw/Documents/projects/scraping/chromedriver"
        driver = webdriver.Chrome(
            executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get("https://www.livecoin.net/en")
        rur_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        rur_tab[4].click()
        self.html = driver.page_source
        driver.close()

    # def start_requests(self):
    #     pass
        # yield SplashRequest(url="http://www.livecoin.net/en", callback=self.parse, endpoint="execute", args={
        #     'lua_source': self.script
        # })

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency_pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume_name': currency.xpath(".//div[2]/span/text()").get()
            }
