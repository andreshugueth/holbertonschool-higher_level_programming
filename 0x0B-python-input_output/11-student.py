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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance

        Returns:
            [dict] -- dictionary representation
        """
        return (self.__dict__)
