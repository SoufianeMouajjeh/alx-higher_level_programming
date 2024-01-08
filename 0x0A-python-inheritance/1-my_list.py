#!/usr/bin/python3
"""Module that inherits from a list"""
class MyList(list):
    """Sort the list in ascending order"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
        