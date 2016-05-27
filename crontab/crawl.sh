#!/usr/bin/env bash
cd /home/apps/qichacha_spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_crawl.log"
echo $path_to_log
scrapy crawl qichacha_spider -s LOG_FILE=$path_to_log &
