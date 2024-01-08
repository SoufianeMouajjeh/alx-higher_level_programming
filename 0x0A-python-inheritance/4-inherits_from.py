#!/usr/bin/python3
"""Module that return an object is an instance"""
def inherits_from(obj, a_class):
    """
    if the object is an instance of a class
    that inherited from the specified class
    then return True
    """
    if issubclass(type(obj), a_class):
        return True
    for base in type(obj).__bases__:
        if inherits_from(base, a_class):
            return True
    return False