#!/usr/bin/python3
"""
Tanner Babcock
GUI Calculator Final Project
"""
import tkinter

class Calculator:
    def __init__(self):
        self.current_buffer = 0.0
        self.history = dict()

    def add_operation(self, op, value):
        if isinstance(op, str) != True:
            raise ValueError
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise ValueError
        self.history.update({ op : value })

    def equals(self):
        if op == '+':
            self.current_buffer += float(value)
        elif op == '-':
            self.current_buffer -= float(value)
        elif op == '*':
            self.current_buffer *= float(value)
        elif op == '/':
            self.current_buffer /= float(value)



if __name__ == "__main__":
    m = tkinter.Tk()
    m.title("Calculator")
    current = tkinter.Label(m, text='0')
    calc = Calculator()
    current.configure(text="{}".format(calc.current_buffer))
    current.grid(row=0, column=1)

    buttons = []

    m.mainloop()

