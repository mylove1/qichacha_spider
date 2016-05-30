#!/usr/bin/env bash
cd /home/apps/qichacha_spider
sh crontab/crawl_bjda.sh &
sh crontab/crawl_jd.sh &
