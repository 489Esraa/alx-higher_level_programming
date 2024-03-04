#!/usr/bin/python3
"""
This module defines an empty class called Square.
"""


class Square:
    """
    This class represents a geometric square.

    Attributes:
    - size: private attribute
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("the message size must be >= 0")
        self.__size = size
