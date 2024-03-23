#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
from sqlalchemy.ext.declarative import declarative_base



class User(BaseModel, Base):
    """This defines the user attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
    reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')