from tkinter import *
import speech_recognition as sr
from tkinter.filedialog import *

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
    output.insert(END,text+" ")
    
def save():
    file=asksaveasfile(defaultextension=".txt")
    if file:
        print(output.get(1.0,END),file=file)
        

savebtn=Button(root,text="Save",activebackground="red",background="White",font=("Ariel",14),command=save)
savebtn.place(x=120,y=190)

recordbtn=Button(root,text="Start Recording",activebackground="red",background="White",font=("Ariel",14),command=convert)
recordbtn.place(x=220,y=190)

caption=Label(root,text="Text here:",font=("Ariel",20),background="light grey")
caption.place(x=180,y=50)

output=Text(root,font=("Ariel",15),width=30,height=3)
output.place(x=100,y=100)



root.mainloop()
