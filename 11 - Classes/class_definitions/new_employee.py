#!/usr/bin/python3
"""
Tanner Babcock
November 6, 2019
Module 11, topic 4: Inheritance and Polymorphism
"""
import datetime

class Employee:
    # Constructor
    def __init__(self, fname, lname, address, phone):
        if (isinstance(lname, str) != True):
            raise ValueError
        if (isinstance(fname, str) != True):
            raise ValueError
        if (isinstance(address, str) != True):
            raise ValueError
        if (isinstance(phone, str) != True):
            raise ValueError

        self._last_name = lname
        self._first_name = fname
        self._address = address
        self._phone = phone

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

        return output

class SalariedEmployee(Employee):
    # Constructor
    def __init__(self, fname, lname, addr, phone, start, salary):
        super().__init__(fname, lname, addr, phone)
        if (isinstance(start, datetime.datetime) != True) and (isinstance(start, datetime.date) != True):
            raise ValueError
        if (isinstance(salary, int) != True):
            raise ValueError("The salary field for this class expects an integer type")

        self._start_date = start
        self._salary = salary

    def give_raise(self, newsalary):
        if (isinstance(newsalary, int) != True):
            raise ValueError("The salary field for this class expects an integer type")
        self._salary = newsalary

    def display(self):
        output = str(self._first_name) + " " + str(self._last_name) + "\n"
        output += self._address + "\n"
        
        output += "Salaried employee: ${}/year\n".format(self._salary)
        output += "Start date: " + str(self._start_date) + "\n"
        return output

class HourlyEmployee(Employee):
    # Constructor
    def __init__(self, fname, lname, addr, phone, start, hourly):
        super().__init__(fname, lname, addr, phone)
        if (isinstance(start, datetime.datetime) != True) and (isinstance(start, datetime.date) != True):
            raise ValueError
        if (isinstance(hourly, float) != True):
            raise ValueError("The hourly_pay field for this class expects a float type")
        
        self._start_date = start
        self._hourly_pay = hourly

    def give_raise(self, newhourly):
        if (isinstance(newhourly, float) != True):
            raise ValueError("The hourly_pay field for this class expects a float type")

        self._hourly_pay = newhourly

    def display(self):
        output = str(self._first_name) + " " + str(self._last_name) + "\n"
        output += self._address + "\n"

        output += "Hourly employee: ${0:.2f}/hour\n".format(self._hourly_pay)
        output += "Start date: " + str(self._start_date) + "\n"
        return output

# Driver

if __name__ == "__main__":
    try:
        salary_man = SalariedEmployee("Bill", "Gates", "Seattle, Washington\nMicrosoft Land", "555-444-3333", datetime.datetime.strptime("11-6-2019", "%m-%d-%Y"), 40000)
        hourly_man = HourlyEmployee("Dave", "Chapelle", "Los Angeles, California\nUnited States", "333-222-1111", datetime.datetime.strptime("11-6-2019", "%m-%d-%Y"), 10.00)

        print(salary_man.display())
        salary_man.give_raise(45000)
        print(salary_man.display())
        del salary_man

        print(hourly_man.display())
        hourly_man.give_raise(12.00)
        print(hourly_man.display())
        del hourly_man
    except ValueError:
        print("Bad input")

