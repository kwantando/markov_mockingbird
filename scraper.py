import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://mobile.twitter.com/dadtellsjokes',
    ]

    def parse(self, response):
        for tweet in response.css('div.tweet-text'):
            yield {
                'text': tweet.css('div.dir-ltr').extract_first()
            }

        next_page = response.css('div.w-button-more a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
