#!/usr/bin/python3
class Square:
    """
    A class that define a square

    Attributes:
    it has a size attribut
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = size

        if size < 0:
            raise ValueError("size must be >= 0")
