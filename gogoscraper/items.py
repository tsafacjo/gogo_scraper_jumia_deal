# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GogoscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PostItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field() 
    title = scrapy.Field()
    description = scrapy.Field()
    town = scrapy.Field()
    category = scrapy.Field()
    transactionType =  scrapy.Field()
    area=  scrapy.Field()
    publishedDate = scrapy.Field()
    price =  scrapy.Field()
    priceCurency = scrapy.Field()
    phoneNumber = scrapy.Field()
    url = scrapy.Field()

class VehiculescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    seller = scrapy.Field() 
    mark = scrapy.Field()
    model = scrapy.Field()
    town = scrapy.Field()
    category = scrapy.Field()
    transmission =  scrapy.Field()
    carburant=  scrapy.Field()
    annee = scrapy.Field()
    kilometrage = scrapy.Field()
    publishedDate = scrapy.Field()
    transactionType=scrapy.Field()
    price =  scrapy.Field()
    priceCurency = scrapy.Field()
    phoneNumber = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    transmission = scrapy.Field()