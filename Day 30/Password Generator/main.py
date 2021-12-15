from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_text.get()
    email_username = email_username_text.get()
    password = password_text.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if website == "" or email_username == "" or password == "":
        messagebox.showinfo(title="Opps", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data:
                data_file = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            data_file.update(new_data)

            with open("data.json", "w") as data:
                json.dump(data_file, data, indent=4)
        finally:
            website_text.delete(0, END)
            email_username_text.delete(0, END)
            password_text.delete(0, END)

def find_password():
    website = website_text.get()
    try:
        with open("data.json") as data:
            data_file = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data_file:
            email_username = data_file[website]["email"]
            password = data_file[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email_username}\n\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", pady=10)
website_label.grid(column=0, row=1)

website_text = Entry(width=30)
website_text.grid(column=1, row=1, columnspan=2, sticky="w")
website_text.focus()

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

email_username_label = Label(text="Email/Username:", pady=10)
email_username_label.grid(column=0, row=2)

email_username_text = Entry(width=52)
email_username_text.grid(column=1, row=2, columnspan=2, sticky="w")
email_username_text.insert(0, "email@gmail.com")

password_label = Label(text="Password:", pady=10)
password_label.grid(column=0, row=3)

password_text = Entry(width=30)
password_text.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
