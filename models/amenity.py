#!/usr/bin/python3
""" amenities Module for ALX project """
from models.base_model import BaseModel


class Amenity(BaseModel):
     __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
