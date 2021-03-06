# Abdul-Malik Mohamed
# import tkinter
from tkinter import *

# create a frame or window , whatever you wanna call it
box = Tk()

# name your box
box.title("BMI Calculator")

# give your box a size
box.geometry("640x600")

# give your box a background colour
box.configure(bg="sky blue")

# give your box a background image
# name and call your image
treadmill = PhotoImage(file = "treadmil.png")

# place image
background = Label(box, image=treadmill,).place(x=50, y=50)

# create variables for entry boxes
bmi = StringVar()
ideal = StringVar()
w_ent = StringVar()
h_ent = StringVar()
a_ent = StringVar()
s_res = StringVar()


# add a heading to your programme and place it
Label(text="Ideal Box Mass Index Calculator", bg="sky blue").place(x= 250, y=100)

# give a command and place it
Label(text="Enter your Weight, Height, Gender and Age", bg="sky blue").place(x=150, y=250)

# name and put a frame down, add padding as well
input_box = LabelFrame(box, padx=50, pady=30, bg="light blue")
# place the frame
input_box.place(x=50, y=300)


# add labels to your frame, give it a background color and place them
Label(input_box, text="Weight: ", bg="light blue").grid(row=1, column=1)
Label(input_box, text="Height: ", bg="light blue").grid(row=2, column=1)
Label(input_box, text="Gender: ", bg="light blue").grid(row=3, column=1)
Label(input_box, text="kgs", bg="light blue").grid(row=1, column=3)
Label(input_box, text="cm", bg="light blue").grid(row=2, column=3)
Label(input_box, text="Age: ", bg="light blue").grid(row=3,column=3)
# name your entries, put entries in frame and place them
weight = Entry(input_box)
weight.grid(row=1, column=2)
height = Entry(input_box)
height.grid(row=2, column=2)
# Disabling the age entry
age = Entry(input_box, state=DISABLED)
# placing the age entry
age.grid(row=3, column=4)

# create a list of options
options = ["Male", "Female"]
# create a variable for your options
var = StringVar(box)
# setting display value of options
var.set("Select Gender")


# defining function of the options
def select(var):
    if var != "Female":
        # can either use "disabled" or DISABLED
        age.config(state=DISABLED)
    elif var == "Female":
        age.config(state=NORMAL)
        # when clicking on female move cursor to age entry
        age.focus()


# add an option menu to your frame
opt = OptionMenu(input_box, var, *options, command=select)
# give your menu a width and a background color
opt.config(width=15,bg="light blue")
# place your option menu
opt.grid(row=3,column=2)


# defining the function of the calculating bmi button
def calculate():
    if var.get() == "Male":
        bmi_calc = int(weight.get()) / (int(height.get()) / 100) ** 2
        bmi.set(bmi_calc)
        ibmi_calc = (0.5 * float(weight.get()) / (float(height.get()) / 100) ** 2) + 11.5
        ideal.set(ibmi_calc)
    elif var.get() == "Female":
        bmi_calc = int(weight.get()) / (int(height.get()) / 100) ** 2
        bmi.set(bmi_calc)
        ibmi_calc = (0.5 * float(weight.get()) / (float(height.get()) / 100) ** 2) + (0.03 * float(age.get())) + 11
        ideal.set(ibmi_calc)

    # define size of the gym member
    if int(float(bmi.get())) < 18:
        s_res.set("skinny")
    elif int(float(bmi.get())) >= 18 and int(float(bmi.get())) < 25:
        s_res.set("Normal")
    elif int(float(bmi.get())) >= 25 and int(float(bmi.get())) < 30:
        s_res.set("Chubby")
    elif int(float(bmi.get())) >= 30:
        s_res.set("Fat")


# create a button to calculate BMI, give it a color and place it
Button(box, text="Calculate your Ideal BMI", bg="light blue", command=calculate).place(x=220, y=450)
# add result labels and result boxes to your box and not the frame and place them
# result labels
Label(box, text="BMI: ", bg="sky blue").place(x=50, y=500)
Label(box, text="Ideal BMI: ", bg= "sky blue").place(x=300, y=500)
# result boxes
answer_bmi = Label(box, textvariable=bmi, width=20).place(x=100, y=500)
ideal_bmi = Label(box, width=20, textvariable=ideal).place(x=390, y=500)


Label(box, text="You are:", bg='sky blue').place(x=250, y=530)
size = Label(box, width=20, bg='sky blue', textvariable=s_res ).place(x=200, y=560)



# defining function of the clear button
def clear_entries():
    weight.delete(0, END)
    height.delete(0, END)
    age.delete(0, END)
    var.set("Select Gender")
    bmi.set("")
    ideal.set("")
    s_res.set("")


# clear button and place it, give a color as well
Button(box, text="CLEAR", bg="light blue", command=clear_entries).place(x=50, y=550)


# defining function of the exit button
def close_box():
    box.destroy()


# add exit button, give a background color add command and place it
Button(box, text="EXIT", bg="light blue", command=close_box).place(x=390, y=550)


# for the program to work, call this command
box.mainloop()
