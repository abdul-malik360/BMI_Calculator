# import tkinter
from tkinter import *

# create a frame or window , whatever you wanna call it
box = Tk()

# name your box
box.title("BMI Calculator")

# give your box a size
box.geometry("800x600")

# give your box a background colour
box.configure(bg="sky blue")

# give your box a background image
# name and call your image
treadmill = PhotoImage(file = "treadmil.png")

# place image
background = Label(box, image=treadmill,).place(x=50, y=50)

# add a heading to your programme and place it
Label(text="Ideal Box Mass Index Calculator", bg="light blue").place(x= 250, y=100)

# give a command and place it
Label(text="Enter your Weight, Height and Gender", bg="light blue").place(x=150, y=250)

# name and put a frame down, add padding as well
input_box = LabelFrame(box, padx=170, pady=100, bg="light blue")
# place the frame
input_box.place(x=50, y=300)

# create a list of options
options = ["select", "Male", "Female"]
# create a variable
var = StringVar(box)
# set variable to the list options
var.set(options[0])
# add labels to your frame
Label(input_box, text="Weight").grid(row=1, column=1)
Label(input_box, text="Height").grid(row=2, column=1)
Label(input_box, text="Gender").grid(row=3, column=1)
Label(input_box, text="kgs").grid(row=1, column=3)
Label(input_box, text="cm").grid(row=2, column=3)
Label(input_box, text="Age").grid(row=3,column=3)
# put entries in frame
Entry(input_box).grid(row=1, column=2)
Entry(input_box).grid(row= 2, column=2)
# add an option menu to your frame
opt = OptionMenu(input_box, var, *options)
# give your menu a width
opt.config(width=15)
# place your option menu
opt.grid(row=3,column=2)







# for the program to work, call this command
box.mainloop()
