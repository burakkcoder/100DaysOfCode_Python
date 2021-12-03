import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

walk = 0
tim.pensize(15)
tim.speed("fastest")
t.colormode(255)

while walk < 100:
    turn = random.choice([0,90,180,270])
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(turn)
    walk += 1

screen = t.Screen()
screen.exitonclick()