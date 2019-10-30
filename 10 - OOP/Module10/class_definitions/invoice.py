#!/usr/bin/python3
"""
Tanner Babcock
October 29, 2019
Module 10, topic 2: Classes and Objects
"""

class Invoice:
    # Constructor
    def __init__(self, iid, cid, lname, fname, phone, address, items=None):
        if (isinstance(iid, int) != True):
            raise AttributeError("Invoice object received non-numeric invoice_id\n")
        if (isinstance(cid, int) != True):
            raise AttributeError("Invoice object received non-numeric customer_id\n")
        if (isinstance(lname, str) != True):
            raise AttributeError("Invoice object received non-string last_name\n")
        if (isinstance(fname, str) != True):
            raise AttributeError("Invoice object received non-string first_name\n")
        if (isinstance(phone, str) != True):
            raise AttributeError("Invoice object received non-string phone_number\n")
        if (isinstance(address, str) != True):
            raise AttributeError("Invoice object received non-string address\n")

        self._invoice_id = iid
        self._customer_id = cid
        self._last_name = lname
        self._first_name = fname
        self._phone_number = phone
        self._address = address

        if (items != None):
            self._items_with_price = items

