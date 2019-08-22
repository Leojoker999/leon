import scrapy

from ..items import PythonprojectItem

class NewSpider(scrapy.Spider):
    name = "spider"
    start_urls = ['http://172.18.58.238/freebix']

    def parse(self, response):
        items = PythonprojectItem()

        css_selector = 'img'


        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse)