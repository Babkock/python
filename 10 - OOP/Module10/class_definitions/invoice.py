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
            raise AttributeError("Invoice object received non-numeric invoice_id")
        if (isinstance(cid, int) != True):
            raise AttributeError("Invoice object received non-numeric customer_id")
        if (isinstance(lname, str) != True):
            raise AttributeError("Invoice object received non-string last_name")
        if (isinstance(fname, str) != True):
            raise AttributeError("Invoice object received non-string first_name")
        if (isinstance(phone, str) != True):
            raise AttributeError("Invoice object received non-string phone_number")
        if (isinstance(address, str) != True):
            raise AttributeError("Invoice object received non-string address")

        self._invoice_id = iid
        self._customer_id = cid
        self._last_name = lname
        self._first_name = fname
        self._phone_number = phone
        self._address = address

        if (items != None):
            self._items_with_price = items

    def add_item(self, item):
        self._items_with_price.update(item)

    def create_invoice(self):
        if (self._items_with_price == None):
            raise AttributeError("No items_with_price dictionary\n")
        subtotal = 0.0
        total = 0.0
        for key, value in self._items_with_price.items():
            subtotal += value
        tax = float(subtotal * 0.06)
        total = subtotal + tax

        for key, value in self._items_with_price.items():
            print("{0} ..... ${1:.2f}".format(key, value))
        print("Tax ..... ${0:.2f}".format(tax))
        print("Total ..... ${0:.2f}".format(total))

# Driver
inv = Invoice(1, 2, "Smith", "John", "555-333-4444", "12 Example St.\nNew York, NY", {'iPad' : 799.99})
inv.add_item({'Surface' : 999.99})
inv.create_invoice()
del inv

