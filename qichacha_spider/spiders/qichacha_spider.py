# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..db.mongo import ShellerInfoItemsDB
from ..items import CompanyInfoItem

import random
from ..proxy.proxy_helper import ProxyHelper


class QixinSpider(scrapy.Spider):
    name = "qichacha_spider"

    def start_requests(self):
        sheller_info_items = ShellerInfoItemsDB.get_sheller_info_items()
        proxy_items_http = ProxyHelper.get_proxy_items_qichacha_type_http()
        proxy_len = len(proxy_items_http)
        n = 0
        for item in sheller_info_items:
            url = "http://www.qichacha.com/search?key=%s&index=0" % item['shop_name']
            req = scrapy.Request(
                url,
                # cookies=self.cookie,
                callback=self.parse,
                # dont_filter=True,
                # meta={
                    # 'item': item,
                    # 'date': meta_data['date'],
                    # 'weibo_id': meta_data['weibo_id']
                    # 'cookiejar': 'cookiejar',
                # }
            )
            if proxy_len > 0:
                if n >= proxy_len:
                    proxy_items_http = ProxyHelper.get_proxy_items_qichacha_type_http()
                    proxy_len = len(proxy_items_http)
                    n = 0
                proxy = "http://%s:%d" % (proxy_items_http[n]["ip"], int(proxy_items_http[n]["port"]))
                print proxy
                req.meta['proxy'] = proxy
            yield req
            break

    def parse(self, response):
        search_list = response.xpath('//div[@class="col-md-9"]/section/ul/a')
        # print search_list
        print "headers: ", response.headers
        print "meta: ", response.meta

        for sel in search_list:
            url = sel.xpath(
                './@href').extract_first()
            url = response.urljoin(url)
            print "url: ", url
            c = response.headers['Set-Cookie']
            cookies = {
                c.split(';')[0].split('=')[0]: c.split(';')[0].split('=')[1]
            }
            print "cookies: ", cookies
            print "proxy: ", response.meta["proxy"]
            request = scrapy.Request(
                url,
                cookies=cookies,
                callback=self.parse_company,
                # dont_filter=True,
                meta={
                    # 'cookiejar': response.meta['cookiejar'],
                    'proxy': response.meta['proxy'],
                }

            )
            yield request
            # break

    def parse_company(self, response):
        # print response.body
        companyInfoItem = CompanyInfoItem()

        companyInfoItem['company_name'] = response.xpath(
            '//div[@class="company-card"]/h2/text()').extract_first()
        # companyInfoItem['status'] = response.xpath(
        #     '//div[@class="company-card"]/div[@class="company-info-item clearfix"][1]/div[@class="company-info-item-text"]/span/text()').extract_first()
        companyInfoItem['phone'] = response.xpath(
            '//div[@class="company-card"]/div[@class="company-info-item clearfix"][2]/div[@class="company-info-item-text"]/text()').extract_first()
        companyInfoItem['url'] = response.xpath(
            '//div[@class="company-card"]/div[@class="company-info-item clearfix"][3]/div[@class="company-info-item-text"]/a/@href').extract_first()
        # companyInfoItem['address'] = response.xpath(
        #     '//div[@class="company-card"]/div[@class="company-info-item clearfix"][4]/div[@class="company-info-item-text"]/span/text()').extract_first()

        companyInfoItem['unified_social_credit_code'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[1]/td[2]/text()').extract_first()
        companyInfoItem['organization_registration_code'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[1]/td[4]/text()').extract_first()

        companyInfoItem['registration_number'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[2]/td[2]/text()').extract_first()
        companyInfoItem['business_status'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[2]/td[4]/text()').extract_first()

        companyInfoItem['business_type'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[3]/td[2]/text()').extract_first()
        companyInfoItem['register_date'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[3]/td[4]/text()').extract_first()

        companyInfoItem['legal_representative'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[4]/td[2]/a/text()').extract_first()
        companyInfoItem['operating_period'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[4]/td[4]/text()').extract_first()

        companyInfoItem['registered_capital'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[5]/td[2]/text()').extract_first()
        companyInfoItem['date_of_issue'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[5]/td[4]/text()').extract_first()

        companyInfoItem['registration_authority'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[6]/td[2]/text()').extract_first()

        companyInfoItem['business_address'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[7]/td[2]/text()').extract_first()

        companyInfoItem['business_scope'] = response.xpath(
            '//div[@id="info"]/div[1]/div[1]/div[1]/table[1]/tr[8]/td[2]/text()').extract_first()

        print companyInfoItem
        yield companyInfoItem
