from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxlhtml import LxmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field

class MyItem(Item):
	url = Field()
	
class exampleSpider(CrawlSpider):
	name = 'example'
	allowed_domains = ['someurl.com']
	start_urls = ['http://www.someurl.com']
	rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)

	def parse_obj(self,response):
		item = MyItem()
		item['url'] = []
		for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
			item['url'].append[link.url]
		return item
