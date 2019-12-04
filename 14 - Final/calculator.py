#!/usr/bin/python3
"""
Tanner Babcock
GUI Calculator Final Project
"""
import tkinter
import tkinter.font as font
import decimal

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
                if (isinstance(self.current_buffer, float)) or (isinstance(self.history[-1].value, float)):
                    self.current_buffer = float(self.current_buffer) + float(self.history[-1].value)
                else:
                    self.current_buffer += self.history[-1].value
            
            elif self.history[-1].op == '-':
                if (isinstance(self.current_buffer, float)) or (isinstance(self.history[-1].value, float)):
                    self.current_buffer = float(self.history[-1].value) - float(self.current_buffer)
                else:
                    self.current_buffer = self.history[-1].value - self.current_buffer

            elif self.history[-1].op == '*':
                if (isinstance(self.current_buffer, float)) or (isinstance(self.history[-1].value, float)):
                    self.current_buffer = float(self.current_buffer) * float(self.history[-1].value)
                else:
                    self.current_buffer *= self.history[-1].value

            elif self.history[-1].op == '/':
                if (isinstance(self.current_buffer, float)) or (isinstance(self.history[-1].value, float)):
                    self.current_buffer = float(self.history[-1].value) / float(self.current_buffer)
                else:
                    self.current_buffer = self.history[-1].value / self.current_buffer

            del self.history[-1]
        if self.current_buffer >= 1000:
            self.places_front = 4
        elif self.current_buffer >= 100:
            self.places_front = 3
        elif self.current_buffer >= 10:
            self.places_front = 2
        elif self.current_buffer >= 1:
            self.places_front = 1

        #if isinstance(self.current_buffer, float):
        #    d = decimal.Decimal(str(self.current_buffer))
        #    print(d.as_tuple().exponent)
        #    self.places_back = (d.as_tuple().exponent * -1)

    def precision(self):
        if self.places_back == 0:
            return 0
        elif self.places_back == 1:
            return 1
        else:
            return self.places_back - 1

