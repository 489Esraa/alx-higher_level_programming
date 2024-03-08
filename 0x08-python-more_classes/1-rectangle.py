#!/usr/bin/python3

"""
This module defines an empty class called Rectangle.
"""


class Rectangle:
    """
    This class represents a geometric square.

    Attributes:
    - None
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(self.__width) is int:
            if self.__width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(self.__height) is int:
            if self.__height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
