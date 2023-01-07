#!/usr/bin/python3
"""This module instantiates an object"""
from models.engine.file_storage import FileStorage
from engine.db_storage import DBStorage
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

if getenv('HBNB_MYSQL_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
