# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyInfoItem(scrapy.Item):
    company_name = scrapy.Field()  # 公司名称
    phone = scrapy.Field()  # 电话
    url = scrapy.Field()  # 官网

    unified_social_credit_code = scrapy.Field()  # 统一社会信用代码
    organization_registration_code = scrapy.Field()  # 组织机构代码

    registration_number = scrapy.Field()  # 注册号
    business_status = scrapy.Field()  # 经营状态

    business_type = scrapy.Field()  # 公司类型
    register_date = scrapy.Field()  # 成立日期

    legal_representative = scrapy.Field()  # 法定代表人
    operating_period = scrapy.Field()  # 营业期限

    registered_capital = scrapy.Field()  # 注册资本
    date_of_issue = scrapy.Field()  # 发照日期

    registration_authority = scrapy.Field()  # 登记机关

    business_address = scrapy.Field()  # 企业地址

    business_scope = scrapy.Field()  # 经营范围

    pass
