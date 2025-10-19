from tkinter import *
import tkinter.font as font

root=Tk()
root.geometry("600x100")
root.config(background="light grey")
root.title("weight converter")

def convertvalues():
    weightget=float(weight.get())
    gramresult1=weightget*1000
    poundresult1=weightget*2.20462
    ounceresult1=weightget*35.274
    gramresult.config(text=gramresult1)
    poundresult.config(text=poundresult1)
    ouncesresult.config(text=ounceresult1)

topframe=Frame(root,background="light grey")
topframe.pack()
enter=Label(topframe,text="Enter Weight in Kg:",font=("Ariel",20))
enter.grid(row=0,column=0,padx=10)
weight=Entry(topframe,font=("Ariel",20), width=10)
weight.grid(row=0,column=1,padx=10)
convert=Button(topframe,text="Convert",activebackground="red",background="white", width=20,command=convertvalues)
convert.grid(row=0,column=2,padx=10)

font1=font.Font(weight="bold",size=7)

bottomframe=Frame(root)
bottomframe.pack(pady=10)
gram=Label(bottomframe,text="Grams:",width=30,font=font1)
gram.grid(row=0,column=0)
pound=Label(bottomframe,text="Pounds:",width=30,font=font1)
pound.grid(row=0,column=1)
ounces=Label(bottomframe,text="Ounces:",width=30,font=font1)
ounces.grid(row=0,column=2)
gramresult=Label(bottomframe,width=30)
gramresult.grid(row=1,column=0)
poundresult=Label(bottomframe,width=30)
poundresult.grid(row=1,column=1)
ouncesresult=Label(bottomframe,width=30)
ouncesresult.grid(row=1,column=2)

root.mainloop()