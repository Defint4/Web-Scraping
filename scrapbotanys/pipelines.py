# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class ScrapbotanysPipeline:
#     def process_item(self, item, spider):
#         return item

import csv
import os
from scrapy.exporters import XmlItemExporter
from scrapy.exporters import CsvItemExporter

class CSVPipeline:

    def __init__(self):
        self.file = open("itemsBotanys.csv", 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    


class XmlPipeline:

    def __init__(self):
        self.file = open("itemsBotanys.xml", 'wb')
        self.exporter = XmlItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item