#Sam Bowles 15/06/2022
#trying to use a recursive function to generate a dragon curve

from turtle import *

# setting up the window (wn) and the turtle for drawing the curve
wn = Screen()
pen = Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()


#functions

#midpoint function
def mid(a, b):
    midPoint = (a + b) / 2
    return midPoint

#dragon curve function
def dragon(p1, p2, order, flip):
    
    #check if we can draw a line yet
    if order > 0:
        
        #calculate midpoint of p1 and p2
        midP = [mid(p1[0], p2[0]),
                mid(p1[1], p2[1])
                ]

        #basic maths to find where the next point to draw to/from is
        #to get a better idea for how this works, see this graph: https://www.desmos.com/calculator/ccmf3rhlnp
        if flip == False:
            newPoint = [(midP[0] - (midP[1] - p1[1])),
                        (midP[1] + (midP[0] - p1[0]))
                        ]

        #flip just means find the point on opposite side of the line
        else:
            newPoint = [(midP[0] + (midP[1] - p1[1])),
                        (midP[1] - (midP[0] - p1[0]))
                        ]
            
        #recursively draw new dragon curves using the new point
        dragon(p1, newPoint, order - 1, False)
        dragon(newPoint, p2, order - 1, True)
        
    else:
        #if the order is zero, just draw a line from p1 to p2
        pen.goto(p1)
        pen.pendown()
        pen.goto(p2)
        pen.penup()

#main

wn.tracer(0,0) # <-- caption this if you want to see the line being drawn
dragon([-200,-150], [200,150], 11, False)
update() # <-- also caption this

mainloop() #makes the window not close immediately
