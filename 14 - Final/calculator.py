#!/usr/bin/python3
"""
Tanner Babcock
GUI Calculator Final Project
"""
import tkinter
import tkinter.font as font

class Operation:
    def __init__(self, op, value):
        if isinstance(op, str) != True:
            raise ValueError
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise ValueError
        self.op = op
        self.value = value

class Calculator:
    def __init__(self):
        self.current_buffer = 0
        self.history = list()
        self.places_front = 1
        self.places_back = 0

    def add_operation(self, op):
        if isinstance(op, Operation) != True:
            raise ValueError
        self.history.append(op)

    def equals(self):
        while len(self.history) > 0:
            if self.history[-1].op == '+':
                self.current_buffer += self.history[-1].value
            elif self.history[-1].op == '-':
                self.current_buffer -= self.history[-1].value
            elif self.history[-1].op == '*':
                self.current_buffer *= self.history[-1].value
            elif self.history[-1].op == '/':
                self.current_buffer /= self.history[-1].value
            del self.history[-1]
        if self.current_buffer >= 10:
            self.places_front += 1
        if self.current_buffer >= 100:
            self.places_front += 1
        if self.current_buffer >= 1000:
            self.places_front += 1
        if isinstance(self.current_buffer, float):
            if (self.current_buffer % 1) != 0:
                self.places_back += 1
            if (self.current_buffer % 0.1) != 0:
                self.places_back += 1
            if (self.current_buffer % 0.01) != 0:
                self.places_back += 1

    def precision(self):
        if self.places_back == 0:
            return 0
        elif self.places_back == 1:
            return 1
        else:
            return self.places_back - 1

