from lib2to3.pgen2.token import OP
from sys import setswitchinterval
from tkinter import *

from numpy import sign
root = Tk()
#  not required here root.geometry()
root.title("calculator")
entry = Entry(root, width=65, borderwidth=5)
entry.grid(row=0, column=0, columnspan=10, padx=10, pady=10)


def button_add(number):
    # entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current)+str(number))

def button_clear():
    entry.delete(0,END)

def button_oporation(x):
    current = entry.get()
    global f_num
    f_num = int(current)
    entry.delete(0, END)
    global sign
    sign = x



def button_equal():
    current = entry.get()
    # entry.insert(0, str(eval(current)))
    if sign == "+":
        entry.delete(0, END)
        op = f_num + int(current)
        entry.insert(0, op)
    if sign == "-":
        entry.delete(0, END)
        op = f_num - int(current)
        entry.insert(0,op)
    if sign == "*":
        entry.delete(0, END)
        op = f_num * int(current)
        entry.insert(0,op)
    if sign == "/":
        entry.delete(0, END)
        op = f_num / int(current)
        entry.insert(0, op)




button_1 = Button(root, text="1", padx=40, pady=20,
                  command=lambda: button_add(1))
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: button_add(2))
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: button_add(3))
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: button_add(4))
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: button_add(5))
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: button_add(6))
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: button_add(7))
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: button_add(8))
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: button_add(9))
button_0 = Button(root, text="0", padx=40, pady=20,
                  command=lambda: button_add(0))
button_ads = Button(root, text='+', padx=40, pady=50,
                    command=lambda: button_oporation('+'))
button_sub = Button(root, text='-', padx=40, pady=20,command=lambda: button_oporation('-'))
button_mul = Button(root, text='*', padx=40, pady=20,command=lambda: button_oporation('*'))
button_div = Button(root, text='/', padx=40, pady=20,command=lambda: button_oporation('/'))
button_equal = Button(root, text='=', padx=40, pady=50,
                      command=button_equal)
button_clear = Button(root, text='clear', padx=141.5,
                      pady=10, command=button_clear)

# grid being set

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_ads.grid(row=1, column=3, rowspan=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4,column=0)
button_sub.grid(row=5, column=0)
button_mul.grid(row=4, column=1)
button_div.grid(row=4, column=2)
button_equal.grid(row=3, column=3, rowspan=2)
button_clear.grid(row=5, column=1, columnspan=3)

root.mainloop()
