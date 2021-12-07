from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def summon_cars(self):
        random_summon_chance = random.randint(1,6)
        if random_summon_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(285, random.randint(-240,240))
            self.all_cars.append(new_car)

    def move(self):
        for x in self.all_cars:
            x.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT