#!/usr/bin/python3
"""
Tanner Babcock
GUI Calculator Final Project
"""
import tkinter
import tkinter.font as font

class Calculator:
    def __init__(self):
        self.current_buffer = 0.0
        self.history = dict()

    def add_operation(self, op, value):
        if isinstance(op, str) != True:
            raise ValueError
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise ValueError
        self.history.update({ op : value })

    def equals(self):
        if op == '+':
            self.current_buffer += float(value)
        elif op == '-':
            self.current_buffer -= float(value)
        elif op == '*':
            self.current_buffer *= float(value)
        elif op == '/':
            self.current_buffer /= float(value)



if __name__ == "__main__":
    m = tkinter.Tk() 
    m.title("Calculator")
    m.config(bg="#101010")

    top_frame = tkinter.Frame(m, width=360, height=40, bg='#000000')
    top_frame.grid(row=0, column=0, padx=2, pady=5)
    bottom_frame = tkinter.Frame(m, width=360, height=250, bg='#000000')
    bottom_frame.grid(row=1, column=0, padx=2, pady=5)

    current = tkinter.Label(top_frame, text='0', width=14, height=3, fg="#efefef", bg="#101010", font=("Ubuntu Mono", 22))
    calc = Calculator()
    current.configure(text="{}".format(calc.current_buffer))
    current.pack()

    add = tkinter.Button(bottom_frame, text=' + ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571b18", activebackground="#c35b58", font=("Ubuntu Mono", 22)).grid(row=2, column=4)
    button9 = tkinter.Button(bottom_frame, text=' 9 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=2, column=3)
    button8 = tkinter.Button(bottom_frame, text=' 8 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=2, column=2)
    button7 = tkinter.Button(bottom_frame, text=' 7 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=2, column=1)
    subtract = tkinter.Button(bottom_frame, text=' - ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571b18", activebackground="#c35b58", font=("Ubuntu Mono", 22)).grid(row=3, column=4)
    button6 = tkinter.Button(bottom_frame, text=' 6 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=3, column=3)
    button5 = tkinter.Button(bottom_frame, text=' 5 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=3, column=2)
    button4 = tkinter.Button(bottom_frame, text=' 4 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=3, column=1)
    multiply = tkinter.Button(bottom_frame, text=' x ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571b18", activebackground="#c35b58", font=("Ubuntu Mono", 22)).grid(row=4, column=4)
    button3 = tkinter.Button(bottom_frame, text=' 3 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=4, column=3)
    button2 = tkinter.Button(bottom_frame, text=' 2 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=4, column=2)
    button1 = tkinter.Button(bottom_frame, text=' 1 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=4, column=1)
    period = tkinter.Button(bottom_frame, text=' . ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=5, column=1)
    button0 = tkinter.Button(bottom_frame, text=' 0 ', bd=0,  width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22)).grid(row=5, column=2)
    equals = tkinter.Button(bottom_frame, text=' = ', bd=0, width=2, height=2, fg="#204450", bg="#30adb8", activeforeground="#224b57", activebackground="#38b5c1", font=("Ubuntu Mono", 22)).grid(row=5, column=3)
    divide = tkinter.Button(bottom_frame, text=' / ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571818", activebackground="#c25858", font=("Ubuntu Mono", 22)).grid(row=5, column=4)

    current.configure(text="{}".format(0.0))

    m.mainloop()

