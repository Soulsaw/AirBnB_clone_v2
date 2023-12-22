#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            """
            from models import storage
            my_cities = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    my_cities.append(city)
            return my_cities
