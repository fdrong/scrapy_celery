#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '21/06/2017'
"""


class Config(object):
    BROKER_URL = 'redis://localhost:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_IGNORE_RESULT = True
