import scrapy                                                                   # on importe la bibliothèque scrapy
from ..items import ScrapbotanysItem                                            # depuis le fichier items.py on importe la classe ScrapbotanysItem


class BotanysSpider(scrapy.Spider):                                             # on crée une classe BotanysSpider qui hérite de la classe scrapy.Spider contenu dans la bibliothèque scrapy

    name = 'botanys'                                                            # on définit le nom de notre spider (le nom du site par exemple ici botanys pour nous)

    allowed_domains = ['www.botanys.fr']                                        # on définit les domaines autorisés pour notre spider, pas obligatoire mais conseillé

    start_urls = ['https://www.botanys.fr/catalogue/fleurs/',
                  'https://www.botanys.fr/catalogue/huile/',
                    ]                                                           # on définit les urls de départ de notre spider          

    def parse(self, response):                                                  # on définit la méthode parse qui va récupérer les infos des produits    
        for product_card in response.css('div.layout-grid-item'):               # on fait une boucle sur tous les produits de la page ayant la classe "layout-grid-item" dans une div

            item = ScrapbotanysItem()                                           # on crée un objet de la classe ScrapbotanysItem que l'on a créee dans le fichier items.py
            item['link']  = product_card.css('a::attr(href)').get()   
            item['image'] = product_card.css('img::attr(src)').get()            # ici on récupère les infos qu'on veut et on les stocke dans l'objet item
            item['price'] = float(product_card.css('bdi::text').get().replace(',','.'))
            item['name']  = product_card.css('a.name-product::text').get()
            yield item                                                          # on retourne l'objet item qui contient les infos du produit yield renvoie les infos qu'on à récupéré


        # next_pages = response.css('nav a::attr(href)').getall()
        # for next_page in next_pages:
        #     if next_page is not None:
        #         print(next_page)
        #         yield response.follow(next_page, self.parse)             

    

            