# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class ScrapbotanysPipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.exporters import CsvItemExporter    

class botanysPipeline(object):

    def __init__(self):     
        self.file = open("itemsBotanys.csv", 'wb')
        self.exporter = CsvItemExporter(self.file)   
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def validate_item(self, name, price, link, image):

        if not isinstance(name, str):
            raise ValueError("Nom invalide")
        
        if not isinstance(price, float):
            raise ValueError("Prix invalide")

        if not isinstance(link, str):
            raise ValueError("Lien invalide")

        if not isinstance(image, str):
            raise ValueError("Image invalide")

        return name , price , link , image

    def process_item(self, item, spider):
        item['name'],item['price'],item['link'],item['image'] = self.validate_item(item['name'],item['price'],item['link'],item['image'])
        self.exporter.export_item(item)
        return item