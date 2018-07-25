#!/usr/bin/python3
"""
    This is the database storage
"""
import models
from models.base_model import Base
from models import City, State, User, Place, Amenity, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import Column, Integer, String
from os import getenv

objects = [City, State, User, Place, Amenity, Review]


class DBStorage:
    """
        This is the datbase storage where we will create a new engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            Initializing public instance
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Based on cls run a query for current database objects
        """
        dictionary = {}

        if cls:
            for selection in self.__session.query(cls):
                key = str(selection.__class__.__name__) + "." + str(selection.
                                                                    id)
                dictionary[key] = selection

        else:
            for option in objects:
                for var in self.__session.query(option):
                    key = str(var.__class__.__name__) + "." + str(var.id)
                    dictionary[key] = var
        return dictionary

    def new(self, obj):
        """
            This will add an object to the current
            database session

        """
        self.__session.add(obj)

    def save(self):
        """
            This will commit all changes of the current
            database session

        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            This will delete the obj from the current
            database session if not empy
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
            This will create tables in the database
            and apply scope session for thread safety

        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
