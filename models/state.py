#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel


class State(BaseModel):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    name = Column((String(128)), nullable=False)
    cities = relationship("City", backref="state", cascade="all,
                          delete-orphan")

    @property
    def cities(self):
        '''
            This script will get all the City values

        '''
        listofcities = models.storage.all("City").values()

        for city in listofcities:
            if city.state_id == self.id:
                return city
