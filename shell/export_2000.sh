#!/usr/bin/env bash

mongoexport --type=csv -f _id,company_name,phone,item_category,item_category_num -d qichacha -c company_info_items -q '{"item_from": "jd", "phone": {"$ne": null}, "province": "北京"}' -o jd.csv