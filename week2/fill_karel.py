from karel.stanfordkarel import *

def main():
    """
    Karel starts in the bottom-left corner facing right.
    The goal is to fill the entire world with beepers and end up
    in the top-right corner facing right.
    """
    # Fill first row and move to leftmost position of second row
    fill_row()
    move_to_next_row()
    
    # Fill all middle rows
    while front_is_clear():
        fill_row()
        if front_is_blocked():  # If at right edge
            move_to_next_row()
    
    # Fill the last row (if we're not already done)
    if front_is_clear():
        fill_row()

def fill_row():
    """Fill the current row with beepers from current position to the right wall"""
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    
    # Don't forget the last cell
    if no_beepers_present():
        put_beeper()

def move_to_next_row():
    """Navigate to the start of the next row using the left column passage"""

    # Turn around
    turn_around()
    
    # Move all the way to the left wall
    while front_is_clear():
        move()
    
    # We're at left wall, turn right to face north
    turn_right()
    
    # Check if we can move up (if not, we're at the top row)
    if front_is_clear():
        move()  # Move up one row
        turn_right()  # Face east to begin next row

    # IMPORTANT CODE BLOCK!!!
    if front_is_blocked() and facing_north() and beepers_present():
        turn_around()
        turn_left()
        while front_is_clear():
            move()

def turn_around():
    """Turn Karel around to face the opposite direction"""
    turn_left()
    turn_left()

def turn_right():
    """Turn Karel right"""
    for _ in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
