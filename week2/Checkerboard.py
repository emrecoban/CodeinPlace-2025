from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    put_beeper()
    move_east()  
    return_home()
    pass    


def move_east():
    place_beepers_to_wall()
    turn_left()
    if front_is_clear():
        shift_to_next_row()
        turn_left()
        move_west()

def move_west():
    place_beepers_to_wall()
    turn_right()
    if front_is_clear():
        shift_to_next_row()
        turn_right()
        move_east()

def shift_to_next_row():
    if beepers_present():
        move()
    else:
        move()
        put_beeper()

def place_beepers_to_wall():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            move()
            put_beeper()

def turn_right():
    for _ in range(3):
        turn_left()

def return_home():
    while not_facing_south():
        turn_left()
    while front_is_clear():
        move()
    while not_facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()

def safe_move():
    if front_is_clear():
        move()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
