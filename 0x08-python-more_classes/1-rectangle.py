#!/usr/bin/python3
"""
Module: Rectangle module

this module defines a simple class for representing rectangle

classes:
- Rectangle: A class representing rectangle
"""


class Rectangle:
    """
    this is a class called rectangle
    attributes:
    - width

    methods:

    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__value

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        return self.__value

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
