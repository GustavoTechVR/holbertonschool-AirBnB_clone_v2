#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State.
    Attributes:
        name (str): The name of the state.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Getter for cities related to the state (for non-DBStorage).
        Returns:
            list: A list of City objects related to this state.
        """
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == 'City':
                lista.append(var[key])
        for elem in lista:
            if elem.state_id == self.id:
                result.append(elem)
        return result
    
    @property
    def cities(self):
        """Getter for cities related to the state""" 
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city) 
                if city[0] == 'City':
                    lista.append(var[key])
            for elem in lista:
                if elem.state_id == self.id:
                    result.append(elem)
            return result
