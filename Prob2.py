########################################
# Name: Cordelia Trueax
# Collaborators: N/A
# Estimated time spent (hrs): 0.33
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 25
BRICK_HEIGHT = 25
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)

    # You got it from here
    # variable to store how many bricks are in the current row - starting with bottom row
    bricks_in_row = BRICKS_IN_BASE

    # number of rows is equal to bricks in base since one is decreased each row
    rows = BRICKS_IN_BASE
    # the start point for the y coordinate
    # starting point y is the same as starting point x (below) but with brick_height and plus 1 brick_height to start at the upper left corner
    start_y = (1/2 * HEIGHT) + (1/2 * rows * BRICK_HEIGHT) if rows % 2 == 0 else (1/2 * HEIGHT) + (1/2 * (rows-1) * BRICK_HEIGHT)

# while there is 1 or more bricks in the row
    while bricks_in_row>=1:
        # if the number of bricks is even, the starting point x is 1/2 brick_width + (bricks_in_row -1)/2 * brick_width
        # otherwise, it's just bricks_in_row/2 * brick_width
        # using ternary operator because I love long and convoluted lines of code
        start_x = (1/2 * WIDTH)- (1/2 * bricks_in_row * BRICK_WIDTH) if bricks_in_row % 2==0 else (1/2 * WIDTH) - ((1/2*BRICK_WIDTH)+ (bricks_in_row - 1)/2 * BRICK_WIDTH)


    # then just draw the bricks in row, incrementing 1 brick_width from starting x per brick
        for i in range(bricks_in_row):
            draw_brick(start_x + i*BRICK_WIDTH, start_y, gw)

    # and increments the starting points/variables
        bricks_in_row-=1
        start_y -=BRICK_HEIGHT
    

def draw_brick(x,y,gw):
    rect = GRect(x,y,BRICK_WIDTH, BRICK_HEIGHT)
    gw.add(rect)    







if __name__ == '__main__':
    draw_pyramid()
