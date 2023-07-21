# https://www.youtube.com/watch?v=GLnNPjL1U2g
from tkinter import *

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('')
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)


def our_command():
    Label(root, text="You clicked a Dropdown Menu").pack()


file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(labe="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(labe="Exit", command=root.quit)


option_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=option_menu)
option_menu.add_command(labe="Cut", command=our_command)
option_menu.add_command(labe="Copy", command=our_command)


option_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=option_menu)
option_menu.add_command(labe="Find", command=our_command)
option_menu.add_command(labe="Find Next", command=our_command)

root.mainloop()
