from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.spiders import BaseSpider
from scrapy import Request
from scrapy.http import Request
from scrapy.utils.httpobj import urlparse

class InputSpider(CrawlSpider):
        name = "Input"

        def __init__(self, url=None, *args, **kwargs):
            super(InputSpider, self).__init__(*args, **kwargs)
            self.allowed_domains = [url]
            self.start_urls = ["http://" + url]

        rules = [
        Rule(SgmlLinkExtractor(allow=()), follow=True, callback='parse_item')
        ]

        def parse_item(self, response):
            x = HtmlXPathSelector(response)
            filename = "output.txt"
            open(filename, 'ab').write(response.url + "\n")

print "Crawling site..."
print "See crawler/output.txt for links"
