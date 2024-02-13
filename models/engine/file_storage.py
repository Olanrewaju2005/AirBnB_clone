#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_clsname = obj.__class__.__name__
	key = "{}.{}".format(obj_clsname, obj.id)
        self.__objects[key] = obj

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        all_objs = self.__objects
        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
        """
        if os.path.isFile(self.__filepath)
            with open(self.__filepath, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key_split('.')

                        cls = eval(class_name)

                        inst = cls(**values)
                        self.__objects[key] = inst

                except Exception:
                    pass
