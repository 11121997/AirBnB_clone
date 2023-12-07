!/usr/bin/python3
import json

class FileStorage:
    ''''''
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding='utf-8') as file: #open
            dic = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(dic, file) #convert dict to str

    def reload(self):
        pass
