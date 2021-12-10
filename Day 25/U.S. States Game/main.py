import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed = []

while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What's another state's name?").title()
    data = pd.read_csv("50_states.csv")
    states = data.state.to_list()

    if answer_state == "Exit":
        missing = []
        for x in states:
            if x not in guessed:
                missing.append(x)
        new_data = pd.DataFrame(missing)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


