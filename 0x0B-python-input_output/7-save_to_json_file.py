#!/usr/bin/python3
"""write an object using json"""
import json


def save_to_json_file(my_obj, filename):
    """save using json representation

    Arguments:
        my_obj {any} -- object
        filename {str} -- name of the file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
