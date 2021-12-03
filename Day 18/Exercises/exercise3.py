import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
deg = 360
shape_corners = 3
colors = ["blue","red","black","green","yellow","darkGreen","DeepSkyBlue"]
while shape_corners < 10:
    tim.color(random.choice(colors))
    for x in range(shape_corners):
        tim.right(deg / shape_corners)
        tim.forward(100)
    shape_corners += 1


screen = t.Screen()
screen.exitonclick()