#!/usr/bin/python3
import tkinter

m = tkinter.Tk()
m.title("Counting Sheep")
button = tkinter.Button(m, text='Stop', width=25, command=m.destroy)
button.pack()
m.mainloop()

