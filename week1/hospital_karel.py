"""
Program: Hospital Karel
Karel traverses 1st Street from west to east, building hospitals
wherever it encounters a beeper.
"""
from karel.stanfordkarel import *

def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()
        safe_move()


def build_hospital():
    """
    Karel picks up supplies and builds a hospital.
    Pre-condition: Karel is on a beeper, representing a
        pile of supplies. Karel is facing east.
    Post-condition: Karel is standing at the bottom
        of the last column of the hospital, facing east.
    """
    # pick up supplies
    pick_beeper()
    do_one_column()
    move()
    do_one_column()


def do_one_column():
    """
    Karel builds a single column of a hospital.
    Pre-condition: Karel is facing east at the bottom
        of where we want to build a column.
    Post-condition: Karel is facing east at the bottom
        of the column it just built.
    """
    turn_left()
    put_three_beepers()
    return_to_base()
    turn_left()


def put_three_beepers():
    """
    Karel places three beepers in a row.
    Pre-condition: Karel is on the corner where we want
        to place the first beeper.
    Post-condition: Karel is on the corner where it
        placed the third beeper in a row.
    """
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()


def return_to_base():
    """
    Karel turns around and goes to the wall.
    Pre-condition: Karel is at the end of the column
        it just built, facing north.
    Post-condition: Karel has returned to 1st Street,
        below the column is just built, facing south.
    """
    turn_around()
    move_to_wall()


def move_to_wall():
    while front_is_clear():
        move()


def safe_move():
    if front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()


# Note: turn_right() is not called above but added for reference.
def turn_right():
    for i in range(3):
        turn_left()

    

if __name__ == '__main__':
    main()
