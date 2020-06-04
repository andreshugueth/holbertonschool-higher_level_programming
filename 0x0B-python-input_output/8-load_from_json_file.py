#!/usr/bin/python3
"""load from json"""
import json


def load_from_json_file(filename):
    """decodes json to obj

    Arguments:
        filename {json} -- name of the file

    Returns:
        [any] -- original object
    """
    with open(filename) as f:
        return (json.load(f))
