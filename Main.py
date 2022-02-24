from tkinter import *

root =Tk()

mylabel1 = Label(root, text="Hello World")
mylabel2 = Label(root, text="bye World")

#pack() is used to display the label

# mylabel.pack()


# grid is used to display the label

 
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)

root.mainloop()


#button