#!/usr/bin/python3
"""Defines a DB Storage Class"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


all_classes = [User, State, City, Amenity, Place, Review]
class DBStorage:
    """DB Storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize class"""

        uri = "{}+{}://{}:{}@{}:3306/{}".format(
            'mysql', 'mysqldb', getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')
        )
        self.__engine = create_engine(uri, pool_pre_ping=True)
        self.reload()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Establish a query session based on cls"""

        table_info = {}
        if cls:
            return self.Get_data(cls, table_info)

        for _class in all_classes:
            table_info = self.Get_data((_class), table_info)


    def new(self, obj):
        """Add instances(obj) to current Database"""

        if obj:
            self.__session.add(obj)

    def save(self):
        """Save/Commit all changes to current Database"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete instances from current Database"""

        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Create table and establish a session"""
        Base.metadata.create_all(self.__engine)
        Session_Sm = sessionmaker(bind=self.__engine,
                                expire_on_commit=False)
        Session_SS = scoped_session(Session_Sm)
        self.__session = Session_SS()
    
    def Get_data(self, cls, D_type):
        """Get data from MySQL Table"""

        if type(D_type) is dict:
            query = self.__session.query(cls)

        for row in query:
            key = "{}.{}".format(cls.__name__, row.id)
            D_type[key] = row

        return D_type

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
