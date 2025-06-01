from karel.stanfordkarel import *

def main():
    if front_is_clear():
        move_to_midpoint()
    put_beeper()
    turn_around()

def move_to_midpoint():
    if facing_east():
        move()
        if front_is_clear():
            move()
            if front_is_clear():
                move_to_midpoint()
            else:
                turn_around()
        else:
            turn_around()        
    move()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
