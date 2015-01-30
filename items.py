# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HkOddsItem(scrapy.Item):
    # define the fields for your item here like:
    # Name = scrapy.Field()
    RaceDate = scrapy.Field()   #used for public index only
    RaceDateTime = scrapy.Field()
    RacecourseCode = scrapy.Field()
    RaceName = scrapy.Field()
    Raceclass = scrapy.Field()
    Raceratingspan = scrapy.Field()
    Prizemoney = scrapy.Field()
    Surface = scrapy.Field()
    RailType = scrapy.Field()
    Distance = scrapy.Field()
    RaceNumber = scrapy.Field()
    HorseNumber = scrapy.Field()
    Last6runs = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    Horsename = scrapy.Field()
    Horsecode = scrapy.Field()
    ActualWt = scrapy.Field()
    Jockeyname = scrapy.Field()
    Jockeycode = scrapy.Field()
    JockeyWtOver = scrapy.Field()
    Draw = scrapy.Field()
    Trainername = scrapy.Field()
    Trainercode = scrapy.Field()
    Rating = scrapy.Field()
    RatingChangeL1 = scrapy.Field()
    DeclarHorseWt = scrapy.Field()
    HorseWtDeclarChange = scrapy.Field()
    # Besttime = scrapy.Field()
    Age = scrapy.Field()
    WFA = scrapy.Field()
    Sex = scrapy.Field()
    SeasonStakes = scrapy.Field()
    Priority = scrapy.Field()
    Gear = scrapy.Field()
    Owner = scrapy.Field()
    SireName = scrapy.Field()
    DamName = scrapy.Field()
    ImportType = scrapy.Field()
    #odds data 
    # Updatetime = scrapy.Field()
    # UpdateDate = scrapy.Field()
    # # Winodds = scrapy.Field()
    # # Placeodds = scrapy.Field()

