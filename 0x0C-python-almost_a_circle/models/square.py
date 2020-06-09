#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y)
        self.size = size

    def __str__(self):
        """str representation of square"""
        msg = "[Square] ({}) {}/{} - {}".format(self.id,
                                                self.x,
                                                self.y,
                                                self.size)
        return msg
