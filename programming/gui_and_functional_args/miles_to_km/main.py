from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
# window.minsize(width=300, height=150) - Not needed for compact GUI
window.config(padx=20)

my_entry = Entry(width=15)
my_entry.grid(row=1, column=2)

miles_label = Label(text="Miles")
miles_label.grid(row=1, column=3)

to_km = ""


def convert_to_km():
    global to_km
    if my_entry.get() == "":
        return
    to_km = round(float(my_entry.get())*1.60934, 3)  # 1.60934 is the conversion factor and .get() returns string
    km_value_label.config(text=f"{to_km}")


km_label = Label(text="is equal to")
km_label.grid(row=2, column=1)

km_value_label = Label(text=f"{to_km}")
km_value_label.grid(row=2, column=2)

km_ = Label(text="Km")
km_.grid(row=2, column=3)

button = Button(text="Calculate", command=convert_to_km)
button.grid(row=3, column=2)
window.mainloop()
