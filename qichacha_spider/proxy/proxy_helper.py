# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from qichacha_spider.db.mongo import ProxyItemsQichachaDB


class ProxyHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items_type_http():
        try:
            proxy_items = ProxyItemsQichachaDB.get_proxy_items()
            print "proxy_items_http.count:=", proxy_items.count()
            http = [h for h in proxy_items if h["type"].lower().find("http") > -1]
            print "Http: ", len(http)
            return http
        except Exception, e:
            print e.message
            return []

    @staticmethod
    def get_proxy_items_type_https():
        try:
            proxy_items = ProxyItemsQichachaDB.get_proxy_items()
            print "proxy_items_https.count:=", proxy_items.count()
            https = [h for h in proxy_items if h["type"].lower().find("https") > -1]
            print "Https: ", len(https)
            return https
        except Exception, e:
            print e.message
            return []
