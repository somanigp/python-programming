# GUI - Graphical User Interface and one the ways is python uses tk interface to create GUI.

# import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Main code goes here
# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
my_label = Label(text="I am a label", font=("Arial", 12, "bold"))
my_label.pack()  # To display any component on the window : Using packer to pack our label to the screen
# he packer is one of Tk’s geometry-management mechanisms. A simple way to layout components.

# from turtle import Turtle
# tim = Turtle()
# tim.write() # All the arguments are listed in defination. Only text is required. Others are Optional and have a default value

# Commands for tkinter : https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
# PyDocs : https://docs.python.org/3/library/tkinter.html#setting-options
my_label["text"] = "New Text"
my_label.config(text="New Text 2")


def button_clicked():
    print("I got clicked")
    my_label.config(text=my_entry.get())  # Now at this time my_entry.get() will return the text as a string
    # as the value is there
    # my_label["text"] = "Button got clicked"


# Buttons
my_button = Button(text="Click Me to print text", command=button_clicked)  # When the button detects an click event it calls
# the button_clicked function. The function is passed as an argument.
my_button.pack()

# Entry component
my_entry = Entry(width=30)
my_entry.insert(END, string="some text to write here")  # Add some text to begin with.
print(my_entry.get())  # to get the current text in my_entry
my_entry.pack()
# my_entry.get() # To get the text(as a string) from the entry - but here at the time it will be executed there
# will be no entry
# my_entry.insert(0, "Enter your name here") # insert at an index position, ** can execute after pack

# Text
text = Text(height=5, width=30) # Large area where user can edit
# Puts cursor in textbox. Scroll inside text.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")  # END - tkinter constant - represents last character
# inside the entry.
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))  # 1.0 is line 1, character 0 till the END - get all text
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)  # It passes over a value to the function which is called, in
#   This case it is scale_used. Thus scale_used has one parameter.
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()  # Construct an integer variable. A class of tkinter.
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# To keep the window open
window.mainloop()
