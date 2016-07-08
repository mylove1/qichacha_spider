# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo

from qichacha_spider.settings import MONGO_URI, MONGO_PROXY_DB, MONGO_JD_DB, MONGO_QICHACHA_DB, MONGO_BJDA_DB, \
    MONGO_NEEQ_DB, MONGO_QICHACHA_GB2312_DB

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]
jd_db = mongo_client[MONGO_JD_DB]
qichacha_db = mongo_client[MONGO_QICHACHA_DB]
qichacha_gb2312_db = mongo_client[MONGO_QICHACHA_GB2312_DB]
bjda_db = mongo_client[MONGO_BJDA_DB]
neeq_db = mongo_client[MONGO_NEEQ_DB]

class ProxyItemsQichachaDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        # print "get_proxy_items"
        return proxy_db.proxy_items_qichacha.find({}, {'_id': 0}).batch_size(50)


class ShellerInfoItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_sheller_info_items():
        return jd_db.sheller_info_items.find().batch_size(50)


class CompanyInfoItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company_info_item(item):
        qichacha_db.company_info_items.update(
            {'company_name': item['company_name']},
            {'$set': item}, True, True)


class CompanyInfoItemsGb2312DB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company_info_item(item):
        # print item
        qichacha_gb2312_db.company_info_items.update(
            {'company_name': item['company_name']},
            {'$set': item}, True, True)


class BjdaItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company_info_item(item):
        bjda_db.company_info_items.update({
            'company_name': item['company_name']
        }, {"$set": item}, True, True)

    @staticmethod
    def get_company_info_items():
        return bjda_db.company_info_items.find().batch_size(50)
        # return bjda_db.company_info_items.find().batch_size(50).skip(skip).limit(limit)

    @staticmethod
    def upsert_company_info_item_clean(item):
        bjda_db.company_info_items_clean.update({
            'company_name': item['company_name']
        }, {"$set": item}, True, True)


class NeeqItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_neeq_items():
        return neeq_db.neeq_items.find().batch_size(50)
