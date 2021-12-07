from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.left_paddle_score, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 230)
        self.write(self.right_paddle_score, align="center", font=("Arial", 50, "normal"))

    def left_point(self):
        self.left_paddle_score += 1
        self.update()

    def right_point(self):
        self.right_paddle_score += 1
        self.update()