#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    # ... [rest of your existing methods] ...

    def do_create(self, args):
        """Create an object of any class with parameters."""
        args_list = args.split(" ")
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if args_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.classes[args_list[0]]()

        for param in args_list[1:]:
            key_value = param.split("=")
            if len(key_value) == 2:
                key, value = key_value
                if value[0] == "\"" and value[-1] == "\"":
                    value = value[1:-1].replace("_", " ").replace("\\\"", "\"")
                elif "." in value:
                    try:
                        value = float(value)
                    except ValueError:
                        continue
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        continue
                setattr(new_instance, key, value)

        new_instance.save()
        print(new_instance.id)
        storage.save()

    # ... [rest of your existing methods] ...

if __name__ == "__main__":
    HBNBCommand().cmdloop()
