#####Turtle Intro######
import turtle as t

tim = t.Turtle()


######## Challenge 1 - Draw a Square ############
for x in range(4):
    tim.forward(100)
    tim.right(90)

screen = t.Screen()
screen.exitonclick()

