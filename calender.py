import tkinter as tk
import calendar

root = tk.Tk()
root.title("CALENDER")
root.geometry("300x250")
root.configure(bg="white")

def show_calender():
    contentscreen = tk.Tk()
    year=int(year_entry.get())
    content=calendar.calendar(year)
    contentdisplay = tk.Text(contentscreen,height=50)
    contentdisplay.insert(tk.END,content)
    contentdisplay.pack()
    contentdisplay.mainloop()

title_label = tk.Label(root, text="CALENDAR", font=("Times New Roman", 28), background="grey", foreground="black")
title_label.place(x=50, y=10)

year_label = tk.Label(root, text="Enter Year", font=("Arial", 12), background="lightgreen", foreground="green")
year_label.place(x=110, y=70)

year_entry = tk.Entry(root, font=("Arial", 14), justify='center')
year_entry.place(x=45, y=100)

show_button = tk.Button(root, text="Show Calendar", background="red", foreground="white", font=("Arial", 12), command=show_calender)
show_button .place(x=90, y=140)

exit_button = tk.Button(root, text="Exit", background="red", foreground="white", font=("Arial", 12), command=exit)
exit_button.place(x=130, y=180)


root.mainloop()