#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import storage
from amenity import Amenity, place_amenity

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    if getenv('HBNB_MYSQL_STORAGE') == 'db':
        city_id     =   Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id       =   Column(String(60), ForeignKey('users.id'), nullable=False)
        name            =   Column(String(128), nullable=False)
        description       =   Column(String(1024), nullable=False)
        number_rooms        =   Column(Integer, nullable=False, Default=0)
        number_bathrooms    =   Column(Integer, nullable=False, Default=0)
        max_guest           =   Column(Integer, nullable=False, Default=0)
        price_by_night      =   Column(Integer, nullable=False, Default=0)
        latitude            =   Column(Float, nullable=False)
        longitude           =   Column(Float, nullable=False)
        reviews             = relationship("Place", back_ref='user', 
                                                    cascade='all, delete-orphan')
        amenities           = relationship('Amenity', secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []


    @property
    def reviews(self):
        """" """

        R_list = []
        for _id, place in storage.all(Place).items():
            if place.user_id == self.id:
                R_list.append(place)

        return R_list

    @property
    def amenities(self):
        """Get and Set linked Amenities.
        """

        amenity_list = []

        for amenity in storage.all(Amenity).values():
            if amenity.id in self.amenity_ids:
                amenity_list.append(amenity)

        return amenity_list

    @amenities.setter
    def amenities(self, value):
        """Adding an Amenity.id to the amenity_ids
        """

        if type(value) == Amenity:
            self.amenity_ids.append(value.id)