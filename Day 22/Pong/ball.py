from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.move_x = 10
        self.move_y = 10
        self.speed = 0.1

    def move(self):
        x_cord = self.xcor() + self.move_x
        y_cord = self.ycor() + self.move_y
        self.goto(x_cord, y_cord)

    def vertical_bounce(self):
        self.move_y *= -1
        self.speed *= 0.9

    def horizontal_bounce(self):
        self.move_x *= -1
        self.speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.horizontal_bounce()

