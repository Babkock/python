#!/usr/bin/python3
"""
Tanner Babcock
November 12, 2019
Module 12, topic 3: Abstraction
"""
from abc import ABC, abstractmethod

class Rider(ABC):
    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass

class Bicycle(Rider):
    def __init__(self):
        print("Instantiating Bicycle...")

    def ride(self):
        print("Man-powered vehicle two wheels")

    def riders(self):
        print("One rider, not enclosed")

class Motorcycle(Rider):
    def __init__(self):
        print("Instantiating Motorcycle...")

    def ride(self):
        print("Engine powered vehicle two wheels")

    def riders(self):
        print("One or two riders, not enclosed")

class Car(Rider):
    def __init__(self):
        print("Instantiating Car...")

    def ride(self):
        print("Engine powered vehicle four wheels")

    def riders(self):
        print("Up to four riders, enclosed")

if __name__ == "__main__":
    bike = Bicycle()
    bike.ride()
    bike.riders()

    harley = Motorcycle()
    harley.ride()
    harley.riders()

    steelcage = Car()
    steelcage.ride()
    steelcage.riders()

