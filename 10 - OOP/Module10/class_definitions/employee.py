#!/usr/bin/python3
"""
Tanner Babcock
October 29, 2019
Module 10, topic 1: Encapsulation
"""
import datetime

class Employee:
    # Constructor
    def __init__(self, fname, lname, address, phone, salaried, start, sal):
        if (isinstance(lname, str) != True):
            raise ValueError
        if (isinstance(fname, str) != True):
            raise ValueError
        if (isinstance(address, str) != True):
            raise ValueError
        if (isinstance(phone, str) != True):
            raise ValueError
        if (isinstance(salaried, bool) != True):
            raise ValueError
        if (isinstance(start, datetime.datetime) != True) and (isinstance(start, datetime.date) != True):
            raise ValueError

        self._last_name = lname
        self._first_name = fname
        self._address = address
        self._phone = phone
        self._salaried = salaried
        self._start_date = start
        self._salary = sal

    def set_last_name(self, lname):
        if (isinstance(lname, str) != True):
            raise ValueError
        self._last_name = lname

    def set_first_name(self, fname):
        if (isinstance(fname, str) != True):
            raise ValueError
        self._first_name = fname

    def set_address(self, addr):
        if (isinstance(addr, str) != True):
            raise ValueError
        self._address = addr

    def set_phone(self, phone):
        if (isinstance(phone, str) != True):
            raise ValueError
        self._phone = phone

    def display(self):
        output = str(self._first_name) + " " + str(self._last_name) + "\n"
        output += self._address + "\n"
        if self._salaried == True:
            output += "Salaried employee: ${}/year\n".format(self._salary)
        else:
            output += "Hourly employee: ${0:.2f}/hour\n".format(self._salary)
        output += "Start date: " + str(self._start_date) + "\n"
        return output

# Driver
address = "1 Infinite Loop\nCupertino, CA"
# call the constructor
emp = Employee("Steve", "Jobs", address, "212-222-2222", True, datetime.datetime.strptime("10-1-1985", "%m-%d-%Y"), 1000000)

print(emp.display())    # display() returns a str
del emp

