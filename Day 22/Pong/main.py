from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vertical_bounce()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.horizontal_bounce()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_point()

screen.exitonclick()