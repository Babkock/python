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
    def __init__(self, cid=1, lname="Test", fname="Test", phone="555-555-5555", address="5 Example Dr.\nExample, CA"):
        if (isinstance(cid, int) != True) and (isinstance(cid, float) != True):
            raise InvalidCustomerIdException("Customer object has non-numeric attribute 'cid'\n")

        if (cid < 1000) or (cid > 9999):
            raise InvalidCustomerIdException("Customer Id should be in range 1000-9999")


        if (isinstance(lname, str) != True):
            raise InvalidNameException("Last name is not str type\n")
        if (lname.isalpha() != True):
            raise InvalidNameException("Last name has non-alphabetic characters")

        if (isinstance(fname, str) != True):
            raise AttributeError("First name is not str type\n")
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
customer1 = Customer(1001, "Cassavetes", "John", "515-555-5555", "50 Hollywood Blvd.\nLos Angeles, CA")
print(customer1.display())

customer2 = Customer("1002", "Lincoln", "Abraham", "222-333-4444", "White House\nWashington, DC")
# AttributeError raised here, in the constructor

print(customer2.display())

