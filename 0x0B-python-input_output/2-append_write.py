#!/usr/bin/python3
"""Module that append a text in file"""
def append_write(filename="", text=""):
    """Append a string in text file and return number of char"""
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
    return len(text)
