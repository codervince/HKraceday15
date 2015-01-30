from sqlalchemy import create_engine, Column, Integer, Float, String, Time, Date, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
import settings
from sqlalchemy import *


# ModelBase = declarative_base()

Base = declarative_base()
engine = create_engine(URL(**settings.DATABASE))
metadata = MetaData(bind=engine)

class HKRace(Base):
    __table__ = Table('hk_race', metadata, autoload=True)

class HKRunner(Base):
    __table__ = Table('hk_runner', metadata, autoload=True)

class Horse(Base):
    __table__ = Table('horse', metadata, autoload=True)

class Jockey(Base):
    __table__ = Table('jockey', metadata, autoload=True)

class Gear(Base):
    __table__ = Table('hk_gear', metadata, autoload=True)

class Owner(Base):
    __table__ = Table('owner', metadata, autoload=True)

class Trainer(Base):
    __table__ = Table('trainer', metadata, autoload=True)

class RailType(Base):
    __table__ = Table('hk_railtype', metadata, autoload=True)    

class RaceClass(Base):
    __table__ = Table('hk_raceclass', metadata, autoload=True) 

class Distance(Base):
    __table__ = Table('hk_distance', metadata, autoload=True)

class Going(Base):
    __table__ = Table('hk_going', metadata, autoload=True)     

class Odds(Base):
    __table__ = Table('hk_odds', metadata, autoload=True)  

# class Horse(ModelBase):
#     __tablename__ = "horse"
#     __tableargs__ = ( CheckConstraint('Homecountry in ("HKG", "SIN", "AUS", "NZL", "RSA". "ENG", "IRE", "DUB", "IRE", "SCO", "MAC")'))
#     id = Column(Integer, primary_key=True)
#     Code = Column(String(6), nullable=False, unique=True)
#     Name = Column(String(255), nullable=False)
#     Homecountry = Column('Homecountry', String(3), nullable=False)
#     Sex = Column(String(2))
#     Importtype = Column(String(10))
#     Sirename = Column(String(255))
#     Damname = Column(String(255))
#     Damsirename = Column(String(255))
#     UniqueConstraint('Name', 'Code', 'Homecountry', name='Horsecodehomecountry_uidx')

# class Owner(ModelBase):
#     __tablename__ = "owner"
#     __tableargs__ = ( CheckConstraint('Homecountry in ("HKG", "SIN", "AUS", "NZL", "RSA". "ENG", "IRE", "DUB", "IRE", "SCO", "MAC")'))
#     id = Column(Integer, primary_key=True)
#     Name = Column(String(255), unique=True)
#     Homecountry = Column('Homecountry', String(3), nullable=False)
#     UniqueConstraint('Name', name='Ownername_uidx')

# class Jockey(ModelBase):
#     __tablename__ = "jockey"
#     __tableargs__ = ( CheckConstraint('Homecountry in ("HKG", "SIN", "AUS", "NZL", "RSA". "ENG", "IRE", "DUB", "IRE", "SCO", "MAC")'))
#     id = Column(Integer, primary_key=True)
#     Name = Column(String(100), unique=True)
#     Code = Column(String(10))
#     Homecountry = Column('Homecountry', String(3), nullable=False)
#     UniqueConstraint('name', name='JockeyName_uidx')

# class Trainer(ModelBase):
#     __tablename__ = "trainer"
#     __tableargs__ = ( CheckConstraint('Homecountry in ("HKG", "SIN", "AUS", "NZL", "RSA". "ENG", "IRE", "DUB", "IRE", "SCO", "MAC")'))
#     id = Column(Integer, primary_key=True)
#     Name = Column(String(255), unique=True)
#     Code = Column(String(10))
#     Homecountry = Column('Homecountry', String(3), nullable=False)
#     UniqueConstraint('Name', name='Trainername_uidx')

# class Gear(ModelBase):
#     __tablename__ = "gear"
#     id = Column(Integer, primary_key=True)
#     Name = Column(String(255), unique=True)
#     UniqueConstraint('Name', name='Gearname_uidx')

# class HKTrackType(ModelBase):
# 	__tablename__= "hk_tracktype"
# 	id = Column(Integer, primary_key=True)
# 	Name = Column(String(256))
# 	UniqueConstraint('Name', name='HKTrackType_Name_uidx')


# class HKRaceClass(ModelBase):
# 	__tablename__= "hk_raceclass"
# 	id = Column(Integer, primary_key=True)
# 	Name = Column(String(256))
# 	UniqueConstraint('Name', name='HKRaceClass_Name_uidx')

# class HKDistance(ModelBase):
# 	__tablename__= "hk_distance"
# 	id = Column(Integer, primary_key=True)
# 	Name = Column(String(256))
# 	# ImperialName = Column(Float) #convert meters to 
# 	UniqueConstraint('Name', name='HKDistance_Name_uidx')


# 	@hybrid_property
# 	def ImperialName(self):
# 		return int(self.Name)/1600.0

# 	@hybrid_property
# 	def imperialstr(self):
# 		miles = self.Name/1600
# 		furls = (self.Name%1600)/0.125
# 		return str(miles) + ' ' + str(furls)
    
# class HKRace(ModelBase):
# 	__tablename__ = "hk_race"
# 	__tableargs__ = ( 
# 	 	CheckConstraint('Racecoursecode in ("HV", "ST")'),
#         CheckConstraint('Surface in ("Turf", "AWT")')
# 	 	)
# 	id = Column(Integer, primary_key=True)
# 	Racecoursecode = Column('Racecoursecode', String, nullable=False)
# 	Racedatetime = Column('Racedate', Date, nullable=False)
# 	Racename = Column('Racename', String(256))
# 	Racenumber = Column('Racenumber', String, nullable=False)
# 	Surface = Column('Surface', String)
# 	Raceratingspan = Column('Raceratingspan', String)
# 	Raceclassid = Column(Integer, ForeignKey("hk_raceclass.id"))
# 	Distanceid = Column(Integer, ForeignKey("hk_distance.id"))
# 	Tracktypeid = Column(Integer, ForeignKey("hk_tracktype.id"))
# 	Incidentreport = Column('Incidentreport', String(400))
# 	Raceindex = Column('Raceindex', String)

# 	UniqueConstraint('Racecoursecode','Racedatetime', 'Racenumber', name='HKRace_RacecourseDateNumber_uidx') 
# #TODO FIx this table in db!
# class HKRunner(ModelBase):
#     __tablename__ = "hk_runner"
#     id = Column(Integer, primary_key=True)

#     Raceid = Column(Integer, ForeignKey("hk_race.id"))
#     Horseid = Column(Integer, ForeignKey("horse.id"))
#     Jockeyid =Column(Integer, ForeignKey("jockey.id"))
#     Trainerid =Column(Integer, ForeignKey("trainer.id"))
#     Gearid =Column(Integer, ForeignKey("gear.id"))
#     Ownerid = Column(Integer, ForeignKey("owner.id"))

#     Horseno= Column('Horseno', String, nullable=False)
#     Last6runs = Column(String(25))
#     Jockeywt= Column('Jockeywt', Float, nullable=False)
#     Jockeywtover = Column('Jockeywtover', Float)
#     Draw = Column(Integer,nullable=False)
#     Rating = Column(Integer,nullable=False)
#     RatingChangeL1 = Column(Float)
#     Horsewtdeclaration = Column(Integer)
#     Horsewtdeclarationchange = Column(Integer)
#     Besttime = Column(Time)    
#     WFA = Column(Float)
#     Seasonstakes = Column(Integer)
#     Priority = Column(String(5))
#     Age = Column(Integer)    
#     LBW= Column('LBW', String)
#     ##SECTIONALS
#     RunningPosition= Column('RunningPosition', String)
#     Sec1DBL = Column('Sec1DBL', String)
#     Sec2DBL = Column('Sec2DBL', String)
#     Sec3DBL = Column('Sec3DBL', String)
#     Sec4DBL = Column('Sec4DBL', String)
#     Sec5DBL = Column('Sec5DBL', String)
#     Sec6DBL = Column('Sec6DBL', String)
#     FinishTime= Column('FinishTime', Time)
#     Sec1Time = Column('Sec1Time', Time)
#     Sec2Time = Column('Sec2Time', Time)
#     Sec3Time = Column('Sec3Time', Time)
#     Sec4Time = Column('Sec4Time', Time)
#     Sec5Time = Column('Sec5Time', Time)
#     Sec6Time = Column('Sec6Time', Time)
#     WinOdds= Column('WinOdds', Float)
#     HorseReport = Column('HorseReport', String, nullable=True)
#     UniqueConstraint('Raceid', 'Horseno', 'Horseid', name='HKRunner_raceidhorsenohorseid_uidx')


# class HKRacePool(ModelBase):
# 	__tablename__ = "hk_racepool"
# 	id = Column(Integer, primary_key=True)
# 	Updatedate = Column(Date, nullable=False)
# 	Updatetime = Column(Time, nullable=False)           
# 	Winpool = Column(Integer)
# 	Plapool = Column(Integer)
# 	Qinpool = Column(Integer)
# 	Dblpool = Column(Integer)
# 	Tcepool = Column(Integer)
# 	Tripool = Column(Integer)
# 	FFpool = Column(Integer)
# 	Raceid = Column(Integer, ForeignKey("hk_race.id")) 
# 	UniqueConstraint('Raceid', 'Updatedate', 'Updatetime', name='HKRacepool_RaceidUpdateDateTime_uidx')

# class HKOdds(ModelBase):
#     __tablename__ = "hk_odds"
#     id = Column(Integer, primary_key=True)
#     Horsenumber = Column(Integer, nullable=False)
#     Updatedate = Column(Date, nullable=False)
#     Updatetime = Column(Time, nullable=False)
#     Winodds = Column(Float)
#     Placeodds = Column(Float)
#     Raceid = Column(Integer, ForeignKey("hk_race.id"))
#     # Horseid = Column(Integer, ForeignKey("horse.id"))
#     UniqueConstraint('Raceid', 'HorseNumber', 'UpdateDate', 'UpdateTime', name='HKOdds_RaceidHorseNoUpdateDateTime_uidx')


# def get_engine():
#     return create_engine(URL(**settings.DATABASE))


# def create_schema(engine):
#     ModelBase.metadata.create_all(engine)
