#!/usr/bin/python3
"""decoding json"""
import json


def from_json_string(my_str):
    """decodes a json var

    Arguments:
        my_str {any} -- analized variable

    Returns:
        [any] -- decoded variable
    """
    return (json.loads(my_str))
