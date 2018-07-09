
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sys
sys.path.append('..')

import config

engine = create_engine(config.SQLALCHEMY_DB_URI, echo=config.DEBUG)
Base = declarative_base()

class Voter(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String)
    voted = Column(Boolean)

class Vote(Base):
    id = Column(Integer, primary_key=True)
    vote = Column(Integer)
