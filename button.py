from tkinter import *

root =Tk()


def myClick():
    mylabel1 = Label(root, text="Hello World")
    mylabel2 = Label(root, text="bye World")
    mylabel1.pack()
    mylabel2.pack()



mybutton = Button(root, text="Click Me", command=myClick, fg="blue", bg="red")

mybutton.pack()

root.mainloop()