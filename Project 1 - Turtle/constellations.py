# Import all elements of the turtle library:
from turtle import *
from random import randint

# Set up the graphics window:
screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")

# Create a turtle object and set some of its attributes:
starmaker = Turtle()
starmaker.shape("square")
starmaker.resizemode("auto")
starmaker.width(4)
starmaker.pencolor("black")
starmaker.fillcolor("lightslategray")
starmaker.speed(10)
starmaker.hideturtle()

#----------------------------#

# FUNCTIONS
def draw_star():
    starmaker.stamp()
    
#    old code for draw_star() that used to draw literal stars
#    I decided to stylize the stars because I liked how that looked better
#    starmaker.begin_fill()
#    for side in range (5):
#        print(f"side is {side+1}")
#        starmaker.forward(50)
#        starmaker.left(145)
#    starmaker.end_fill()
    
def constellation(list):
    #print(f"starting {list}")
    starmaker.fillcolor("white")
    starmaker.pencolor("gold")
    for item in list:
        #print(item)
        starmaker.goto(item[0], item[1])
        draw_star()    

# ACCEPTABLE BACKGROUND STAR COLOR LIST
starcolor = ["cadetblue", "slateblue", "lightslategray", "darkslateblue"]

# STAR COORDINATE LISTS FOR CONSTELLATIONS
big_dipper = [ [-350, 350],
               [-200, 250],
               [-100, 100],
               [0, 0],
               [-20, -150],
               [200, -200],
               [300, -75]
              ]

cassiopeia = [ [-350, 250],
               [-230, 100],
               [-50, 110],
               [100, -100],
               [250, 100]
              ]

# MAKE BACKGROUND
for starcount in range(40):
    starmaker.up()
    starmaker.goto(randint(-500, 500), randint(-500,500))
    starmaker.fillcolor(starcolor[randint(0,3)])
    draw_star()
    


# USER CHOICE
choice = input("which constellation would you prefer to draw, big dipper or cassiopeia? ")
#print(choice)

if choice == "big dipper":
    constellation(big_dipper)
elif choice == "cassiopeia":
    constellation(cassiopeia)
else:
    print("invalid input")



#----------------------------#

# Closes the graphics window when the user clicks:
exitonclick() 