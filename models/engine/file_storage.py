#!/usr/bin/python3
"""Este archivo crea una clase FileStorage para el AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """Esta clase serializa instancias a un archivo JSON y
   deserializa un archivo JSON a instancias
   Atributos:
       __file_path: ruta al archivo JSON
       __objects: objetos que se almacenarán
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """retorna un dict
        Return:
            retorna un dict of __object
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """sets __object obj
        Args:
            obj: objeto dado
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializa la ruta del archivo a la ruta del archivo JSON
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serializa la ruta del archivo a la ruta del archivo JSON
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ borra el elemento existente
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ llama reload()
        """
        self.reload()