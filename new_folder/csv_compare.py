import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
from PIL import Image, ImageTk


def window():
    root = tk.Tk()
    root.title('Wagner CSV-Vergleicher')
    root.geometry('500x300')

    image = Image.open("../logo-white-negativ.png")
    photo = ImageTk.PhotoImage(image)

    #root.minsize(width=200, height=200)
    #root.maxsize(width=800, height=800)
    root.resizable(width=False, height=False)

    label1 = ttk.Label(root, image=photo, padding=50)
    label1.pack()

    label2 = ttk.Label(root, text='CSV #1', font='Arial')
    label2.pack(side='left', expand=True)

    label3 = ttk.Label(root, text='CSV #2', font='Arial')
    label3.pack(side='left', expand=True)

    #open_file = filedialog.askdirectory()

    root.mainloop()


# https://www.youtube.com/watch?v=zEBmvpqCXdE
window()

"""
with open('old.csv', 'r') as t1, open('new.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
"""
