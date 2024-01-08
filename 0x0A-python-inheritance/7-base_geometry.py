#!/usr/bin/python3
"""Module that """
class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        raise an exception
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        validate value
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        