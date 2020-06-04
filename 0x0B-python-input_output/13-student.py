#!/usr/bin/python3
"""Represent a Student"""


class Student:
    """Represent Student class
    """
    def __init__(self, first_name, last_name, age):
        """Constructor
        Arguments:
            first_name {str} -- first_name
            last_name {str} -- last name
            age {int} -- age
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Represent a dictionary
        Keyword Arguments:
            attrs {list} -- keys of dictionary (default: {None})
        Returns:
            [dict] -- sorted dictionary or same dictionary
        """
        if attrs is None:
            return (self.__dict__)

        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        """reload

        Arguments:
            json {json} -- reload
        """
        for k, v in json.items():
            if hasattr(self, k):
                setattr(self, k, v)
