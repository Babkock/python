#!/usr/bin/python3
"""
Tanner Babcock
November 19, 2019
Module 13, topic 1: GUI and Data Visualization
"""
import tkinter

class NumberGuesser:
    def __init__(self):
        self.guessed_list = []

    def add_guess(self, guess):
        self.guessed_list.append(guess)

if __name__ == "__main__":

