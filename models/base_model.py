#!/usr/bin/python3
'''import necessary modules'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''Main class contain all things to childs classes '''

    def __init__(self, *args, **kwargs):
        '''constructor
        Args:
        - *args: list of arguments (unused)
        - *kwargs: dict of keyword arguments(key-values)
        '''

        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']

        for key, val in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
            setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # add a call to the method new(self) on storage
            models.storage.new(self)

    def save(self):
        '''function to save updates to storage'''
        self.updated_at = datetime.now()
        # call save(self) method of storage
        models.storage.save()

    def to_dict(self):
        ''' returns a dictionary containing all
        keys/values of __dict__ of the instance'''

        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict

    def __str__(self):
        '''Returns the class'''
        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                                      self.id, self.__dict__))
