from tkinter import *
from gtts import gTTS
import os

root=Tk()
root.geometry("500x300")
root.config(background="light grey")
root.title("text to speech")

def convert():
    conversiontext=text.get()
    convertedtext=gTTS(text=conversiontext,lang="es")
    convertedtext.save("tts.wav")
    os.system("tts.wav")

text=Entry(root,font=("Ariel",15),width=30)
text.place(x=100,y=150)

caption=Label(root,text="Enter Text Here:",font=("Ariel",20),background="light grey")
caption.place(x=150,y=100)

submit=Button(root,text="Convert",activebackground="red",background="White",font=("Ariel",15),command=convert)
submit.place(x=205,y=190)


root.mainloop()