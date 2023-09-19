#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City  # Import the City class

class State(BaseModel, Base):
    """ The state class, contains name """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        from models import storage
        city_list = []
        for key, city in storage.all(City).items():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list