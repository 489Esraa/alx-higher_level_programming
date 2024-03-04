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

    def __init__(self, size = 0):
      """
      the size attribute that define
      must be integer 
      must be > 0
      else raise error
      """
      self.__size = size
      if not isinstance(size, int):
          raise TypeError("size must be an integer")
      if __size < 0:
          raise ValueError("the message size must be >= 0")
      else:
          self.__size = size