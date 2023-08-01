#!/usr/bin/python3
# 0-square.py by Ima-obong Akinwumi Olabiyi
""" defines a square based on size  """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size):

        """
        Args:
            size: size of square
        """

        self.__size = size
