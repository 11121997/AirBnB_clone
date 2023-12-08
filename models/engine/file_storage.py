#!/usr/bin/python3
import json
from os.path import isfile


class FileStorage:
    '''class that serializes instances to
    a JSON file and deserializes JSON file to instances'''
    def __init__(self):
        '''initialize'''
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding='utf-8') as file:  # open
            dic = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(dic, file)  # convert dict to str

    def reload(self):
        '''deserializes the JSON file to __objects'''
        if isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                d_json = json.load(file)  # python dict
                for key, val in d_json.items():
                    # evaluate the str (cls name) and returns (cls obj)
                    self.__objects[key] = eval(val['__class__'])(**val)
