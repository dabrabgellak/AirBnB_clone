#!/usr/bin/python3
""" Module Base """


from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    pass
                else:                
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Print str """
        name_c = __class__.__name__
        return("[{}] ({}) {}".format(name_c, self.id, self.__dict__))

    def save(self):
        """
        save - Updates the public instance
        with the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing
        all keys/values of __dict__ """
        new_dict = self.__dict__.copy()

        new_dict.update({"created_at": self.created_at.isoformat()})
        new_dict.update({"updated_at": self.updated_at.isoformat()})
        new_dict.update({"__class__": __class__.__name__})
        return new_dict