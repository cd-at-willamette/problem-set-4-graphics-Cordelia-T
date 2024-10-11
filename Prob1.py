############################################################
# Name: Cordelia Trueax
# Name(s) of anyone worked with: N/A
# Est time spent (hr): 0.5
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!

    # Stem
    w = 5
    h = 300
    stem = GRect(WIDTH/2+15, HEIGHT-h, w, h)
    stem.set_color("green")
    stem.set_filled(True)
    gw.add(stem)

    # Petals
     # center point
    cent_x = WIDTH/2
    cent_y = HEIGHT/2
    # radius of flower petal range
    radius = 40

    # modifiers for the coordinates of flower petals so they make a circle
    coordinates = ((1,0), (2**(1/2)/2, 2**(1/2)/2), (0,1), (-2**(1/2)/2, 2**(1/2)/2), (-1,0), (-2**(1/2)/2, -2**(1/2)/2), (0,-1), (2**(1/2)/2, -2**(1/2)/2))

    for i in range(8):
        # flower petals are at coordinates radius * (1,0), (sqrt(2)/2), (0,1), (-sqrt(2)/2)... all plus cent_x & cent_y
        petal = GOval(cent_x+(radius*coordinates[i][0]), cent_y+(radius*coordinates[i][1]), 40, 40)
        petal.set_fill_color("orange")
        petal.set_filled(True)
        gw.add(petal)

        
    # draws center of flower
    center = GOval(WIDTH/2, HEIGHT/2, radius, radius)
    center.set_color("black")
    center.set_filled(True)
    gw.add(center)


    # label & underscore
    label = GLabel("Sunflower?", WIDTH/2-25, HEIGHT/4)
    label.set_color("black")
    gw.add(label)

    line = GLine(WIDTH/2-25,HEIGHT/4+10,WIDTH/2+55,HEIGHT/4+10)
    line.set_color("black")
    gw.add(line)





if __name__ == '__main__':
    draw_image()
