#!/usr/bin/python3
"""model that holede Basemodel class"""
import uuid
from datetime import datetime


class BaseModel:
    """base model class"""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for class BaseModel
        Args:
            id - identification number
            *args - arguments (not used)
            **kwargs - dictionary arguments
        """

        if kwargs and kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v,
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, v)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a formated strining format string of clasname, id
        created_at and updated_at
        """

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def seve(self):
        """save new information add in BassModel class"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """ eturns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.name
        d['updated_at'] = self.updated_at.isoformat()
        d['created_at'] = self.created_at.isoformat()
        return d
