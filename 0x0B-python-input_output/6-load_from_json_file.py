#!/usr/bin/python3
"""Module create an Object from a JSON file"""
import json

def load_from_json_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)