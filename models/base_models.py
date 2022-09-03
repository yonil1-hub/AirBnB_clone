#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """base class for all class"""

    def __init__(self, id, *args, **kwargs):
        """ initilizes attribute for class
        Args
        id : unique identifier
        created_at: datetime object
        uppdated_at: date time object
        """
        if kwargs and kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(k, datetime.strptime(v, "%y-%m-%dT%H:%M:%s.%f"))
                elif k == '__class__':
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a formated string of classname, id, and dictionary
        contens
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def seve(self):
        """saves instances"""

        self.updated_at = datetime.now()

    def to_dict(self):

        """a dictionary containing all
        keys/values of __dict__ of the instance
        """

        d = self.__dict__.copy()
        d['__class__'] = self.__class__.name
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
