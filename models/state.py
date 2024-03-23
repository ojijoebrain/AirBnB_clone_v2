#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.Envar import HBNB_TYPE_STORAGE, DB
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
     if (getenv(HBNB_TYPE_STORAGE) == DB):
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            '''creates a list of city instances'''
            list_c = []
            d = storage.all()
            for city in d:
                try:
                    if d[city].state_id == self.id:
                        list_c.append(d[city])
                except:
                    pass
            return list_c
