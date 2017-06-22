#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '21/06/2017'
"""

import os
from scrapy import cmdline
from celery.task import periodic_task
from celery.schedules import timedelta
from celery.schedules import crontab


@periodic_task(run_every=timedelta(seconds=30))
def quotesbot_spider_scheduler():
    os.system('scrapy crawl author')
    # cmdline.execute("scrapy crawl author".split())
