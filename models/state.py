#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.city import City

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_ref='state', cascade='all, delete-orphan')
    else:
        name = ""

    @property
    def cities(self):
        """returns the list of City instances with 
        state_id equals to the current State.id"""

        citinst = []
        for _id, city in models.storage.all(City).items():
            if city.state_id == self.id:
                citinst.append(city)
            
        return citinst
