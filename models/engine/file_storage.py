#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """

    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """

        """
        obj_clsname = obj.__class__.__name__
	key = "{}.{}".format(obj_clsname, obj.id)
        self.__objects[key] = obj

    def all(self):
        """

        """
        return self.__objects

    def save(self):
        """

        """
        all_objs = self.__objects
        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """

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
