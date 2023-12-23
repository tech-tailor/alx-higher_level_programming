#!/usr/bin/python3
"""
This module adds numbers together
"""


def add_integer(a, b=98):
    """
    function that adds 2 integers
    args:
    a = first arg
    b = second arg

    >>> 5 + 2
    7
    >>> 5 + -3
    2
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
