#!/usr/bin/python3
"""Module that import an ractagle"""

Rectangle = __import__('9-base_geometry').Rectangle

class Square(Rectangle):

    def __init__(self, size):
        """
        init method to initialize the Square
        """
        self.integer_validator("size", size)
        self.__size = 0
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area method to calculate the area of the Square
        """
        return self.__size ** 2
    