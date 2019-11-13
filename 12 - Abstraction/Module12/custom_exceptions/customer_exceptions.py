#!/usr/bin/python3
"""
Tanner Babcock
November 12, 2019
Module 12, topic 2: Custom Exceptions
"""

class InvalidCustomerIdException(Exception):
    pass

class InvalidNameException(Exception):
    pass

class InvalidPhoneNumberFormat(Exception):
    pass

def valid_number(phone_number):
    if len(phone_number) != 12:
        return False
    for i in range(12):
        if i in [3,7]:
            if phone_number[i] != '-':
                return False
        elif not phone_number[i].isalnum():
            return False
    return True

class Customer:
    # Constructor
    def __init__(self, cid=1, lname="Test", fname="Test", phone="555-555-5555"):
        if (isinstance(cid, int) != True) and (isinstance(cid, float) != True):
            raise InvalidCustomerIdException("Customer object has non-numeric attribute 'cid'\n")

        if (cid < 1000) or (cid > 9999):
            raise InvalidCustomerIdException("Customer Id should be in range 1000-9999")


        if (isinstance(lname, str) != True):
            raise InvalidNameException("Last name is not str type\n")
        if (lname.isalpha() != True):
            raise InvalidNameException("Last name has non-alphabetic characters")

        if (isinstance(fname, str) != True):
            raise InvalidNameException("First name is not str type\n")
        if (fname.isalpha() != True):
            raise InvalidNameException("First name has non-alphabetic characters")

        if (isinstance(phone, str) != True):
            raise InvalidPhoneNumberFormat("Phone number is not str type")
        if (valid_number(phone) != True):
            raise InvalidPhoneNumberFormat("Phone number is invalid format")

        self._customer_id = cid
        self._last_name = lname
        self._first_name = fname
        self._phone_number = phone
     
    def display(self):
        output = "Customer #{}\n".format(self._customer_id)
        output += str(self._first_name) + " " + str(self._last_name) + "\n"
        output += str(self._phone_number)
        return output

    def __str__(self):
        output = "Customer #{}\n".format(self._customer_id)
        output += str(self._first_name) + " " + str(self._last_name) + "\n"
        output += str(self._phone_number)
        return output

if __name__ == "__main__":
    try:
        custom1 = Customer(1000, ',', 'a', '555-555-1234')
    except InvalidNameException:
        print("Invalid First Name Exception")

    try:
        custom1 = Customer(5, 'a', 'b', '333-555-5555')
    except InvalidCustomerIdException:
        print("Invalid Customer ID")

    try:
        custom1 = Customer(1002, 'a', ':', '444-555-4444')
    except InvalidNameException:
        print("Invalid Last Name Exception")

    try:
        custom1 = Customer(1003, 'a', 'b', '43-3')
    except InvalidPhoneNumberFormat:
        print("Invalid Phone Number Format Exception")
    finally:
        custom2 = Customer(1003, 'Hello', 'World', '555-123-1234')
        print(custom2)

