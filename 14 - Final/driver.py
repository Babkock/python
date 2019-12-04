#!/usr/bin/python3
"""
Tanner Babcock
GUI Calculator Final Project
"""
import tkinter
import tkinter.font as font
import decimal
from calculator import Operation
from calculator import Add
from calculator import Subtract
from calculator import Multiply
from calculator import Divide
from calculator import Calculator
#from calculator import decimal_places

calc = Calculator()
period_used = False
last_result = 0
thefont = "Ubuntu Mono"

# This function is the callback for all of the keys
def add_multiple_to_buffer(val):
    if isinstance(val, int) != True:
        raise ValueError("add_multiple_to_buffer() argument should be int type")
    if (val > 9) or (val < 0):
        raise ValueError("add_multiple_to_buffer() argument is out of range")

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
    if isinstance(val, int) != True:
        raise ValueError("add_number_after_period() argument should be int type")
    if (val > 9) or (val < 0):
        raise ValueError("add_number_after_period() argument is out of range")
    
    calc.current_buffer += (val * pow(10, (calc.places_back * -1)))
    calc.places_back += 1 
    
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
        calc.history = list()
        current.configure(text="{}".format(calc.current_buffer))
        period_used = False

    last_result = 0
    current = tkinter.Label(top_frame, text='0', width=14, height=3, fg="#efefef", bg="#101010", font=(thefont, 22))
    
    current.configure(text=("{0:." + str(calc.places_back) + "f}").format(calc.current_buffer))
    current.pack()
    # Clear the displayed number and history when the number itself is clicked
    current.bind("<Button-1>", clear_buffer)

    # This inner function determines if the current buffer was recently saved
    # in the history, and should be discarded. Then, it sends the int literal val to
    # either add_multiple_to_buffer(), or add_number_after_period()
    def press_number(val):
        global last_result
        global period_used
        if len(calc.history) > 0:
            if calc.history[-1].value == calc.current_buffer:
                calc.current_buffer = 0
                calc.places_front = 1
                calc.places_back = 0
        if last_result == calc.current_buffer:
            calc.current_buffer = 0
            calc.places_front = 1
            calc.places_back = 0
            last_result = 0
            period_used = False

        if period_used == True:
            add_number_after_period(val)
        else:
            add_multiple_to_buffer(val)
       
        if calc.places_back > 6:
            calc.current_buffer = float("{0:.6f}".format(str(calc.current_buffer)))

        current.configure(text=("{0:." + str(calc.places_back) + "f}").format(calc.current_buffer)) 

    def press_equals():
        global last_result
        calc.equals()
        last_result = calc.current_buffer
        d = decimal.Decimal(str(calc.current_buffer))
        calc.places_front = (len(d.as_tuple().digits) + d.as_tuple().exponent)
        calc.places_back = (d.as_tuple().exponent * -1)
        
        if calc.places_back > 6:
            current.configure(text="{0:.6f}".format(calc.current_buffer))
        else:
            current.configure(text=("{0:." + str(calc.places_back) + "f}").format(calc.current_buffer))

    def period():
        global period_used
        if period_used == False:
            period_used = True
            if calc.current_buffer == 0:
                calc.current_buffer = 0.0
                calc.places_front = 1
                calc.places_back = 1
            else:
                calc.current_buffer = float(calc.current_buffer * 1.0)
                calc.places_back = 1
        
        current.configure(text=("{0:." + str(calc.places_back) + "f}").format(calc.current_buffer))

    def plus():
        #calc.add_operation(Operation('+', calc.current_buffer))
        calc.add_operation(Add(calc.current_buffer))
        current.configure(text=("{0:." + str(calc.places_back) + "f}").format(calc.current_buffer))

    def minus():
        calc.add_operation(Operation('-', calc.current_buffer))
        current.configure(text=("{0:." + str(calc.places_back) + "f}").format(calc.current_buffer))

    def times():
        calc.add_operation(Operation('*', calc.current_buffer))
        current.configure(text=("{0:." + str(calc.places_back) + "f}").format(calc.current_buffer))

    def divide():
        calc.add_operation(Operation('/', calc.current_buffer))
        current.configure(text=("{0:." + str(calc.places_back) + "f}").format(calc.current_buffer))

    # It gets pretty ugly here but that is what makes it look good
    add = tkinter.Button(bottom_frame, text=' + ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571b18", activebackground="#c35b58", font=(thefont, 22), command=plus).grid(row=2, column=4)
    button9 = tkinter.Button(bottom_frame, text=' 9 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=lambda: press_number(9)).grid(row=2, column=3)
    button8 = tkinter.Button(bottom_frame, text=' 8 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=lambda: press_number(8)).grid(row=2, column=2)
    button7 = tkinter.Button(bottom_frame, text=' 7 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=lambda: press_number(7)).grid(row=2, column=1)
    subtract = tkinter.Button(bottom_frame, text=' - ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571b18", activebackground="#c35b58", font=(thefont, 22), command=minus).grid(row=3, column=4)
    button6 = tkinter.Button(bottom_frame, text=' 6 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=lambda: press_number(6)).grid(row=3, column=3)
    button5 = tkinter.Button(bottom_frame, text=' 5 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=lambda: press_number(5)).grid(row=3, column=2)
    button4 = tkinter.Button(bottom_frame, text=' 4 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=lambda: press_number(4)).grid(row=3, column=1)
    multiply = tkinter.Button(bottom_frame, text=' x ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571b18", activebackground="#c35b58", font=(thefont, 22), command=times).grid(row=4, column=4)
    button3 = tkinter.Button(bottom_frame, text=' 3 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=lambda: press_number(3)).grid(row=4, column=3)
    button2 = tkinter.Button(bottom_frame, text=' 2 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=lambda: press_number(2)).grid(row=4, column=2)
    button1 = tkinter.Button(bottom_frame, text=' 1 ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=lambda: press_number(1)).grid(row=4, column=1)
    period = tkinter.Button(bottom_frame, text=' . ', bd=0, width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=period).grid(row=5, column=1)
    button0 = tkinter.Button(bottom_frame, text=' 0 ', bd=0,  width=2, height=2, fg="#ffffff", bg="#000000", activeforeground="#eed92f", activebackground="#131313", font=(thefont, 22), command=lambda: press_number(0)).grid(row=5, column=2)
    equals = tkinter.Button(bottom_frame, text=' = ', bd=0, width=2, height=2, fg="#204450", bg="#30adb8", activeforeground="#224b57", activebackground="#38b5c1", font=(thefont, 22), command=press_equals).grid(row=5, column=3)
    divide = tkinter.Button(bottom_frame, text=' / ', bd=0, width=2, height=2, fg="#561410", bg="#bd5054", activeforeground="#571818", activebackground="#c25858", font=(thefont, 22), command=divide).grid(row=5, column=4)

    current.configure(text="{}".format(0))

    m.mainloop()
