from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('image test')

my_img = ImageTk.PhotoImage(Image.open("S.png"))
my_label = Label(image = my_img) # one extra step for placing image 
# image is placed into window as a label
my_label.pack()











button_quit = Button(root,text="Exit",command=root.quit)
button_quit.pack()


root.mainloop()