# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..db.mongo import ShellerInfoItemsDB
from ..items import CompanyInfoItem


class QichachaSpider(scrapy.Spider):
    name = "qichacha_spider"

    def start_requests(self):
        sheller_info_items = ShellerInfoItemsDB.get_sheller_info_items()

        for item in sheller_info_items:
            url = "http://www.qichacha.com/search?key=%s&index=0" % item['shop_name']
            request = scrapy.Request(
                url,
                callback=self.parse
            )
            yield request
            break

    def parse(self, response):
        search_list = response.xpath('//ul[@class="list-group list-group-lg no-bg auto"]/a')

        for sel in search_list:
            companyInfoItem = CompanyInfoItem()
            url = sel.xpath('./@href').extract_first()
            companyInfoItem['province'] = sel.xpath(
                './span[@class="clear"]/span[@class="btn btn-link pull-right"]/text()').extract_first()
            companyInfoItem['phone'] = sel.xpath('./span[@class="clear"]/small[2]/span[1]/text()').extract_first()
            companyInfoItem['email'] = sel.xpath('./span[@class="clear"]/small[2]/span[2]/text()').extract_first()
            url = response.urljoin(url)
            print "url: ", url
            request = scrapy.Request(
                url,
                callback=self.parse_company
            )
            request.meta['item'] = companyInfoItem
            yield request
            # break

    def parse_company(self, response):
        # print response.body
        companyInfoItem = response.meta['item']

        companyInfoItem['company_name'] = response.xpath('//span[@class="text-big font-bold"]/text()').extract_first()
        # companyInfoItem['status'] = response.xpath('//span[@class="label  label-success m-l-xs"]/text()').extract_first()
        companyInfoItem['registration_number'] = response.xpath(
            '//ul[@class="company-base"]/li[1]/text()').extract_first()
        companyInfoItem['organization_registration_code'] = response.xpath(
            '//ul[@class="company-base"]/li[2]/text()').extract_first()
        companyInfoItem['business_status'] = response.xpath('//ul[@class="company-base"]/li[3]/text()').extract_first()
        companyInfoItem['business_type'] = response.xpath('//ul[@class="company-base"]/li[4]/text()').extract_first()
        companyInfoItem['register_date'] = response.xpath('//ul[@class="company-base"]/li[5]/text()').extract_first()
        companyInfoItem['legal_representative'] = response.xpath(
            '//ul[@class="company-base"]/li[6]/a/text()').extract_first()
        companyInfoItem['registered_capital'] = response.xpath(
            '//ul[@class="company-base"]/li[7]/text()').extract_first()
        companyInfoItem['operating_period'] = response.xpath('//ul[@class="company-base"]/li[8]/text()').extract_first()
        companyInfoItem['registration_authority'] = response.xpath(
            '//ul[@class="company-base"]/li[9]/text()').extract_first()
        companyInfoItem['date_of_issue'] = response.xpath('//ul[@class="company-base"]/li[10]/text()').extract_first()
        companyInfoItem['business_address'] = response.xpath(
            '//ul[@class="company-base"]/li[11]/text()').extract_first()
        companyInfoItem['business_scope'] = response.xpath('//ul[@class="company-base"]/li[12]/text()').extract_first()

        print companyInfoItem
        yield companyInfoItem
