#!/usr/bin/python3
""" amenities Module for ALX project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity
from models.Envar import HBNB_TYPE_STORAGE, DB
from os import getenv


class Amenity(BaseModel, Base):
     """ the Amenity Class and its attributes"""
     __tablename__ = "amenities"
     if getenv(HBNB_TYPE_STORAGE) == DB:
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity, back_populates='amenities')
    else:
        name = ''