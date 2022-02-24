from cgitb import text
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("learn frame")
# root.geometry("400x400")
root.iconbitmap("favicon.ico")
frame = Frame(root,width=400, height=400)
frame.pack(padx=20, pady=20)

btn1 = Button(frame, text="Button 1")
# btn1.pack(side=LEFT)
btn1.grid(row=0, column=0)
btn2 = Button(frame, text="Button 2")
# btn2.pack(side=LEFT)
btn2.grid(row=0, column=1)
btn3 = Button(frame, text="Button 3")
# btn3.pack(side=LEFT)
btn3.grid(row=0, column=2)


root.mainloop()