#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import Place
from models import storage


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    if getenv('HBNB_MYSQL_STORAGE') == 'db':
        email       =   Column(String(128), nullable=False)
        password    =   Column(String(128), nullable=False)
        first_name  =   Column(String(128), nullable=False)
        last_name   =   Column(String(128), nullable=False)
        places    = relationship("Place", back_ref='user', cascade='all, delete-orphan')
        reviews    = relationship("Review", back_ref='user', cascade='all, delete-orphan')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
