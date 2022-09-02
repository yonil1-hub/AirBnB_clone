#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """base class for all class"""

    def __init__(self, id, created_at, updated_at):
        """ initilizes attribute for class
        Args
        id : unique identifier
        created_at: datetime object
        uppdated_at: date time object
        """

        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
