from email import message
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()
root.title('.....')
root.iconbitmap('favicon.ico')

def Popup():
    messagebox.showinfo('Title', 'Message')

Button(root, text='Popup',command=Popup).pack()



root.mainloop()