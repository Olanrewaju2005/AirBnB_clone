#!/usr/bin/python3

import datetime
import uuid

def BaseModel:
   
    def __init__(self, *args, **kwargs):
        datetime_isoformat = "%Y-%m-%dT%H:%M:%S.%"
        if kwargs:
            for key, value in kwargs:
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, datetime_isoformat)
                else:
                    setattr(self, key, value)
        else:
            self.name = name
            self.my_number = int(my_number)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"

    def save(self):
            updated_at = datetime.date.time.now()

    def to_dict(self):
        self.__dict__['__class__'] = self.__class__.__name__
	self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__.items()
