#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from os import getenv
association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship('Amenity', secondary=association_table,
                             viewonly=False)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """
            """
            from models import storage
            my_reviews = []
            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    my_reviews.append(review)
            return my_reviews

        @property
        def amenities(self):
            """
            """
            from models import storage
            amenity_list = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

            @amenities.setter
            def amenities(self, value):
                """
                """
                if type(value) == Amenity:
                    self.amenity_ids.append(value)
