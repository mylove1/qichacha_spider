# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from qichacha_spider.db.mongo import CompanyInfoItemsDB, CompanyInfoItemsGb2312DB
from utils import require_value_from_dict
from items import CompanyInfoItem


class StripParamsPipeline(object):
    def process_item(self, item, spider):
        i = CompanyInfoItem()
        for key in ['province', 'phone', 'email',
                    'company_name', 'registration_number', 'organization_registration_code',
                    'business_status', 'business_type', 'register_date', 'legal_representative',
                    'registered_capital', 'operating_period', 'registration_authority',
                    'date_of_issue', 'business_address', 'business_scope', 'unified_social_credit_code',
                    'english_name', 'item_category', 'item_category_num', 'item_from', 'item_from_gb2312',
                    'item_update_time']:
            i[key] = require_value_from_dict(item, key)
        return i


class ValidParamsPipeline(object):
    def process_item(self, item, spider):
        if item.get("company_name"):
            return item
        raise DropItem("company_name is null")


# class DuplicatesPipeline(object):
#     def __init__(self):
#         self.ips_seen = set()
#
#     def process_item(self, item, spider):
#         if item['company_name'] in self.ips_seen and not item.get('phone'):
#             raise DropItem("Duplicate item found: %s" % item['company_name'])
#         else:
#             self.ips_seen.add(item['company_name'])
#             return item


class MongoPipeline(object):
    def process_item(self, item, spider):
        # CompanyInfoItemsDB.upsert_company_info_item(dict(item))
        CompanyInfoItemsGb2312DB.upsert_company_info_item(dict(item))
        return item
