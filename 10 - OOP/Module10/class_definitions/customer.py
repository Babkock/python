#!/usr/bin/python3
"""
Tanner Babcock
October 29, 2019
Module 10, topic 2: Classes and Objects
"""

class Customer:
    # Constructor
    def __init__(self, cid=1, lname="Test", fname="Test", phone="555-555-5555", address="5 Example Dr.\nExample, CA"):
        if (isinstance(cid, int) != True) and (isinstance(cid, float) != True):
            raise AttributeError("Customer object has non-numeric attribute 'cid'\n")
        if (isinstance(lname, str) != True):
            raise AttributeError("Last name is not str type\n")
        if (isinstance(fname, str) != True):
            raise AttributeError("First name is not str type\n")
        if (isinstance(phone, str) != True):
            raise AttributeError("Phone number is not str type\n")
        if (isinstance(address, str) != True):
            raise AttributeError("Address is not str type\n")

        self._customer_id = cid
        self._last_name = lname
        self._first_name = fname
        self._phone_number = phone
        self._address = address
    
    def set_customer_id(self, cid):
        if (isinstance(cid, int) != True) and (isinstance(cid, float) != True):
            raise AttributeError("set_customer_id on non-numeric 'cid'")
        self._customer_id = cid

    def set_first_name(self, fname):
        if (isinstance(fname, str) != True):
            raise AttributeError("set_first_name on non-string 'fname'")
        self._first_name = fname

    def set_last_name(self, lname):
        if (isinstance(lname, str) != True):
            raise AttributeError("set_last_name on non-string 'lname'")
        self._last_name = lname

    def set_phone_number(self, phone):
        if (isinstance(phone, str) != True):
            raise AttributeError("set_phone_number on non-string")
        self._phone_number = phone

    def display(self):
        output = "Customer #{}\n".format(self._customer_id)
        output += str(self._first_name) + " " + str(self._last_name) + "\n"
        output += str(self._address) + "\n"
        output += str(self._phone_number) + "\n"
        return output

# Driver
customer1 = Customer(1, "Cassavetes", "John", "515-555-5555", "50 Hollywood Blvd.\nLos Angeles, CA")
print(customer1.display())

customer2 = Customer("2", "Lincoln", "Abraham", "222-333-4444", "White House\nWashington, DC")
# AttributeError raised here, in the constructor

print(customer2.display())

