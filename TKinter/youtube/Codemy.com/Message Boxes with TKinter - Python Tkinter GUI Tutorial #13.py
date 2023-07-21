# https://www.youtube.com/watch?v=GLnNPjL1U2g
# https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course.git
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('codemy.ico')
root.geometry("400x400")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my popup!", "hello world")
    if response == 1:
        Label(root, text="you Clicked yes").pack()
    else:
        Label(root, text="you Clicked no").pack()


Button(root, text="Click Me!", command=popup).pack()

root.mainloop()
