#!/usr/bin/python3
"""Base class"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """list of JSON str representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        json_file = cls.__name__ + ".json"
        obj_list = []
        try:
            with open(json_file, 'r') as f:
                info = f.read()
        except:
            return obj_list

        json_info = Base.from_json_string(info)

        for obj in json_info:
            obj_list.append(cls.create(**obj))

        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Update the class Base by adding the class method"""
        filename = cls.__name__ + ".csv"
        if filename == "Rectangle.csv":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]
        with open(filename, 'w', newline='') as write_file:
            if list_objs is not None:
                writer = csv.DictWriter(write_file, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            elif list_objs is None:
                writer = csv.writer(write_file)
                writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""
        list_objs = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, newline='') as write_file:
                reader = csv.DictReader(write_file)
                for row in reader:
                    new_list = dict((k, int(v)) for k, v in row.items())
                    list_objs.append(new_list)
                return ([cls.create(**obj) for obj in list_objs])

        except Exception:
            return list_objs
