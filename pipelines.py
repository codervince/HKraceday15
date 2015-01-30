# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from collections import defaultdict
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker, exc, create_session
from sqlalchemy import *
from hkodds.models import *
from textxml import *


class HkoddsPipeline(object):
    def process_item(self, item, spider):
        return item


# class MyImagesPipeline(ImagesPipeline):


#     def set_filename(self, response):
#         return 'full/{0}.jpg'.format(response.meta['url'][0])

#     def get_images(self, response, request, info):
#         for key, image, buf in super(MyImagesPipeline, self).get_images(response, request, info):
#             key = self.set_filename(response)
#         yield key, image, buf


#     def get_media_requests(self, item, info):
#         for image_url in item['image_urls']:
#             yield scrapy.Request(image_url)

#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['image_paths'] = image_paths
#         return item

class SQLAlchemyPipeline(object):

    def __init__(self):

        # global t_races
        # global t_HKrunners

        # meta.Session.configure(bind=engine)
        # meta.engine = engine

        # t_races = sqlalchemy.Table('hk_race', autoload=True, autoload_with=engine)
        # t_HKrunners = sqlalchemy.Table('hk_runner', autoload=True, autoload_with=engine)
        # orm.mapper(HKRace, t_races)
        # orm.mapper(HKRunner, t_HKrunners)

        # meta.Session.configure(bind=engine)
        # meta.engine = engine


        # class HKRace:
        #     pass

        # class HKRunner:
        #     pass    
        # engine = get_engine()
        # create_schema(engine)
        
        #get data from textxml
     

        #what tables exist?
        # meta = MetaData()
        # meta.reflect(bind=engine)
        # if meta.tables['horse']:
        #load existing tables if any
        # horses = Table('horse', meta, autload=True, autoload_with=engine)

        # Base = declarative_base()
 
        engine = create_engine(URL(**settings.DATABASE))

      




                # engine = create_engine(URL(**settings.DATABASE))

        # self.Session = sessionmaker(bind=engine)
        # self.cache = defaultdict(lambda: defaultdict(lambda: None))
        # metadata = MetaData(bind=engine)


        self.Session = sessionmaker(bind=engine)
        self.cache = defaultdict(lambda: defaultdict(lambda: None))

        session = create_session(bind=engine)
        
        testlist = session.query(HKRace).all()     
        for test in testlist:  
            print test.RaceDate


        #TODO: get horsecolors!
    def process_item(self, item, spider):
        session = self.Session()

        #todo - what about oddsddata from XML parser?
        #first update Race
        runners = HKRunner(
                    # HorseColors

                    Raceid=self.get_id(session, HKRace, "PublicRaceIndex", {
                                "Name" : item["RaceName"],
                                "PublicRaceIndex": item["RacecourseCode"] + item["RaceDate"].strftime("%Y%m%d") + item["RaceNumber"],
                                "RaceDateTime": item["RaceDateTime"],
                                "RacecourseCode": item["RacecourseCode"],
                                "RaceNumber": item["RaceNumber"],
                                "Surface": item["Surface"],
                                "Prizemoney": item["Prizemoney"],
                                "Raceratingspan": item["Raceratingspan"],
                                 "Raceclassid": self.get_id(session, RaceClass, "Name", {"Name": item.get("Raceclass", None)}),
                                "Railtypeid": self.get_id(session, RailType, "Name", {"Name": item.get("Railtype", None)}),
                                                                                    # "Goingid": self.get_id(session, Going, "Name", {"Name": item.get("Going", None)}),
                                "Distanceid": self.get_id(session, Distance, "MetricName", {"MetricName": int(item.get("Distance", 0)     ),
                                                                                    "Miles": float(float(item.get("Distance", 0)    )/1600.0),
                                                                                    "Furlongs": int(int(item.get("Distance", 0))/200)

                                    }), #end distance

                        }),

				    HorseNumber= item['HorseNumber'],
				    Last6runs = item["Last6runs"],
				    ActualWt= item["ActualWt"],
				    JockeyWtOver = item["JockeyWtOver"] if item["JockeyWtOver"] != u'' else None,
				    Draw = item["Draw"],
				    Rating = item["Rating"],
				    RatingChangeL1 = int(item["RatingChangeL1"]),
				    DeclarHorseWt = item["DeclarHorseWt"] if item["DeclarHorseWt"] != u'' else None,
				    HorseWtDeclarChange = item["HorseWtDeclarChange"] if item["HorseWtDeclarChange"] != '-' else None,
                    HorseWtpc = float(item["ActualWt"])/float(item["DeclarHorseWt"]) if item["DeclarHorseWt"] else None,
				    # Besttime = item["Besttime"],
				    WFA = item["WFA"] if item["WFA"] != '-' else None,
				    SeasonStakes = item["SeasonStakes"],
				    Priority = item["Priority"],
				    # Age= item["Age"],

				    Horseid = self.get_id(session, Horse, "Name", {
				        	"Name": item["Horsename"],
				        	"Code": item["Horsecode"],
				        	"SireName": item["SireName"],
				        	"DamName": item["DamName"],
				        	"ImportType": item["ImportType"],
				        	"Sex": item["Sex"],
				        	"Homecountry": 'HKG'
				        	}),

				    Jockeyid = self.get_id(session, Jockey, "Name", {
				    	"Name": item["Jockeyname"],
				    	"Code": item["Jockeycode"],
				    	"Homecountry": 'HKG'
				    	}),
				 
				 	Trainerid = self.get_id(session, Trainer, "Name", {
				 		"Name": item["Trainername"],
				 		"Code": item["Trainercode"],
				 		"Homecountry": 'HKG'
				 		}),

				    # Raceid = self.get_id(session, HKRace, "Name", {
        #                 "PublicRaceIndex": item["RacecourseCode"] + item["RaceDate"].strftime("%Y%M%d") + item["RaceNumber"],
				    # 	"Name": item["RaceName"],
        #                 "RaceDate": item["RaceDate"],
				    # 	"RaceDateTime": item["RaceDateTime"],
				    # 	"RaceNumber": item["RaceNumber"],
				    # 	"RacecourseCode": item["RacecourseCode"]
				    # 	}),

				    
				    Gearid = self.get_id(session, Gear, "Name", {"Name": item["Gear"]}),
				    Ownerid = self.get_id(session, Owner, "Name", {
				    	"Name": item["Owner"],
				    	"Homecountry": 'HKG'
				    	}),
        	)
        #need 1 race 
        # races = HKRace(	
        						
        # 						Name=item["RaceName"],
        #                         PublicRaceIndex = item["RacecourseCode"] + item["RaceDate"].strftime("%Y%M%d") + item["RaceNumber"],
        #                         RaceDate = item["RaceDate"],
        #                         RaceDateTime=item["RaceDateTime"],
        #                         RacecourseCode=item["RacecourseCode"],
        #                         RaceNumber = item["RaceNumber"],
        #                         Surface = item["Surface"],
        # 						Raceratingspan = item["Raceratingspan"],	
        #                         Railtypeid=self.get_id(session, RailType, "Name", {"Name": item["RailType"]}),
        #                         # Goingid=self.get_id(session, Going, "Name", {"Name": item["Going"]}),
        #                         Raceclassid=self.get_id(session, RaceClass, "Name", {"Name": item["Raceclass"]}),	
        #                         Distanceid=self.get_id(session, Distance, "MetricName", {"MetricName": item["Distance"]})
        #                         )

        try:
            # session.add(races)
            session.add(runners)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

    def get_id(self, session, model, unique, fields):
        fval = fields[unique]
        id = self.cache[model][fval]
        if id is None:
            try:
                id = session.query(model).filter(getattr(model, unique) == fval).one().id
            except exc.NoResultFound:
                item = model(**fields)
                session.add(item)
                session.flush()
                session.refresh(item)
                id = item.id
            self.cache[model][fval] = id
        return id