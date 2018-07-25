#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        '''
            This script will get all the City values

        '''
        listofcities = []

        for city in listofcities:
            if city.state_id == self.id:
                listofcities.append(city)
        return city
