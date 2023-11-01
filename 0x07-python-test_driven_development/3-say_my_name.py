#!/usr/bin/python3
"""
Documentation for function that prints My name is <first name> <last name>.

Example:
    $ python3
    >>> say_my_name = __import__('3-say_my_name').say_my_name
    say_my_name("John", "Smith")
    My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>.

    Args:
        first_name (string): the first name
        last_name (string): the last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
