#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from models.Envar import HBNB_TYPE_STORAGE, DB


if getenv("HBNB_TYPE_STORAGE") == DB:
    storage = DBStorage()
else:
    storage = FileStorage()

classes = {'User': User, 'BaseModel': BaseModel,
           'Place': Place, 'State': State, 'City': City,
           'Amenity': Amenity, 'Review': Review}

storage.reload()
