# https://www.youtube.com/watch?v=GLnNPjL1U2g
from tkinter import *

root = Tk()
root.title('Codemy.com')
root.iconbitmap('')
root.geometry("400x400")


def clicker(event):
    myLabel = Label(root, text="You clicked a button: " + event.char)
    myLabel.pack()


myButton = Button(root, text="Click Me")
myButton.bind("<Key>", clicker)
myButton.pack(pady=20)

root.mainloop()
