#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file"""
        jsonfile = cls.__name__ + ".json"
        var = []
        if list_objs is not None:
            for obj in list_objs:
                var.append(cls.to_dictionary(obj))
        with open(jsonfile, 'w') as f:
            f.write(cls.to_json_string(var))