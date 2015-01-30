# -*- coding: utf-8 -*-

# Scrapy settings for hkodds project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os
from os.path import join, abspath, dirname

BASE_DIR = dirname(dirname(abspath(__file__)))
IMAGES_STORE = join(BASE_DIR, '..')


BOT_NAME = 'hkodds'

SPIDER_MODULES = ['hkodds.spiders']
NEWSPIDER_MODULE = 'hkodds.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hkodds (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    "hkodds.pipelines.SQLAlchemyPipeline": 10,
    # 'scrapy.contrib.pipeline.images.ImagesPipeline': 20
}  

DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'vmac',
            'password': '',
            'database': 'hkraces10'}

USER_AGENT = "Googlebot/2.1 ( http://www.google.com/bot.html)" 

# WEBSERVICE_PORT = 6092


         