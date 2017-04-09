from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.spider import BaseSpider

class hsleidenSpider(CrawlSpider):
        name = "hsleiden1"
        allowed_domains = ["quotes.toscrape.com"]
        start_urls = ["http://quotes.toscrape.com/"]

        # allow=() is used to match all links
        rules = [
        Rule(SgmlLinkExtractor(allow=()), follow=True, callback='parse_item')
        #Rule(SgmlLinkExtractor(allow=()), callback='parse_item'), # Added this to first rule
        ]

        def parse_item(self, response):
            x = HtmlXPathSelector(response)
            filename = "hsleiden-output.txt"
            open(filename, 'w').write(response.url + "\n")
            #file = open(filename, "w")
            #for resp in x:
                #file.write(resp.url + "\n")

                # got from http://stackoverflow.com/questions/13740825/trying-to-crawl-all-links-of-a-webpage-with-scrapy-but-i-cannot-output-the-link
