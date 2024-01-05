#!/usr/bin/python3
""" FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Class for serializing and deserializing instances to/from JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns a dictionary of all objects
        """
        if cls is None:
            return self.__objects
        else:
            cls_objects = {}
            for obj_id, obj in self.__objects.items():
                if isinstance(obj, cls):
                    cls_objects[obj_id] = obj
            return cls_objects

    def new(self, obj):
        """ Adds a new object to the dictionary
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name, obj_id = key.split(".")
                cls = globals()[cls_name]
                self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes an object from __objects if it exists
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
