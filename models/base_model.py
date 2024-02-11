#!/usr/bin/python3

import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Unused positional arguments
            **kwargs: Dictionary representation of an instance.

        If kwargs is not empty:
            Each key has an attribute name
            Each value is the value of the corresponding attribute name
            Convert datetime to datetime objects

        Otherwise:
            Create id, created_at, and updated_at values as initially done
        """
        datetime_isoformat = "%Y-%m-%dT%H:%M:%S.%"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in {"created_at", "updated_at"}:
                    setattr(self, key, datetime.datetime.strptime(value, datetime_isoformat))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation of the object class"""
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing key/value
        of __dict__ for an instance
        """
        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

