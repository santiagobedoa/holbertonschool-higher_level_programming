#!/usr/bin/python3
''' Module for Base class '''
import json


class Base:
    ''' Base object '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Constructor '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns JSON string representation '''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes to a file the JSON string representatio '''
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of the JSON string representation '''
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
