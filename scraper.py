import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://mobile.twitter.com/dadtellsjokes',
    ]

    def parse(self, response):
        for tweet in response.css('.tweet-text > .dir-ltr::text').extract():
            yield {
                '' : tweet
            }

        next_page = response.css('div.w-button-more a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
