from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('.....')
root.iconbitmap('favicon.ico')

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

#create cursor
c = conn.cursor()

f_name_editor = Entry(editor, width=30)
f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name_editor = Entry(editor, width=30)
l_name_editor.grid(row=1, column=1)
address_editor = Entry(editor, width=30)
address_editor.grid(row=2, column=1)
city_editor = Entry(editor, width=30)
city_editor.grid(row=3, column=1)
state_editor = Entry(editor, width=30)
state_editor.grid(row=4, column=1)
zipcode_editor = Entry(editor, width=30)
zipcode_editor.grid(row=5, column=1)

f_name_label = Label(editor, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(editor, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(editor, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(editor, text="City")
city_label.grid(row=3, column=0)
state_label = Label(editor, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(editor, text="Zipcode")
zipcode_label.grid(row=5, column=0)

root.mainloop()