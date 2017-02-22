import scrapy
from scrapy.linkextractors import LinkExtractor

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'Links': quote.css('span.text::text').extract_first(),
                'Selectors':
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


            # Look into link extractors here https://doc.scrapy.org/en/latest/topics/link-extractors.html