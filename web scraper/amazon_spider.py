import scrapy
from ..items import AmazontestItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011%2Cp_n_feature_browse-bin%3A2656020011&dc&qid=1617118359&rnid=618072011&ref=sr_nr_p_n_feature_browse-bin_2']
    page_number = 2

    # def response_is_ban(self, request, response):    #     return b'banned' in response.body
    #
    # def exception_is_ban(self, request, exception):
    #     return None

    def parse(self, response):
        items = AmazontestItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css(
            '.sg-col-12-of-20 .sg-col-12-of-20 .a-color-secondary .a-size-base:nth-child(2) , .a-letter-space~ .a-link-normal').css(
            '::text').extract()
        product_price_whole = response.css('.a-spacing-top-small .a-price:nth-child(1) span').css('::text').extract()
        product_price_fraction = response.css('.a-spacing-top-small .a-price-fraction').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price_whole'] = product_price_whole
        items['product_price_fraction'] = product_price_fraction
        items['product_imagelink'] = product_imagelink

        yield items

        # next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=' + str(
        #     AmazonSpiderSpider.page_number) + '&qid=1617092202&rnid=1250225011&ref=sr_pg_1'
        # if AmazonSpiderSpider.page_number <= 100:
        #     AmazonSpiderSpider.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)
