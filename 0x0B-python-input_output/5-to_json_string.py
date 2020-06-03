#!/usr/bin/python3
"""json representation
"""
import json


def to_json_string(my_obj):
    """Type to a json representation

    Arguments:
        my_obj {any} -- analyzed object

    Returns:
        [str] -- json representation
    """
    return (json.dumps(my_obj))
