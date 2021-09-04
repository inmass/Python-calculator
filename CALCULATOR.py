from tkinter import *
ws = Tk()
ws.title('CALCULATOR')
#ENTRY CREATION
e=Entry(ws, border=5)
#FUNCTIONS CREATION
def num_button(x):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(x))
def clearing():
    e.delete(0, END)
def addition():
    global task
    global first_number
    task = 'add'
    if '.' in e.get():
        first_number = float(e.get())
    else:
        first_number = int(e.get())
    e.delete(0, END)
def substtraction():
    global task
    global first_number
    task = 'substract'
    if '.' in e.get():
        first_number = float(e.get())
    else:
        first_number = int(e.get())
    e.delete(0, END)
def multiplication():
    global task
    global first_number
    task = 'multiply'
    if '.' in e.get():
        first_number = float(e.get())
    else:
        first_number = int(e.get())
    e.delete(0, END)
def division():
    global task
    global first_number
    task = 'divide'
    if '.' in e.get():
        first_number = float(e.get())
    else:
        first_number = int(e.get())
    e.delete(0, END)
def equal():
    if '.' in e.get():
        second_number = float(e.get())
    else:
        second_number = int(e.get())
    e.delete(0, END)
    if task == 'add':
        result = first_number+second_number
        if int(result) == result:
            e.insert(0, int(result))
        else:
            e.insert(0, result)
    elif task == 'substract':
        result = first_number-second_number
        if int(result) == result:
            e.insert(0, int(result))
        else:
            e.insert(0, result)
    elif task == 'multiply':
        result = first_number*second_number
        if int(result) == result:
            e.insert(0, int(result))
        else:
            e.insert(0, result)
    elif task == 'divide':
        result = first_number/second_number
        if int(result) == result:
            e.insert(0, int(result))
        else:
            e.insert(0, result)


#BUTTONS CREATION
button_zero = Button(ws, text='0',padx=47, pady=10, command= lambda:num_button(0))
button_point = Button(ws, text='.',padx=21, pady=10, command= lambda:num_button('.'))
button_addition = Button(ws, text='+',padx=20, pady=10, command= addition)

button_one = Button(ws, text='1',padx=20, pady=10, command= lambda:num_button(1))
button_second = Button(ws, text='2',padx=20, pady=10, command= lambda:num_button(2))
button_third = Button(ws, text='3',padx=20, pady=10, command= lambda:num_button(3))
button_substraction = Button(ws, text='-',padx=22, pady=10, command= substtraction)

button_fourth = Button(ws, text='4',padx=20, pady=10, command= lambda:num_button(4))
button_fifth = Button(ws, text='5',padx=20, pady=10, command= lambda:num_button(5))
button_sixth = Button(ws, text='6',padx=20, pady=10, command= lambda:num_button(6))
button_divide = Button(ws, text='/',padx=22, pady=10,command= division)
button_equal = Button(ws, text='=',padx=22, pady=55, command= equal)

button_seventh = Button(ws, text='7',padx=20, pady=10, command= lambda:num_button(7))
button_eighth = Button(ws, text='8',padx=20, pady=10, command= lambda:num_button(8))
button_ninth = Button(ws, text='9',padx=20, pady=10, command= lambda:num_button(9))
button_multiply = Button(ws, text='*',padx=22, pady=10, command= multiplication)
button_clear = Button(ws, text='C',padx=22, pady=10, command= clearing)
#BUTTONS GRID
e.grid(row=0, column=0,columnspan=5,sticky=EW)

button_zero.grid(row=4, column=0, columnspan=2)
button_point.grid(row=4, column=2)
button_addition.grid(row=4, column=3)

button_one.grid(row=3, column=0)
button_second.grid(row=3, column=1)
button_third.grid(row=3, column=2)
button_substraction.grid(row=3, column=3)

button_fourth.grid(row=2, column=0)
button_fifth.grid(row=2, column=1)
button_sixth.grid(row=2, column=2)
button_divide.grid(row=2, column=3)
button_equal.grid(row=2, column=4, rowspan=3)

button_seventh.grid(row=1, column=0)
button_eighth.grid(row=1, column=1)
button_ninth.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)
button_clear.grid(row=1, column=4)


ws.mainloop()
