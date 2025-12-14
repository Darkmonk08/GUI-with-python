from tkinter import *
from gtts import gTTS
import os
import speech_recognition as sr

root=Tk()
root.geometry("500x300")
root.config(background="light grey")
root.title("speed to text")

def convert():
    recogniser=sr.Recognizer()
    with sr.Microphone()as source:
        audio=recogniser.listen(source)
        try:
            text=recogniser.recognize_google(audio)
        except:
            text="Unable to recognise"
    output.insert(END,text)


recordbtn=Button(root,text="Press to start recording",activebackground="red",background="White",font=("Ariel",14),command=convert)
recordbtn.place(x=170,y=190)

caption=Label(root,text="Text here:",font=("Ariel",20),background="light grey")
caption.place(x=180,y=50)

output=Text(root,font=("Ariel",15),width=30,height=3)
output.place(x=100,y=100)



root.mainloop()
