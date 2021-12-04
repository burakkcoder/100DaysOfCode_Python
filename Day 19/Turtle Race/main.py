import tkinter
from turtle import Turtle, Screen
import random
from tkinter import messagebox

root = tkinter.messagebox

screen = Screen()
screen.setup(width = 500, height = 400)
screen.title("Turtle Race")

user_choice = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): ")

colors = ["red","orange","yellow","green","blue","purple"]
y_pos = [-80, -50, -20, 10 , 40 , 70]
all_turtles = []

for x in range(0,6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_pos[x])
    all_turtles.append(new_turtle)

on_race = False

if user_choice:
    on_race = True

while on_race:
    for x in all_turtles:
        if x.xcor() > 230:
            on_race = False
            winner = x.pencolor()
            if winner == user_choice:
                root.showinfo(title="Race Finished", message=f"You've won! The {winner} turtle is the winner!")
            else:
                root.showinfo(title="Race Finished", message=f"You've lost! The {winner} turtle is the winner!")
        random_forward = random.randint(0, 10)
        x.forward(random_forward)

screen.exitonclick()