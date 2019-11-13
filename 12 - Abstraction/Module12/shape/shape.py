#!/usr/bin/python3
"""
Tanner Babcock
November 12, 2019
Module 12, topic 4: Testing Abstract Classes
"""
from abc import ABC, abstractmethod

class InvalidSideError(Exception):
    pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Area method not implemented")

@Shape.register
class Rectangle():
    def __init__(self, h, b):
        if (isinstance(h, int) != True) and (isinstance(h, float) != True):
            raise ValueError("Height is non-numeric value")
        if h < 0:
            raise InvalidSideError
        if (isinstance(b, int) != True) and (isinstance(b, float) != True):
            raise ValueError("Base is non-numeric value")
        if b < 0:
            raise InvalidSideError

        self._height = h
        self._base = b

    def get_height(self):
        return self._height

    def get_base(self):
        return self._base

    def area(self):
        return self._height * self._base

