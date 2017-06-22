#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '21/06/2017'
"""

from celery import Celery
from celery import platforms
from config import Config
app = Celery('dispatch.spider', include=['dispatch.task'])
app.config_from_object(Config)
platforms.C_FORCE_ROOT = True