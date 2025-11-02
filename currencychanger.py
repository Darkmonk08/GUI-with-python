from tkinter import *
import tkinter.font as font


root = Tk()
root.geometry("600x400")
root.config(background="light grey")
root.title("INR to USD Converter")


def convertvalues():
    inr_amount = float(source_amount.get())
    usd_amount = inr_amount * 0.012 
    print(usd_amount)
    target_result.config(text=round(usd_amount, 2))


topframe = Frame(root, background="light grey")
topframe.pack(pady=10)

title_label = Label(topframe, text="₹ to $", font=("Arial", 24, "bold"), bg="light grey", fg="teal")
title_label.pack()

middleframe = Frame(root, background="light grey")
middleframe.pack(pady=10)

source_label = Label(middleframe, text="Source currency amount ₹", font=("Arial", 14), bg="light grey")
source_label.grid(row=0, column=0, padx=10, pady=5)

source_amount = Entry(middleframe, font=("Arial", 14), width=15)
source_amount.grid(row=0, column=1, padx=10, pady=5)

convert_btn = Button(middleframe, text="Convert", font=("Arial", 12, "bold"), bg="lightgreen", activebackground="green", width=20, command=convertvalues)
convert_btn.grid(row=1, column=0, columnspan=2, pady=10)

bottomframe = Frame(root, background="light grey")
bottomframe.pack(pady=10)

target_label = Label(bottomframe, text="Target currency amount $", font=("Arial", 14), bg="light grey")
target_label.grid(row=0, column=0, padx=10)

target_result = Label(bottomframe, text="", font=("Arial", 14, "bold"), bg="light grey", fg="blue")
target_result.grid(row=1, column=0, padx=10)

root.mainloop()