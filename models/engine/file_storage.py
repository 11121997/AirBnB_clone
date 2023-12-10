#!/usr/bin/python3
"""file storage modules"""
import json
from os.path import isfile
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classnames = {
        'User': User,
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }


class FileStorage:
    '''class that serializes instances to
    a JSON file and deserializes JSON file to instances'''

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        '''initialize'''
        return FileStorage.__objects

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as file:  # open
            dic = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(dic, file)  # convert dict to str

    def reload(self):
        '''deserializes the JSON file to __objects'''
        if isfile(self.__file_path):
            try:
                with open(self.__file_path) as file:
                    d_json = json.load(file)  # python dict
                    for key, val in d_json.items():
                        # evaluate the str (cls name) and returns (cls obj)
                        self.__objects[key] = eval(val['__class__'])(**val)
            except Exception:
                pass
