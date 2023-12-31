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

        if size < 0:
            raise ValueError("size must be >= 0")

        self._size = size
        
    def area(self):
        return (self._size *self._size)
