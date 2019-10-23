#!/usr/bin/python3
"""
Tanner Babcock
October 22, 2019
Module 9, topic 4: Intro to GUIs
"""
import tkinter

def breakfast():
    label.config(text="Selected Breakfast")

def breakfast2():
    label.config(text="Selected Second Breakfast")

def lunch():
    label.config(text="Selected Lunch")

def dinner():
    label.config(text="Selected Dinner")

m = tkinter.Tk()
m.title("Favorite Meal")
label = tkinter.Label(m, text="Waiting")
label.grid(row=4)

var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=breakfast).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=breakfast2).grid(row=1)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Selected Lunch", variable=var3, command=lunch).grid(row=2)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Selected Dinner", variable=var4, command=dinner).grid(row=3)

exit_button = tkinter.Button(m, text="Exit", width=25, command=m.destroy)
exit_button.grid(row=5)

m.mainloop()

