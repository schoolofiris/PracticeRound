# from tkinter import *
# from tkinter import ttk
# root = Tk(screenName="schoolofiris.org")
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

import tkinter as tk
from PIL import Image, ImageTk
print ("is this working?")

root = tk.Tk()
# all the codes will be between root tk.Tk and root.mainloop
canvas = tk.Canvas(root,width = 600, height = 300)
canvas.grid(columnspan=3)

logo = Image.open(r"D:\\PythonDevFolder\\practice files\\tkinter_gui_test\\logo7.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=3,row=1)

root.mainloop()