from tkinter import *

# Layout Manager: pack, place and grid.
# Pack - basically packs each of the widgets next to each other in a vaguely logical format.
# And by default, pack will always start from the top and then pack every other widget just below the previous one.

# Place - places the widgets in the given position. All about precise positioning.

# Grid: Divides the screen into grids of any number of rows and columns. It is relative to other components**.
# NOTE: ** Cant use grid and pack together.


def button_clicked():
    print("I got clicked")
    my_label.config(text=my_entry.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)  # padding - space around the edges

# My Label
my_label = Label(text="I am a label", font=("Arial", 12, "bold"))
# my_label.pack(side="left")
# my_label.place(x=0, y=0)
my_label.grid(column=1, row=1)
# my_label.grid(column=5, row=5) # it will still be at 0,0 if no there object is placed as grid is relative.



# Buttons
my_button = Button(text="Click Me", command=button_clicked)
# my_button.pack(side="left")
# my_button.place(x=10, y=30)
my_button.grid(column=2, row=2)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=3, row=1)

# Entry component
my_entry = Entry(width=30)
my_entry.insert(END, string="some text to write here")
print(my_entry.get())
# my_entry.pack(side="left")
# my_entry.place(x=10, y=60)
my_entry.grid(column=4, row=3)

# To keep the window open
window.mainloop()
