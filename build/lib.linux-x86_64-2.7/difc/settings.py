# -*- coding: utf-8 -*-

# Scrapy settings for difc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'difc'

SPIDER_MODULES = ['difc.spiders']
NEWSPIDER_MODULE = 'difc.spiders'

# Kafka server information
KAFKA_HOSTS = 'kafka:9092'
KAFKA_TOPIC_PREFIX = 'dev'

# Store scraped item in redis for post-processing.
ITEM_PIPELINES = {
    'difc.pipelines.KafkaPipeline': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'difc.middlewares.ProxyMiddleware': 100,
}

LOG_LEVEL = 'INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'difc (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
