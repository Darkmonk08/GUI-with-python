from tkinter import *
from tkinter.ttk import *

root=Tk()
root.geometry("500x300")
root.config(background="light grey")
root.title("window settings")

def gettable():
    tablenum=selectednum.get()
    numchoice=numberchoice.get()
    result=""
    for i in range(numchoice):
        table2=f"{tablenum} X {i} = {tablenum*i}"
        result=result+str(table2)+"\n"
    table.config(text=result)
title=Label(root,text="Mathematical Table",background="light grey",font=("Ariel",20))
title.place(x=130,y=10)

title2=Label(root,text="Number:",background="light grey",font=("Ariel",20))
title2.place(x=40,y=100)

selectednum=IntVar()
numberopt=Combobox(root,textvariable=selectednum,font=("Ariel",15))
numberopt.place(x=150,y=105)

numberopt["values"]=tuple(range(31))
selectednum.set(1)

rangelbl=Label(root,text="Range:",font=("Ariel",15),background="light grey")
rangelbl.place(x=430,y=20)

numberchoice=IntVar()
radio1=Radiobutton(root,text=10,value=10,variable=numberchoice)
radio1.place(x=450,y=60)

radio2=Radiobutton(root,text=20,value=20,variable=numberchoice)
radio2.place(x=450,y=100)

radio3=Radiobutton(root,text=30,value=30,variable=numberchoice)
radio3.place(x=450,y=140)
numberchoice.set(10)

generate=Button(root,text="Generate",command=gettable)
generate.place(x=220,y=200)

table=Label(root,text="",font=("Ariel",12),background="light grey")
table.place(x=220,y=230)


root.mainloop()
