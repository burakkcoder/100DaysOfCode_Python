from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Text"
my_label.config(text="New Text") #same

def button_clicked():
    my_label["text"] = input.get()

button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

button2 = Button(text="Click Me2", command=button_clicked)
button2.grid(column=3, row=1)

#Entry
input = Entry(width=10)
input.grid(column=4, row=4)


window.mainloop()