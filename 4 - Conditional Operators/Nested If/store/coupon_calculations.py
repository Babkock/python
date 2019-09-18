#!/usr/bin/python3
"""
Tanner Babcock
September 17, 2019

Module 4, Topic 3: Multiple and nested if statements
"""
def calculate_order(price, cash_coupon, percent_coupon):
    final_price = price
    discount = 0
    shipping = 0
    print("Initial price: {}".format(price))
    if cash_coupon > 0:
        final_price -= cash_coupon
        print("Cash coupon used")
        if percent_coupon > 0:
            discount = round(final_price * (percent_coupon * 0.01), 2)
            print("Percent coupon used")
            final_price -= discount
    else:
        if percent_coupon > 0:
            discount = round(final_price * (percent_coupon * 0.01), 2)
            print("Percent coupon used")
            final_price -= discount
    tax = round((final_price * 0.06), 2) # sales tax
    print("Subtotal: {}".format(final_price))
    if final_price <= 10.00:
        print("Small shipping")
        shipping = 5.95
    elif (final_price > 10.00) and (final_price <= 30.00):
        print("Medium shipping")
        shipping = 7.95
    elif (final_price > 30.00) and (final_price <= 50.00):
        print("Large shipping")
        shipping = 11.95
    else:
        shipping = 0
    return (final_price + shipping + tax)

if __name__ == '__main__':
    price = 15.99
    print("init price {0} = {1:.2f}".format(price, calculate_order(price, 5, 30)));

