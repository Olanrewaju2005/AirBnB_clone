#!/usr/bin/python3
"""
Module for Base class
Parent class for the airBnb clone project.
"""
import datetime
import uuid


class BaseModel:
    """Class for Base Model"""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Unused positional arguments
            **kwargs: Dictionary representation of an instance.
        """
        datetime_isoformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime(
                        kwargs["created_at"], datetime_isoformat
                    )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime(
                        kwargs["updated_at"], datetime_isoformat
                    )
                else:
                    self.__dict__[key] = kwargs[key]
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
