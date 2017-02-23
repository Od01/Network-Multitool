import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy import optional_features
optional_features.remove('boto')

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['southcoast.craigslist.org']
    start_urls = [
        'http://southcoast.craigslist.org/search/cta',
    ]

    for url in start_urls:
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(respinse.body)
        self.log('Saved file %s' % filename)

    #def parse(self, response):
        #hxs = HtmlXPathSelector(response)
        #for links in response:
            #hxs.select('//base/@href').extract()
        #return links


            # Look into link extractors here https://doc.scrapy.org/en/latest/topics/link-extractors.html
            # Still need to figure out how to add extracters and parse your stuff