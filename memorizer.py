from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.geometry("800x600")
root.config(background="light grey")
root.title("memorizer")

def additem():
    item=entry.get()
    listbox.insert(END,item)

def deleteitem():
    selection=listbox.curselection()
    print(selection)
    if selection:
        selection=selection[::-1]
        for i in selection:
            listbox.delete(i)

def savefile():
    file=asksaveasfile(defaultextension=".txt")
    if file:
        for item in listbox.get(0,END):
            print(item,file=file)
        listbox.delete(0,END)

def openfile():
    file2=askopenfile(filetypes=[('Text Document','*.txt')])
    if file2:
        items=file2.readlines()
        print(items)
        listbox.delete(0,END)
        for item in items:
            print(item)
            listbox.insert(END,item.strip())

frame1=Frame(root,background="light grey")
frame1.pack()

frame2=Frame(root,background="light grey")
frame2.pack()

save=Button(frame1,text="Save",font=("Ariel",15),background="light grey",width=30,command=savefile)
save.pack(side=TOP,pady=10)

open=Button(frame1,text="Open",font=("Ariel",15),background="light grey",width=30,command=openfile)
open.pack(side=TOP,pady=10)

entry=Entry(frame1,font=("Ariel",15),width=30)
entry.pack(side=TOP,pady=20)

add=Button(frame2,text="Add",font=("Ariel",15),width=15,command=additem)
add.pack(side=LEFT,padx=10)

listbox=Listbox(frame2,font=("Ariel",15),width=30,selectmode="multiple")
listbox.pack(side=LEFT,padx=10)

delete=Button(frame2,text="delete",font=("Ariel",15),width=15,command=deleteitem)
delete.pack(side=LEFT,padx=10)



root.mainloop()

