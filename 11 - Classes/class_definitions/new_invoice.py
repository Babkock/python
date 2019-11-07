#!/usr/bin/python3
"""
Tanner Babcock
November 6, 2019
Module 11, topic 1: More Classes
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

class Invoice:
    # Constructor
    def __init__(self, iid, custom, items=None):
        if (isinstance(iid, int) != True):
            raise AttributeError("Invoice object received non-numeric invoice_id")

        self._invoice_id = iid
        self._customer = custom

        if (items != None):
            self._items_with_price = items
        else:
            self._items_with_price = {}

    def add_item(self, item):
        self._items_with_price.update(item)

    def create_invoice(self):
        if (self._items_with_price == None):
            raise AttributeError("No items_with_price dictionary\n")
        print(self._customer.display())

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
if __name__ == "__main__":
    man = Customer(5, "Argento", "Dario", "666-666-6666", "Rome, Italy")
    inv = Invoice(1, man)
    inv.add_item({ 'Murder' : 5000.00 })
    inv.add_item({ 'Sex' : 4000.00 })
    inv.create_invoice()
    del inv
    del man

    man2 = Customer(6, "Dawg", "Pfife", "111-222-3333", "Queens or Brooklyn")
    inv2 = Invoice(2, man2)
    inv2.add_item({ 'Butter' : 17.00 })
    inv2.add_item({ 'Ham and Eggs' : 20.00 })
    inv2.add_item({ 'Nice Red Beets' : 30.00 })
    inv2.create_invoice()
    del inv2
    del man2

