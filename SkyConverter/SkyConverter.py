from tkinter import *
import getpass
import tkinter as tk
from tkinter import filedialog as fd

root = Tk()
root.title("SkyConverter | Конвертор файловых форматов")
root.geometry("1000x800")
root["bg"] = "gray22"

greeting = Label(root, text='Добро пожаловать, ' + getpass.getuser() + '!', font=("Arial Bold", 20), bg="lightgreen")
greeting.pack()

status = Label(root, text='Статус: ', font=("Arial Bold", 20), bg="#FFFF99")
status.place(x=0, y=100)

status_expectation = Label(root, text='Ожидание загрузки файла', font=("Arial Bold", 20), bg="#FF9999")
status_expectation.place(x=110, y=100)

button = Button(root, text="Загрузить файл", font=("Arial Bold", 20), bg="lightgreen")
button.place(relx=0.5, rely=0.5, anchor="c")


# Экран загрузки ниже, нужно зафиксить и соединить
def callback():
    name= fd.askopenfilename()
    print(name)

errmsg = 'Error!'
tk.Button(text='Click to Open File',
       command=callback).pack(fill=tk.X)
tk.mainloop()

root.mainloop()
