from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.spiders import BaseSpider
from scrapy import Request
from scrapy.http import Request
from scrapy.utils.httpobj import urlparse
#from run_first import *

class InputSpider(CrawlSpider):
        name = "Input"
        #allowed_domains = ["example.com"]

        #def allowed_domains(self):
            #self.allowed_domains = user_input

        #def start_requests(self):
            #yield Request(url=self.user_input)

# Stack Overflow edits
        #def __init__(self, *args, **kwargs):
            #inputs = kwargs.get('urls', '').split(',') or []
            #self.allowed_domains = [urlparse(d).netloc for d in inputs]
            # self.start_urls = [urlparse(c).netloc for c in inputs] # For start_urls
# End Stack Overflow edits

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
