import turtle
from turtle import Turtle

starting_x_pos = [(0, 0), (-20, 0), (-40, 0)]
move_dist = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for x in starting_x_pos:
            self.add_box(x)

    def add_box(self,position):
        new_box = Turtle(shape="square")
        new_box.color("white")
        new_box.penup()
        new_box.goto(position)
        self.segments.append(new_box)

    def extend(self):
        self.add_box(self.segments[-1].position())

    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            new_x_pos = self.segments[x - 1].xcor()
            new_y_pos = self.segments[x - 1].ycor()
            self.segments[x].goto(new_x_pos, new_y_pos)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)