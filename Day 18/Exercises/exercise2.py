import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for x in range(10):
    tim.pendown()
    tim.forward(20)
    tim.penup()
    tim.forward(20)

screen = t.Screen()
screen.exitonclick()
