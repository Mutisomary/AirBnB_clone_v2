#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """ The state class, contains name """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def city_list(self):
        """Property that returns a list of City objects associated with this State."""
        city_list = []
        from models import storage  # Import locally to avoid circular import
        for key, city in storage.all('City').items():  # Use the class name as a string
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
