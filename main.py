from tkinter import *
from tkinter import ttk
from pymongo import MongoClient
import messagebox

Client = MongoClient(host='Localhost', port=27017)
db = Client['CRUD']
persons = db['persons']
win = Tk()
win.geometry('1000x600')
# win.attributes('-fullscreen',True)
win.title('CRUD')
win.iconbitmap('E:/CRUD/.venv/images/python_icon_130849.ico')
win.configure(background='#0C1726')


def change_button_style_with_hover(e):
    btnRegister.configure(bg='yellow', fg='green')


def change_button_style_with_hover_to_self(e):
    btnRegister.configure(bg='white', fg='black')


def click_on_register(e):
    person = {'name': txtName.get(), 'family': txtFamily.get(), 'field': txtField.get(), 'age': txtAge.get()}
    clear_table()
    register(person)
    insert_data_to_table(person)


def register(person):
    persons.insert_one(person)
    # print(persons)


def read_data():
    alldata = persons.find()
    # print(AllData[1])


def clear_table():
    for item in table.get_children():
        table.delete(item)
    read_data()


def insert_data_to_table(person):
    table.insert(parent='', index='end', values=[person['name'], person['family'], person['field'], person['age']])


# lbl
lblName = Label(win, width=10, text='Name', font=('arial', 15, 'bold'), bg='yellow', fg='black')
lblName.place(x=20, y=100)
lblFamily = Label(win, width=10, text='Family', font=('arial', 15, 'bold'), bg='yellow', fg='black')
lblFamily.place(x=20, y=160)
lblAge = Label(win, width=10, text='Age', font=('arial', 15, 'bold'), bg='yellow', fg='black')
lblAge.place(x=20, y=280)
lblField = Label(win, width=10, text='Field', font=('arial', 15, 'bold'), bg='yellow', fg='black')
lblField.place(x=20, y=220)
# txt
txtName = Entry(win, bd=5, font=('arial', 15, 'bold'), bg='white', fg='black')
txtName.place(x=150, y=100)
txtFamily = Entry(win, bd=5, font=('arial', 15, 'bold'), bg='white', fg='black')
txtFamily.place(x=150, y=160)
txtField = Entry(win, bd=5, font=('arial', 15, 'bold'), bg='white', fg='black')
txtField.place(x=150, y=220)
txtAge = Entry(win, bd=5, font=('arial', 15, 'bold'), bg='white', fg='black')
txtAge.place(x=150, y=280)
# btn
btnRegister = Button(win, text='Register', font=('arial', 20, 'bold'), bg='white', fg='black', width=7)
btnRegister.place(x=185, y=325)
btnRegister.bind('<Enter>', change_button_style_with_hover)
btnRegister.bind('<Leave>', change_button_style_with_hover)
btnRegister.bind('<Button-1>', click_on_register)
# tbl
columns = ('name', 'family', 'field', 'age')
table = ttk.Treeview(win, columns=columns, show='headings')
for i in range(len(columns)):
    table.heading(columns[i], text=columns[i])
    table.column(columns[i], width=120)
table.place(x=450, y=100)
win.mainloop()