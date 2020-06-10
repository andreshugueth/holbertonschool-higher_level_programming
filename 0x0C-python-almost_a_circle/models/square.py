#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """str representation of square"""
        msg = "[Square] ({}) {}/{} - {}".format(self.id,
                                                self.x,
                                                self.y,
                                                self.size)
        return msg

    def update(self, *args, **kwargs):
        """update function"""
        if len(args):
            for element, value in enumerate(args):
                if element == 0:
                    self.id = value
                if element == 1:
                    self.size = value
                if element == 2:
                    self.x = value
                if element == 3:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Dictionary representation of square"""
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["size"] = self.size
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        return new_dict
