from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def turn_normal():
    turn_left()
    turn_left()

def build_columns():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
    turn_normal()

def start_point():
    while front_is_clear():
        move()
    turn_left()

def between_columns():
    for i in range(4):
        move()

def main():
    turn_left()
    build_columns() 
    start_point()
    between_columns()
    turn_left()
    build_columns() 
    start_point()
    between_columns()
    turn_left()
    build_columns() 
    start_point()
    between_columns()
    turn_left()
    build_columns() 
    start_point()

if __name__ == '__main__':
    main()
