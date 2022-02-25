from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('.....')
root.iconbitmap('favicon.ico')
root.geometry("400x400")

# Database  

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

#create cursor
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS address(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)""")









# commit our command
conn.commit()

conn.close()

root.mainloop()