from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

    if website == "" or email_username == "" or password == "":
        messagebox.showinfo(title="Opps", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_text.get(),
                                       message=f"These are the details entered:\n\nEmail: {email_username}\n\nPassword: {password}\n\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email_username} | {password} \n")
                website_text.delete(0, END)
                email_username_text.delete(0, END)
                password_text.delete(0, END)

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", pady=10)
website_label.grid(column=0, row=1)

website_text = Entry(width=52)
website_text.grid(column=1, row=1, columnspan=2, sticky="w")
website_text.focus()

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