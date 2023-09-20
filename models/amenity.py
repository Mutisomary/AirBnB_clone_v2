#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)
        extend_existing=True
    )

class Amenity(BaseModel, Base):
    """ Amenity class to store amenity information """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        places = relationship("Place", secondary=place_amenity, viewonly=False)
