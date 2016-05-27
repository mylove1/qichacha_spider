# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from qichacha_spider.db.mongo import CompanyInfoItemsDB


class ValidParamsPipeline(object):
    def process_item(self, item, spider):
        if item.get("company_name"):
            return item
        raise DropItem("company_name is null")


class DuplicatesPipeline(object):
    def __init__(self):
        self.ips_seen = set()

    def process_item(self, item, spider):
        if item['company_name'] in self.ips_seen and not item.get('phone'):
            raise DropItem("Duplicate item found: %s" % item['company_name'])
        else:
            self.ips_seen.add(item['company_name'])
            return item


class MongoPipeline(object):
    def process_item(self, item, spider):
        CompanyInfoItemsDB.upsert_company_info_item(dict(item))
        return item
