#Sam Bowles 15/06/2022
#trying to use a recursive function to generate a dragon curve

from turtle import *

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
    
    #check if we need to iterate
    if order > 0:
        
        #calculate midpoint of p1 and p2
        midP = [mid(p1[0], p2[0]),
                mid(p1[1], p2[1])
                ]

        if flip == False:            
            newPoint = [(midP[0] - (midP[1] - p1[1])),
                        (midP[1] + (midP[0] - p1[0]))
                        ]


        #flip means draw on other side of the line
        else:
            newPoint = [(midP[0] + (midP[1] - p1[1])),
                        (midP[1] - (midP[0] - p1[0]))
                        ]
            
        #iterate dragon curves using the new point
        dragon(p1, newPoint, order - 1, False)
        dragon(newPoint, p2, order - 1, True)
        
    else:
        #if the order is zero, just draw a line
        pen.goto(p1)
        pen.pendown()
        pen.goto(p2)
        pen.penup()

#main

wn.tracer(0,0) # <-- caption this if you want to see the line being drawn
dragon([-200,-150], [200,150], 11, False)
update() # <-- also caption this

mainloop() #make the window not close immediately
