from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}

try:
    data = pd.read_csv("data/turkish_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/turkish_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")

def next_card():
    global current_card, timer
    window.after_cancel(timer)

    current_card = random.choice(words)
    canvas.itemconfig(card_language, text="Turkish", fill="black")
    canvas.itemconfig(card_word, text=current_card["turkish"], fill="black")
    canvas.itemconfig(card_img, image=card_front_img)

    timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["english"], fill="white")
    canvas.itemconfig(card_img, image=card_back_img)

def unknown_words():
    words.remove(current_card)
    data = pd.DataFrame(words)
    data.to_csv("data/already_known.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
card_language = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

unknown_button_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_button_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_button_image, highlightthickness=0, command=unknown_words)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()