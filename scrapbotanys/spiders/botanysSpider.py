import scrapy 
from ..items import ScrapbotanysItem


class BotanysSpider(scrapy.Spider):
    name = 'botanys'
    
    allowed_domains = ['www.botanys.fr']
    
    start_urls = ['https://www.botanys.fr/catalogue/fleurs/',
                  'https://botanys.fr/catalogue/huile/']
    
    def parse(self, response):
        for product in response.css('div.layout-grid-item'):
            item = ScrapbotanysItem()  
            item['link'] = product.css('a::attr(href)').get()
            item['image']= product.css('img::attr(src)').get()
            item['price']= product.css('bdi::text').get()+"€"
            item['name'] = product.css('a.name-product::text').get()
            
            yield item
    

            