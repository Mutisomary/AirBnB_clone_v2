#!/usr/bin/python3
""" City Module for HBNB project """
from typing import Any
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel):
    """ The city class, contains state ID and name """
    _tablename = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("state_id"), nullable=False)
