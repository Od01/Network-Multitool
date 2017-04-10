from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.spider import BaseSpider
from scrapy import Request
from scrapy.http import Request
#import request

#from run_first import userInput

#userInput()

class InputSpider(CrawlSpider):
        name = "Input"
        #user_input = ""
        allowed_domains = [user_input]
        #start_urls = ["http://quotes.toscrape.com/"]
        def start_requests(self):
            yield Request(url=self.user_input)

        # allow=() is used to match all links
        rules = [
        Rule(SgmlLinkExtractor(allow=()), follow=True, callback='parse_item')
        ]

        def parse_item(self, response):
            x = HtmlXPathSelector(response)
            filename = "output.txt"
            open(filename, 'ab').write(response.url + "\n")
