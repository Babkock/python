#!/usr/bin/python3
#
# Module 4, Topic 1: Selection statements
# Tanner Babcock
# September 10, 2019
print("Welcome to Programmer's Toolkit Monthly Subscription Box")
print("Subscription: 'p' Platinum, 'g' Gold, 's' Silver, 'b' Bronze, 'f' Free trial")
choice = input("Enter your subscription level: ")
cost = 0

if choice == 'p':
    print("Platinum selected")
    cost += 60
elif choice == 'g':
    print("Gold selected")
    cost += 50
elif choice == 's':
    print("Silver selected")
    cost += 40
elif choice == 'b':
    print("Bronze selected")
    cost += 30
elif choice == 'f':
    print("Free trial selected")
else:
    print("Invalid input")
    exit(1)

print("Your subscription costs ${}".format(cost))

exit(0)

