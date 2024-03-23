#!/usr/bin/python3
""" new database """
from sqlalchemy import create_engine, MetaData
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.city import City
from models.user import User
from models.base_model import Base
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import Envar as EV



class DBStorage:
    """ creates db"""
    __engine = None
    __session = None

    def __init__(self):
        """class initialization"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == EV.TEST:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        returns a dictionary
        """
        dic = {}
        if cls != '':
            objs = self.__session.query(models.classes[cls]).all()
            for obj in objs:
                key = f'{obj.__class__.__name__}.{obj.id}'
                dic[key] = obj
            return dic
        else:
            for k, v in models.classes.items():
                if k != 'BaseModel':
                    objs = self.__session.query(v).all()
                    if len(objs):
                        for obj in objs:
                            key = f'{obj.__class__.__name__}.{obj.id}'
                            dic[key] = obj
            return dic


    def new(self, obj):
        """
        adds a new element to the table
        """
        self.__session.add(obj)

    def save(self):
        """
        save changes to the table
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete an element from the table
        """
        if obj:
            self.session.delete(obj)
        return

    def reload(self):
        """
        configures the db
        """
        self.__session = Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s)
        self.__session = Session()

    def close(self):
        """ 
        calls the remove method
        """
        self.__session.close()