#!/usr/bin/python3
"""
Tanner Babcock
GUI Calculator Final Project
"""
import tkinter
import tkinter.font as font

class Calculator:
    def __init__(self):
        self.current_buffer = 0
        self.history = dict()
        self.places_front = 1
        self.places_back = 0

    def add_operation(self, op, value):
        if isinstance(op, str) != True:
            raise ValueError
        if (isinstance(value, int) != True) and (isinstance(value, float) != True):
            raise ValueError
        self.history.update({ op : value })
        print(self.history)

    def equals(self):
        if op == '+':
            self.current_buffer += float(value)
        elif op == '-':
            self.current_buffer -= float(value)
        elif op == '*':
            self.current_buffer *= float(value)
        elif op == '/':
            self.current_buffer /= float(value)

calc = Calculator()
period_used = False

# This function is the callback for all of the keys
def add_multiple_to_buffer(val):
    if (val > 9) or (val < 0):
        raise ValueError("add_multiple_to_buffer argument is out of range")
    # val is a number 0-9
    if calc.current_buffer == 0:
        if val == 0:
            calc.current_buffer = 0
        else:
            calc.current_buffer = val
    else:
        calc.places_front += 1
        if val == 0:
            calc.current_buffer *= 10
        else:
            multiple = calc.current_buffer * 10
            calc.current_buffer = multiple + val

def add_number_after_period(val):
    if (val > 9) or (val < 0):
        raise ValueError("add_number_after_period argument is out of range")
    
    if calc.places_back == 1:
        calc.places_back += 1
        calc.current_buffer += (val * 0.1)
    elif calc.places_back == 2:
        if val == 0:
            calc.places_back += 1
            calc.current_buffer *= 1.00
        else:
            calc.places_back += 1
            calc.current_buffer += (val * 0.01)
    elif calc.places_back == 3:
        if val == 0:
            calc.places_back += 1
            calc.current_buffer *= 1.000
        else:
            calc.places_back += 1
            calc.current_buffer += (val * 0.001)
    elif calc.places_back == 4:
        if val == 0:
            calc.places_back += 1
            calc.current_buffer *= 1.0000
        else:
            calc.places_back += 1
            calc.current_buffer += (val * 0.0001)
    elif calc.places_back == 5:
        if val == 0:
            calc.places_back += 1
            calc.current_buffer *= 1.00000
        else:
            calc.places_back += 1
            calc.current_buffer += (val * 0.00001)
    else:
        raise ValueError("Buffer too big")

if __name__ == "__main__":
    m = tkinter.Tk() 
    m.title("Calculator")
    m.config(bg="#101010")

    top_frame = tkinter.Frame(m, width=360, height=40, bg='#000000')
    top_frame.grid(row=0, column=0, padx=1, pady=3)
    bottom_frame = tkinter.Frame(m, width=360, height=250, bg='#000000')
    bottom_frame.grid(row=1, column=0, padx=1, pady=3)

    def clear_buffer(event):
        global period_used
        calc.current_buffer = 0
        calc.places_front = 1
        calc.places_back = 0
        current.configure(text="{}".format(calc.current_buffer))
        period_used = False

    current = tkinter.Label(top_frame, text='0', width=14, height=3, fg="#efefef", bg="#101010", font=("Ubuntu Mono", 22))
    if calc.places_back == 0:
        precision = 0
    elif calc.places_back == 1:
        precision = 1
    else:
        precision = calc.places_back - 1
    current.configure(text=("{0:." + str(precision) + "f}").format(calc.current_buffer))
    current.pack()
    current.bind("<Button-1>", clear_buffer)

    def press_number(val):
        if (calc.places_front > 6) or (calc.places_back > 5):
            raise ValueError("Buffer too big")
        if period_used == True:
            add_number_after_period(val)
        else:
            add_multiple_to_buffer(val)

        if calc.places_back == 0:
            precision = 0
        elif calc.places_back == 1:
            precision = 1
        else:
            precision = calc.places_back - 1
        
        current.configure(text=("{0:." + str(precision) + "f}").format(calc.current_buffer)) 

    def period():
        global period_used
        if period_used == False:
            period_used = True
            calc.current_buffer = float(calc.current_buffer * 1.0)
            calc.places_back = 1
        
        if calc.places_back == 0:
            precision = 0
        elif calc.places_back == 1:
            precision = 1
        else:
            precision = calc.places_back - 1

        current.configure(text=("{0:." + str(precision) + "f}").format(calc.current_buffer))

    add = tkinter.Button(bottom_frame, text=' + ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571b18", activebackground="#c35b58", font=("Ubuntu Mono", 22)).grid(row=2, column=4)
    button9 = tkinter.Button(bottom_frame, text=' 9 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=lambda: press_number(9)).grid(row=2, column=3)
    button8 = tkinter.Button(bottom_frame, text=' 8 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=lambda: press_number(8)).grid(row=2, column=2)
    button7 = tkinter.Button(bottom_frame, text=' 7 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=lambda: press_number(7)).grid(row=2, column=1)
    subtract = tkinter.Button(bottom_frame, text=' - ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571b18", activebackground="#c35b58", font=("Ubuntu Mono", 22)).grid(row=3, column=4)
    button6 = tkinter.Button(bottom_frame, text=' 6 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=lambda: press_number(6)).grid(row=3, column=3)
    button5 = tkinter.Button(bottom_frame, text=' 5 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=lambda: press_number(5)).grid(row=3, column=2)
    button4 = tkinter.Button(bottom_frame, text=' 4 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=lambda: press_number(4)).grid(row=3, column=1)
    multiply = tkinter.Button(bottom_frame, text=' x ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571b18", activebackground="#c35b58", font=("Ubuntu Mono", 22)).grid(row=4, column=4)
    button3 = tkinter.Button(bottom_frame, text=' 3 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=lambda: press_number(3)).grid(row=4, column=3)
    button2 = tkinter.Button(bottom_frame, text=' 2 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=lambda: press_number(2)).grid(row=4, column=2)
    button1 = tkinter.Button(bottom_frame, text=' 1 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=lambda: press_number(1)).grid(row=4, column=1)
    period = tkinter.Button(bottom_frame, text=' . ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=period).grid(row=5, column=1)
    button0 = tkinter.Button(bottom_frame, text=' 0 ', bd=0,  width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=("Ubuntu Mono", 22), command=lambda: press_number(0)).grid(row=5, column=2)
    equals = tkinter.Button(bottom_frame, text=' = ', bd=0, width=2, height=2, fg="#204450", bg="#30adb8", activeforeground="#224b57", activebackground="#38b5c1", font=("Ubuntu Mono", 22)).grid(row=5, column=3)
    divide = tkinter.Button(bottom_frame, text=' / ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571818", activebackground="#c25858", font=("Ubuntu Mono", 22)).grid(row=5, column=4)

    current.configure(text="{}".format(0))

    m.mainloop()

