from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title("Pizza App")
root.geometry("600x350")


def place_order():
    pizza = pizza_var.get()
    amount = amount_var.get()
    size = size_var.get()

    if size == "S":
        size_text = "Small"
    elif size == "M":
        size_text = "Medium"
    else:
        size_text = "Large"

    if amount == "":
        result_label.config(text="Enter a quantity.")
    else:
        result_label.config(text=f"You ordered {amount} {pizza} {size_text} Pizza(s).")

title_label = Label(root, text="Welcome to Pizza Hut", font=("Arial", 16))
title_label.pack(pady=15)

frame = Frame(root)
frame.pack()

Label(frame, text="Select your favourite pizza:", font=("Arial", 12)).grid(row=0, column=0, pady=5)

pizza_var = StringVar()
pizza_dropdown = Combobox(frame,textvariable=pizza_var,values=["Veg Extravaganza", "Margherita", "Farmhouse", "Mexican Green Wave"],width=25)
pizza_dropdown.grid(row=0, column=1, padx=10)
pizza_dropdown.current(0)

Label(frame, text="Enter quantity:", font=("Arial", 12)).grid(row=1, column=0, pady=10)

amount_var = StringVar()
amount_entry = Entry(frame, textvariable=amount_var, width=10)
amount_entry.grid(row=1, column=1)

size_var = StringVar(value="S")

Radiobutton(frame, text="S", variable=size_var, value="S").grid(row=0,column=3,padx=10)
Radiobutton(frame, text="M", variable=size_var, value="M").grid(row=1,column=3,padx=10)
Radiobutton(frame, text="L", variable=size_var, value="L").grid(row=2,column=3,padx=10)

order_btn = Button(root, text="Order", width=12, command=place_order)
order_btn.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
