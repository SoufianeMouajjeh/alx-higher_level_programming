#!/usr/bin/python3
"""Module that write an Object to a text file"""
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
