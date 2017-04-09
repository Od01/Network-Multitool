from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.spider import BaseSpider

#from run_first import *

# domain = userInput()

class InputSpider(CrawlSpider):
        name = "Input"
        user_input = ""
        allowed_domains = [user_input]
        start_urls = ["http://" + user_input + "/"]

        # allow=() is used to match all links
        rules = [
        Rule(SgmlLinkExtractor(allow=()), follow=True, callback='parse_item')
        ]

        def parse_item(self, response):
            x = HtmlXPathSelector(response)
            filename = "output.txt"
            open(filename, 'ab').write(response.url + "\n")
