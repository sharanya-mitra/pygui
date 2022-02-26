
from calendar import c
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

from numpy import record


root = Tk()
root.title('.....')
root.geometry("400x400")



# c.execute("""CREATE TABLE addresses (
# 		first_name text,
# 		last_name text,
# 		address text,
# 		city text,
# 		state text,
# 		zipcode integer
# 		)""")

def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("DELETE FROM addresses WHERE oid="+delete_box.get())
    delete_box.delete(0, END)
    conn.commit()


def summit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",
              {
                  'first_name': f_name.get(),
                  'last_name': l_name.get(),
                  'address': address_name.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })
   
   
    conn.commit()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address_name.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record[0]) +" "+str(record[1])+" "+str(record[2])+" "+str(record[3])+" "+str(record[4])+" "+" "+str(record[5])+" "+str(record[6])+" "+"\n"
        query_label = Label(root, text=print_records)
        query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()

#    return "SELECT * FROM addresses" 






f_name = Entry(root, width=30)
f_name.grid(row=0,column=1,padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1,column=1,padx=20)

address_name = Entry(root, width=30)
address_name.grid(row=2,column=1,padx=20)

city = Entry(root, width=30)
city.grid(row=3,column=1,padx=20)

state = Entry(root, width=30)
state.grid(row=4,column=1,padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5,column=1,padx=20)

delete_box = Entry (root,width=30)
delete_box.grid(row=8,column=1)

#creating label
f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0,padx=20)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1,column=0,padx=20)
address_label = Label(root, text="Address")
address_label.grid(row=2,column=0,padx=20)
city_label = Label(root, text="City")
city_label.grid(row=3,column=0,padx=20)
state_label = Label(root, text="State")
state_label.grid(row=4,column=0,padx=20)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5,column=0,padx=20)
delete_label = Label(root, text="Delete")
delete_label.grid(row=8,column=0,padx=20)

summit_btn = Button(root, text="Submit", command=summit)
summit_btn.grid(row=6,column=0,columnspan=2,padx=20,pady=20,ipadx=100)

#query btn
query_btn = Button(root, text="Query", command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=20,pady=20,ipadx=100)

#delete btn

delete_btn = Button(root, text="Delete", command=delete)
delete_btn.grid(row=9,column=0,columnspan=2,padx=20,pady=20,ipadx=100)

root.mainloop()