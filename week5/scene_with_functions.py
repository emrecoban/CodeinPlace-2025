from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw three clouds at different positions with different colors
    draw_cloud(canvas, 50, 40, 'lightpink')     # Left cloud - pink
    draw_cloud(canvas, 140, 10, 'salmon')       # Middle cloud - salmon (original)
    draw_cloud(canvas, 280, 50, 'purple')       # Right cloud - purple
    
    # Draw three trees at different positions
    draw_tree(canvas, 80, 'forestgreen')        # Left tree - green
    draw_tree(canvas, 200, 'red')               # Middle tree - red
    draw_tree(canvas, 320, 'orange')            # Right tree - orange

def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

def draw_tree(canvas, x, leaves_color):
    """
    This function draws one tree with a brown trunk and colored leaves.
    x is the horizontal position of the tree center.
    leaves_color is the color for the tree's leaves.
    """
    # Calculate trunk position (centered on x)
    trunk_left = x - TRUNK_WIDTH // 2
    trunk_right = x + TRUNK_WIDTH // 2
    trunk_top = TREE_BOTTOM_Y - TRUNK_HEIGHT
    trunk_bottom = TREE_BOTTOM_Y
    
    # Draw the trunk (rectangle)
    canvas.create_rectangle(
        trunk_left,
        trunk_top,
        trunk_right,
        trunk_bottom,
        'brown'
    )
    
    # Calculate leaves position (circle centered above trunk)
    leaves_radius = LEAVES_SIZE // 2
    leaves_left = x - leaves_radius
    leaves_right = x + leaves_radius
    leaves_top = trunk_top - leaves_radius
    leaves_bottom = trunk_top + leaves_radius
    
    # Draw the leaves (circle)
    canvas.create_oval(
        leaves_left,
        leaves_top,
        leaves_right,
        leaves_bottom,
        leaves_color
    )


if __name__ == '__main__':
    main()
