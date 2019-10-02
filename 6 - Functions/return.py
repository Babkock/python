#!/usr/bin/python3
"""
Tanner Babcock
October 1, 2019

Module 6, topic 2: Function return values
"""
"""
This function returns the employee's name and weekly pay

:param name: The employee first and last name
:param hours: The total number of hours the employee worked
:param wage: The employee's hourly wage
:returns: A string with the employee's name and weekly pay
"""
def hourly_employee_input(name, hours, wage):
    try:
        if (isinstance(name, str) != True):
            raise ValueError
        if (isinstance(hours, int) != True):
            raise ValueError
        if (isinstance(wage, float) != True):
            raise ValueError
        return "{0} made ${1:.2f} this week".format(name, weekly_pay(hours, wage))
    except:
        return "Bad input"

"""
This function calculates the weekly pay and returns it

:param hours_worked: The total number of hours the employee worked
:param hourly_pay_rate: The employee's hourly wage
:returns: The total weekly pay
:raises ValueError: If the input is bad
"""
def weekly_pay(hours_worked, hourly_pay_rate):
    if (isinstance(hours_worked, int) != True):
        raise ValueError
    if (isinstance(hourly_pay_rate, float) != True):
        raise ValueError
    return float(int(hours_worked) * hourly_pay_rate)

if __name__ == '__main__':
    print(hourly_employee_input("Tanner Babcock", 40, 12.50))
    print(hourly_employee_input(10, "test", -5))

