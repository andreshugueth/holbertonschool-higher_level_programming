#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status using request module
"""
import requests


if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
