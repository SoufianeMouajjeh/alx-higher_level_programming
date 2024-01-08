#!/usr/bin/python3
"""Module that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        init method to initialize the Rectangle
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """
        area method to calculate the area of the Rectangle
        """
        return self.__width * self.__height
    
    def __str__(self):
        """
        str method to print the rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)