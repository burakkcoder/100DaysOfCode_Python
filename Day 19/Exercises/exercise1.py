from turtle import Turtle, Screen

tim = Turtle()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_right():
    tim.right(10)

def move_left():
    tim.left(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkeypress(key = "w", fun = move_forwards)
screen.onkeypress(key = "s", fun = move_backwards)
screen.onkeypress(key = "a", fun = move_left)
screen.onkeypress(key = "d", fun = move_right)
screen.onkeypress(key = "space", fun = clear_screen)

screen.exitonclick()
