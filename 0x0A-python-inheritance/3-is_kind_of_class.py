#!/usr/bin/python3
"""Module that return an object is an instance"""
def is_kind_of_class(obj, a_class):
    """
    if the object is exactly an instance
    then return True
    """
    return isinstance(obj, a_class)
