# -*- coding: utf-8 -*-

import scrapy


class ProjectItem(scrapy.Item):
    source = scrapy.Field()
    destination = scrapy.Field()
    departurepoint = scrapy.Field()

