from tkinter import *
from tkinter import messagebox
import random 

root=Tk()
root.geometry("800x300")
root.config(background="light grey")
root.title("window settings")

answeroptions=["Rock","Paper", "Scissors"]
result=""
playscore=0
compscore=0


def play(getplayerinput):
    global playscore,compscore
    print (getplayerinput)
    computerchoice=random.choice(answeroptions)
    print(computerchoice)
    if getplayerinput == computerchoice:
        result = "It's a draw!"
    elif (getplayerinput == "Rock" and computerchoice == "Scissors") or (getplayerinput == "Paper" and computerchoice == "Rock") or (getplayerinput == "Scissors" and computerchoice == "Paper"):
        result = "You win"
        playscore=playscore+1
    else:
        result = "Computer wins!"
        compscore=compscore+1
    outcome.config(text=result)
    playerscore.config(text="Playerscore:"+ str(playscore))
    computerscore.config(text="Computerscore:"+str(compscore))
    playerguess.config(text="Playerguess:"+str(getplayerinput))
    computerguess.config(text="Computerguess:"+str(computerchoice))

title=Label(root,text="ROCK PAPER SCISSIORS",font=("Ariel",20),background="light grey")
title.grid(row=0,column=1,columnspan=4,pady=5)

outcome=Label(root,text="Outcome:",font=("Ariel",15),background="light grey")
outcome.grid(row=1,column=1,columnspan=4)

options=Label(root,text="Your options:",font=("Ariel",15),background="light grey")
options.grid(row=2,column=1,padx=20)

rockbutton=Button(root,text="Rock",bg="red",activebackground="green",font=("Ariel",15),width=10,command=lambda:play("Rock"))
rockbutton.grid(row=2,column=2)

paperbutton=Button(root,text="Paper",bg="green",activebackground="red",font=("Ariel",15),width=10,command=lambda:play("Paper"))
paperbutton.grid(row=2,column=3,padx=10)

scissorsbutton=Button(root,text="Scissors",bg="blue",activebackground="red",font=("Ariel",15),width=10,command=lambda:play("Paper"))
scissorsbutton.grid(row=2,column=4,padx=10)

playerguess=Label(root,text="Player guess:",font=("Ariel",15),background="light grey")
playerguess.grid(row=3,column=2,padx=20,pady=30)

computerguess=Label(root,text="Computer guess:",font=("Ariel",15),background="light grey")
computerguess.grid(row=4,column=2,padx=20,pady=10)

playerscore=Label(root,text="Player score:",font=("Ariel",15),background="light grey")
playerscore.grid(row=3,column=3,padx=10,pady=30)

computerscore=Label(root,text="Computer score:",font=("Ariel",15),background="light grey")
computerscore.grid(row=4,column=3,padx=10,pady=10)



root.mainloop()
