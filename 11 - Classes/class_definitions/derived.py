#!/usr/bin/python3
"""
Tanner Babcock
November 6, 2019
Module 11, topic 2: Inheritance
"""

class Person:
    def __init__(self, lname, fname, addy=''):
        if (isinstance(lname, str) != True):
            raise AttributeError("Last name field must be a string")
        if (isinstance(fname, str) != True):
            raise AttributeError("First name field must be a string")

        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address

class Student(Person):
    def __init__(self, sid, lname, fname, maj='Computer Science', gpa=0.0, addy=''):
        super().__init__(lname, fname, addy)
        
        if (isinstance(sid, int) != True):
            raise AttributeError("Student ID must be an integer")
        if (isinstance(maj, str) != True):
            raise AttributeError("Major field must be a string")
        if (isinstance(gpa, float) != True):
            raise AttributeError("GPA field must be a float")
        if (gpa < 0.0) or (gpa > 4.0):
            raise AttributeError("GPA must be in valid range")

        self._student_id = sid
        self._major = maj
        self._gpa = gpa

    def display(self):
        output = self._last_name + ", " + self._first_name + ":({}) {}".format(self._student_id, self._major)
        output += " gpa: {0:.2f}".format(self._gpa)
        return output

# Driver
if __name__ == "__main__":
    my_student = Student(900111111, "Tip", "Q")
    print(my_student.display())
    my_student = Student(900222222, "Shaheed Muhammad", "Ali", "Two Turntables and a Microphone")
    print(my_student.display())
    my_student = Student(900333333, "Cherry", "Don", "Trumpet", 3.9)
    print(my_student.display())
    del my_student

