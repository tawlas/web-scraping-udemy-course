# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.net/en']
    script = """
    function main(splash, args)
        splash.private_mode_enabled = false
        --[[headers = {
            ['User-Agent'] = "watson"
        }
        splash:set_custom_headers(headers)]]--
        splash:on_request(function(request)
            request:set_header("User-Agent", "watson")
            end)
        --splash:set_user_agent("alou")
        assert(splash:go(args.url))
        assert(splash:wait(1))
        rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
        rur_tab[5]:mouse_click()
        assert(splash:wait(3))
        --[[
        btn = assert(splash:select("#search_button_homepage"))
        btn:mouse_click()
        ]]--
        splash:set_viewport_full()
        return splash:html()
    end
    """

    def start_requests(self):
        yield SplashRequest(url="http://www.livecoin.net/en", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })

    def parse(self, response):
        for currency in response.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency_pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume_name': currency.xpath(".//div[2]/span/text()").get()
            }
