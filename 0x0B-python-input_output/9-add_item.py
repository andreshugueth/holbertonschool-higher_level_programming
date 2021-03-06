#!/usr/bin/python3
"""script that adds all arguments to a Python list
and then save them to a file
"""
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_file = load_from_json_file(filename)
except Exception:
    my_file = []

my_file = my_file + sys.argv[1:]
save_to_json_file(my_file, filename)
