# https://www.youtube.com/watch?v=GLnNPjL1U2g
# https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course.git
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('codemy.ico')
root.geometry("400x400")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir=".", title="Select A File", filetypes=(("ico files", "*.png"),))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()
