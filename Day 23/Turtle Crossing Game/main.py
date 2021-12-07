import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.summon_cars()
    car.move()

    for x in car.all_cars:
        if x.distance(turtle) < 25:
            scoreboard.game_over()
            game_is_on = False

    if turtle.ycor() >= 280:
        turtle.goto(0, -280)
        scoreboard.add_score()
        car.level_up()

screen.exitonclick()