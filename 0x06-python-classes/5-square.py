#!/usr/bin/python3
"""Initialized Square class"""


class Square:
    """Square class with private attribute"""
    def __init__(self, size=0):
        """Initialized Square with size attribute"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculation of square's area"""
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """Size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Prints a square with #"""
        hashTimes = "#" * self.__size
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print(hashTimes)
                