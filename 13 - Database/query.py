#!/usr/bin/python3
"""
Tanner Babcock
November 19, 2019
Module 13, topic 2: Connecting to a Database
"""
import sqlite3
from sqlite3 import Error

def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :returns: connection if no error, otherwise None """
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn, sql_create_table):
    """ Creates table with given SQL statement 
    :param conn: Connection object
    :param sql_create_table: A SQL CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

def create_tables(database):
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                        id integer PRIMARY KEY,
                        firstname text NOT NULL,
                        lastname text NOT NULL
                        ); """
    sql_create_student_table = """ CREATE TABLE IF NOT EXISTS student (
                        id integer PRIMARY KEY,
                        major text NOT NULL,
                        begin_date text NOT NULL,
                        end_date text,
                        FOREIGN KEY (id) REFERENCES person (id)
                        ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create person table
        create_table(conn, sql_create_person_table)
        # create student table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))

def create_person(conn, person):
    """ Create a new person for table
    :param conn: The connection object
    :param person: The person object
    :returns: ID of the new person
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor() # cursor object
    cur.execute(sql, person)
    return cur.lastrowid # returns the row ID of the cursor object, person ID

def create_student(conn, student):
    """ Create a new person for table
    :param conn: The connection object
    :param student: The student object
    :returns: ID of the new student
    """

    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?) '''
    cur = conn.cursor() # cursor object
    cur.execute(sql, student)
    return cur.lastrowid

if __name__ == "__main__":
    create_tables("pythonsqlite.db")
    conn = create_connection("pythonsqlite.db")
    with conn:
        person = ('Rob', 'Thomas')
        person_id = create_person(conn, person)

        student = (person_id, 'Songwriting', '2000-01-01')
        student_id = create_student(conn, student)

