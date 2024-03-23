#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.Envar import HBNB_TYPE_STORAGE, DB
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This defines the user attributes"""
    __tablename__ = "users"
    if getenv(HBNB_TYPE_STORAGE) == DB:
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''