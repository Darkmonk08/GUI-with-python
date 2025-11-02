from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Guess the number game")
root.geometry("400x250")
root.config(bg="light yellow")

welcome=Label(root, text="Welcome to our game!", bg="light yellow", font=("Arial", 14))
welcome.pack(pady=10)
namelbl=Label(root, text="What's your name?", bg="light yellow", font=("Arial", 12))
namelbl.pack()

name_entry = Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

def start_game():
    name = name_entry.get()
    if name == "":
        messagebox.showinfo("Info", "Please enter your name!")
    else:
        name_entry.pack_forget()
        name_button.pack_forget()
        Label(root, text="Well " + name + ", I am thinking of a number between 1 and 20.",
              bg="light yellow", font=("Arial", 12)).pack(pady=10)
        play_game(name)

name_button = Button(root, text="OK", command=start_game, bg="light green", width=10)
name_button.pack(pady=5)

def play_game(player_name):
    number_to_guess = random.randint(1, 20)

    enterlbl=Label(root, text="Enter your guess:", bg="light yellow", font=("Arial", 12))
    enterlbl.pack(pady=5)
    guess_entry = Entry(root, font=("Arial", 12))
    guess_entry.pack()

    def check_guess():
        guess = guess_entry.get()
        if guess == "":
            messagebox.showinfo("Info", "Please enter a number.")
        else:
            guess = int(guess)
            if guess < number_to_guess:
                messagebox.showinfo("Low", "Your guess is too low.")
            elif guess > number_to_guess:
                messagebox.showinfo("High", "Your guess is too high.")
            else:
                messagebox.showinfo("Good job!", "Congratulations " + player_name + "! You are right!")
    

    guessbutt=Button(root, text="Guess", command=check_guess, bg="light blue", width=10)
    guessbutt.pack(pady=10)

root.mainloop()