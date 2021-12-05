from tkinter import *
import getpass


root = Tk()
root.title("SkyConverter | Конвертор файловых форматов")
root.geometry("1000x800")
root["bg"] = "gray22"

label = Label(root, text='Добро пожаловать, ' + getpass.getuser() + '!', font=("Arial Bold", 20), bg="lightgreen")



label.pack()
root.mainloop()