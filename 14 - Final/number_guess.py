#!/usr/bin/python3
"""
Tanner Babcock
November 19, 2019
Module 13, topic 1: GUI and Data Visualization
"""
import tkinter
import random

class NumberGuesser:
    def __init__(self):
        self.guessed_list = []
        self.the_number = random.randint(1,8)

    def add_guess(self, guess):
        self.guessed_list.append(guess)

    def is_winner(self):
        if self.guessed_list[-1] == self.the_number:
            return True
        else:
            return False

def button_press(which):
    guesser.add_guess(which)
    if guesser.is_winner():
        label.config(text="You win!")
    else:
        label.config(text="That's not the number")

if __name__ == "__main__":
    m = tkinter.Tk()
    m.title("Guess The Number")
    guesser = NumberGuesser()
    label = tkinter.Label(m, text="Guess a Number!")
    label.grid(row=0)

    button1 = tkinter.Button(m, text="1", width=5, command = lambda: button_press(1)).grid(row=1, column=0)
    button2 = tkinter.Button(m, text="2", width=5, command = lambda: button_press(2)).grid(row=1, column=1)
    button3 = tkinter.Button(m, text="3", width=5, command = lambda: button_press(3)).grid(row=1, column=2)
    button4 = tkinter.Button(m, text="4", width=5, command = lambda: button_press(4)).grid(row=1, column=3)

    button5 = tkinter.Button(m, text="5", width=5, command = lambda: button_press(5)).grid(row=2, column=0)
    button6 = tkinter.Button(m, text="6", width=5, command = lambda: button_press(6)).grid(row=2, column=1)
    button7 = tkinter.Button(m, text="7", width=5, command = lambda: button_press(7)).grid(row=2, column=2)
    button8 = tkinter.Button(m, text="8", width=5, command = lambda: button_press(8)).grid(row=2, column=3)

    exit_button = tkinter.Button(m, text="Exit", width=20, command=m.destroy).grid(row=3, column=1)

    m.mainloop()

