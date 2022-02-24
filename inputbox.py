from re import I
from tkinter import *

root =Tk()
e = Entry(root, width=50, borderwidth=5)
e.pack(padx=10, pady=10)
e.insert(0, "Enter your name: ")


def myClick():
    mylabel1 = Label(root, text=e.get())
    mylabel1.pack()

mybutton = Button(root, text="Click Me", command=myClick, fg="blue", bg="red")

mybutton.pack()

root.mainloop()