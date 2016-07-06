#!/usr/bin/env bash
cd /home/apps/qichacha_spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_crawl_gb2312.log"
echo $path_to_log
scrapy crawl qichacha_spider_gb2312 -s LOG_FILE=$path_to_log &
