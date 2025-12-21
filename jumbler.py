from tkinter import *

root = Tk()
root.title("Guess the word game")
root.geometry("450x500")
root.config(bg="black")

title=Label(root,text="Jumbler",foreground="White",background="black",font=("Ariel",30))
title.pack(pady=10)

scrambled=Label(root,text="asdadasdasd",foreground="White",background="black",font=("Ariel",20))
scrambled.pack(pady=40)

answer=Entry(root,font=("Ariel",20))
answer.pack(pady=10)

submitbtn=Button(root,text="Submit",font=("Ariel",20),activebackground="Red",background="White",foreground="Black")
submitbtn.pack(pady=5)

score=Label(root,text="Score = 0",background="Black",foreground="White",font=("Ariel",15))
score.pack(pady=30)

root.mainloop()