#!/usr/bin/python3
"""
Tanner Babcock
GUI Calculator Final Project
"""
import decimal

# An operation in the Calculator's history
class Operation():
    def __init__(self, op, value):
        if isinstance(op, str) != True:
            raise ValueError("op argument should be str type")
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise ValueError("value argument should be an int or float type")
        self.op = op
        self.value = value

class Add(Operation):
    def __init__(self, value):
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise ValueError("value argument should be an int or float type")

        Operation.__init__(self, '+', value)

class Subtract(Operation):
    def __init__(self, value):
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise ValueError("value argument should be an int or float type")

        Operation.__init__(self, '-', value)

class Multiply(Operation):
    def __init__(self, value):
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise ValueError("value argument should be an int or float type")

        Operation.__init__(self, '*', value)

class Divide(Operation):
    def __init__(self, value):
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise ValueError("value argument should be an int or float type")

        Operation.__init__(self, '/', value)

# A Calculator class - has a history and a current buffer, and it keeps track of decimal places
class Calculator:
    def __init__(self):
        self.current_buffer = 0 # The currently displayed value
        self.history = list()   # A list of Operations needed for the current equation
        self.places_front = 1   # Decimal places in front of the period
        self.places_back = 0    # Decimal places behind the decimal

    def add_operation(self, op):
        if isinstance(op, Operation) != True:
            raise ValueError("add_operation() expects an Operation type argument")
        self.history.append(op)

    def equals(self):
        while len(self.history) > 0:
            # Here is where we actually do the math. self.history is a list of Operations, op and value pairs.
            # Using this we can compute complex operations like (1 + 2 + 3 = 6) and (1 + 3 * 3 = 10)
            # In each loop iteration, I access the last element of the history, then
            # compute it using its operation, with the currently displayed number
            # as its operand
            if self.history[-1].op == '+':
                if (isinstance(self.current_buffer, float)) or (isinstance(self.history[-1].value, float)):
                    self.current_buffer = float(self.current_buffer) + float(self.history[-1].value)
                else:
                    self.current_buffer += self.history[-1].value
            
            # Assume float conversion if either of the operands are floats,
            # otherwise they will turn out as ints
            # plus:
            # current_buffer = current_buffer + history[-1].value, or
            # current_buffer += history[-1].value
            #
            # minus:
            # current_buffer = history[-1].value - current_buffer
            #
            # times:
            # current_buffer = current_buffer * history[-1].value, or
            # current_buffer *= history[-1].value
            #
            # divide:
            # current_buffer = history[-1].value / current_buffer

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
        
        d = decimal.Decimal(str(self.current_buffer))
        self.places_front = (len(d.as_tuple().digits) + d.as_tuple().exponent)
        if isinstance(self.current_buffer, float):
            self.places_back = (d.as_tuple().exponent * -1)

