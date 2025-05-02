from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?

while front_is_clear():
        move()
        while beepers_present():
            pick_beeper()
        if front_is_clear():
            put_beeper()
    turn_back()
    while front_is_clear():
        move()
    turn_back()
"""

def turn_around():
    turn_left()
    turn_left()


def main():
    move()

    while beepers_present():
        pick_beeper()
        if beepers_present():
            while beepers_present():
                move()
            put_beeper()
            turn_around()
            while front_is_clear():
                move()
            turn_around()
            move()
    put_beeper()
    turn_around()
    move()
    turn_around()
    




# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
