# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_id=scrapy.Field()
    name=scrapy.Field()
    score=scrapy.Field()
    image_url=scrapy.Field()
    type=scrapy.Field()
    main_actor=scrapy.Field()
    release_time=scrapy.Field()
