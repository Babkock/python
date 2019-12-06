#!/usr/bin/python3
"""
Tanner Babcock
GUI Calculator Final Project
"""
import decimal

# Raised when a divide by zero operation is attempted
class CalculatorDivideError(Exception):
    pass

# Raised when input is not of the expected type or range
class CalculatorInputError(Exception):
    pass

# An operation in the Calculator's history
class Operation():
    def __init__(self, op, value):
        if isinstance(op, str) != True:
            raise CalculatorInputError("op argument should be str type")
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise CalculatorInputError("value argument should be an int or float type")
        self.op = op
        self.value = value

    def __str__(self):
        return "{} : {}".format(self.op, self.value)

class Add(Operation):
    def __init__(self, value):
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise CalculatorInputError("value argument should be an int or float type")

        Operation.__init__(self, '+', value)

    def __str__(self):
        return "Add: {}".format(self.value)

class Subtract(Operation):
    def __init__(self, value):
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise CalculatorInputError("value argument should be an int or float type")

        Operation.__init__(self, '-', value)

    def __str__(self):
        return "Subtract: {}".format(self.value)

class Multiply(Operation):
    def __init__(self, value):
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise CalculatorInputError("value argument should be an int or float type")

        Operation.__init__(self, '*', value)

    def __str__(self):
        return "Multiply: {}".format(self.value)

class Divide(Operation):
    def __init__(self, value):
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise CalculatorInputError("value argument should be an int or float type")

        Operation.__init__(self, '/', value)

    def __str__(self):
        return "Divide: {}".format(self.value)

# A Calculator class - has a history and a current buffer, and it keeps track of decimal places
class Calculator:
    def __init__(self, buf=0, fron=1, back=0):
        if (isinstance(buf, float) != True) and (isinstance(buf, int) != True):
            raise CalculatorInputError("Calculator expects a float or int for the first argument")
        if (isinstance(fron, int) != True) or (isinstance(back, int) != True):
            raise CalculatorInputError("Calculator expects an int for the second and third arguments")

        self.current_buffer = buf # The currently displayed value
        self.history = list()     # A list of Operations needed for the current equation
        self.places_front = fron # Decimal places in front of the period
        self.places_back = back  # Decimal places behind the decimal

    def add_operation(self, op):
        if isinstance(op, Operation) != True:
            raise CalculatorInputError("add_operation() expects an Operation type argument")
        self.history.append(op)

    def equals(self):
        try:
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
            err = False

            d = decimal.Decimal(str(self.current_buffer))
            self.places_front = (len(d.as_tuple().digits) + d.as_tuple().exponent)
            if isinstance(self.current_buffer, float):
                self.places_back = (d.as_tuple().exponent * -1)
        except ZeroDivisionError:
            self.buffer_front_back(-1, 1, 0)
            err = True
        finally:
            if err == True:
                raise CalculatorDivideError

    def buffer_front_back(self, buf, fron, back):
        if (isinstance(buf, float) != True) and (isinstance(buf, int) != True):
            raise CalculatorInputError("buffer_front_back() expects a float or int for the buffer argument")
        if (isinstance(fron, int) != True) or (isinstance(back, int) != True):
            raise CalculatorInputError("buffer_front_back() expects an int for front and back arguments")
        self.current_buffer = buf
        self.places_front = fron
        self.places_back = back

    def __str__(self):
        output = ""
        output += "Current buffer: {}\n".format(self.current_buffer)
        for x in self.history:
            print(x)
        output += "\n"
        return output

