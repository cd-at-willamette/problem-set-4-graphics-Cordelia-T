########################################
# Name: Cordelia Trueax
# Collaborators: N/A
# Estimate time spent (hrs): .75
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score


def clicky_box():


# ======================= Function Definitions ==================================

    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        # if the mouse event happens within the bounds of the square,
        # in the x direction
        if event.get_x()>=init_square.get_x() and event.get_x()<= init_square.get_x()+SQUARE_SIZE:
            #in the y direction 
            if event.get_y()>=init_square.get_y() and event.get_y()<= init_square.get_y() + SQUARE_SIZE:
                # moves the square to a random new location
                move_square(init_square)
                # increments score
                gw.score = gw.score+1
                score_counter.set_label(str(gw.score))
        


    # function to return a random hexadecimal color code
    # I didn't realize random color wasn't required, but I've written this now so I might as well use it
    def random_color():
        color = "#"
        for i in range(6):
            color += random.choice("0123456789ABCDEF")

        return color
    

    
    # function moves a square object to a random new location within the bounds of the gWindow
    # and resets the color just for funsies
    def move_square(square):
        random_x = random.random()*(GW_WIDTH-SQUARE_SIZE) + (1/2*SQUARE_SIZE)
        random_y = random.random()*(GW_HEIGHT-SQUARE_SIZE) + (1/2*SQUARE_SIZE)

        square.set_bounds(random_x-(1/2*SQUARE_SIZE), random_y-(1/2*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE)
        square.set_color(random_color())
        



# ==================== Main Program ========================================

    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function

    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    
    gw.score = 0                           #variable to hold score itself

    # draws an initial square which can be moved later 
    init_square = GRect(GW_WIDTH/2 - 1/2*SQUARE_SIZE,  GW_HEIGHT/2 - 1/2*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
    init_square.set_color(random_color())
    init_square.set_filled(True)
    gw.add(init_square)

    # draws the score counter
    score_counter = GLabel(str(gw.score), SCORE_DX, GW_HEIGHT-SCORE_DY)
    score_counter.set_font(SCORE_FONT)
    gw.add(score_counter)
   

    gw.add_event_listener('mousedown', on_mouse_down)











if __name__ == '__main__':
    clicky_box()
