from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
def rb_test():
    value1 = rb1.get()
    print(value1)

# popup message
def popup():
    # showinfo, showwarning, showerror, askquestion, asktocancel, askyesno
    messagebox.showwarning("This is my pop up","hello world")
    messagebox.showinfo("This is my pop up","hello world")
    messagebox.showerror("This is my pop up","hello world")
    response = messagebox.askokcancel("This is my pop up","hello world")
    messagebox.askquestion("This is my pop up","hello world")
    messagebox.askyesno("This is my pop up","hello world")

root = Tk()
root.title('image test')

my_img = ImageTk.PhotoImage(Image.open("D:\CodeDevFolder\PracticeRound\images\S.png"))
my_label = Label(image = my_img) # one extra step for placing image 
 # image is placed into window as a label
my_label.grid(row=0,column=0)

# Adding a status bar and updates dynammically 
# relief = sunken will give a look of the typical status bar
# anchor will place the text in left or right like east of west
status = Label(root, text="image one of five",bd=1,relief=SUNKEN,anchor=E)
# sticky will span the status bar from east to west
status.grid(row = 3,column=0,sticky=W+E)

# adding frames

frame = LabelFrame(root, text="this is my frame",padx=150,pady=5,width=20)
frame.grid(row=2,column=0,padx=25,pady=10)

b2 = Button(frame,text="button 1",pady=5,command=rb_test)
b2.grid(row=0,column=0)





b3 = Button(frame,text="button 2",pady=5,command=popup)
b3.grid(row=2,column=0)

# Radio Button
rb1 = IntVar()
Radiobutton(root, text="Option 1", variable=rb1, value=1).grid(row=4,column=0) # when someone clicks on the this option, variable value will be 1
Radiobutton(root, text="Option 2", variable=rb1, value=2).grid(row=5,column=0)
rb1.get()
print(rb1.get())

button_quit = Button(root,text="Exit",command=root.quit)
button_quit.grid(row=1,column=0)


root.mainloop()