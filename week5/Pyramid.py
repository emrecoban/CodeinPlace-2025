from graphics import Canvas
import random
import secrets

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base



def main():   
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    current_left_px = 90
    current_top_px = CANVAS_HEIGHT - BRICK_HEIGHT
    j = 14
    while j > 0:
        for i in range(j):
            brick(canvas, current_left_px, current_top_px)
            current_left_px = current_left_px + BRICK_WIDTH
        j -= 1
        current_top_px = current_top_px - BRICK_HEIGHT
        current_left_px = 90 + (14-j)*(BRICK_WIDTH / 2) 



def brick(canvas, left,top):
    canvas.create_rectangle(
    left, top , 
    BRICK_WIDTH + left, BRICK_HEIGHT + top, 
    "yellow", "black")
    

if __name__ == '__main__':
    main()
