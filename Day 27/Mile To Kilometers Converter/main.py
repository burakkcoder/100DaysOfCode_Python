from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

miles_text = Entry(width=10)
miles_text.grid(column=2, row=1)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=3, row=1)

equal_text = Label(text="is equal to", font=("Arial", 12))
equal_text.grid(column=1, row=2)

km_text = Label(text="", font=("Arial", 14))
km_text.grid(column=2, row=2)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=3, row=2)

def button_clicked():
    km_text["text"] = str(round(int(miles_text.get()) * 1.609))

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()