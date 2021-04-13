# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

import pymongo


class AmazontestPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'mongodb+srv://1980kjheng:kjheng8608@cluster-kj.rr1w6.mongodb.net/amazon?retryWrites=true&w=majority',
            27017
        )
        db = self.conn['amazon']
        self.collection = db['amazon_titles']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
