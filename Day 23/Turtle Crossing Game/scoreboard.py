from turtle import Turtle

FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.goto(-250, 270)
        self.hideturtle()
        self.update_level()

    def add_score(self):
        self.level += 1
        self.clear()
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align ="center", font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=FONT)

