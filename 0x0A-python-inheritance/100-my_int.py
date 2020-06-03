#!/usr/bin/python3
"""Represent a inheritance of int"""


class MyInt(int):
    """Represent MyInt class"""
    def __init__(self, value):
        """Constructor

        Arguments:
            value {int} -- value of number
        """
        self.value = value

    def __eq__(self, number):
        """Represent a == b

        Arguments:
            number {int} -- number

        Returns:
            [bool] -- False
        """
        return self.value != number

    def __ne__(self, number):
        """Represent a != b

        Arguments:
            number {int} -- number

        Returns:
            [bool] -- True
        """
        return self. value == number
