from tkinter import *
import random

root = Tk()
root.title("Guess the word game")
root.geometry("450x500")
root.config(bg="black")
listofwords=[]
word=""
userscore=0

def readfile():
    global listofwords
    file=open(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\GUI-python\words.txt","r")
    content=file.read()
    listofwords=content.split("\n")
def maingame():
    global word
    word=random.choice(listofwords).lower()
    shuffledword=scramblewords(word)
    scrambled.config(text=shuffledword)
def scramblewords(word):
    word=list(word)
    print(word)
    random.shuffle(word)
    print(word)
    word="".join(word)
    print(word)
    return word
def submit():
    global userscore
    useranswer=answer.get()
    if useranswer==word:
        userscore=userscore+1
        score.config(text="Score = "+str(userscore))
        maingame()
        answer.delete(0,END)
readfile()


title=Label(root,text="Jumbler",foreground="White",background="black",font=("Ariel",30))
title.pack(pady=10)

scrambled=Label(root,text="",foreground="White",background="black",font=("Ariel",20))
scrambled.pack(pady=40)

answer=Entry(root,font=("Ariel",20))
answer.pack(pady=10)

submitbtn=Button(root,text="Submit",font=("Ariel",20),activebackground="Red",background="White",foreground="Black",command=submit)
submitbtn.pack(pady=5)

score=Label(root,text="Score = "+str(userscore),background="Black",foreground="White",font=("Ariel",15))
score.pack(pady=30)

maingame()

root.mainloop()
