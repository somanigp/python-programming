from tkinter import *
import pandas as pd
import random

COUNT = 3
BACKGROUND_COLOR = "#B1DDC6"
count_down_timer = None
current_card = {}

# Importing CSV
try:
    with open("./data/words_to_learn.csv") as data_file:
        data = pd.read_csv(data_file)
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")

to_learn = data.to_dict(orient="records")  # List of dicts
# print(to_learn)  # [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}]


def guessed_wrong():
    global to_learn, current_card
    to_learn.remove(current_card)
    print(len(to_learn))
    data_to_put = pd.DataFrame(to_learn)
    data_to_put.to_csv("./data/words_to_learn.csv", index=False)  # Operation : write, each time, overrides last file.
    next_card()


# Functions
def next_card():
    # if count_down_timer is not None:  # This can be used too.
    try:
        window.after_cancel(count_down_timer)
    except ValueError:
        pass
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(title, text="French", fill="black")  # Fill used to change text color in canvas.
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    count_down(COUNT)


def count_down(count):
    # print(count)
    if count > 0:
        global count_down_timer
        count_down_timer = window.after(3000, count_down, count-3)  # sending multiple inputs
    else:  # Use else as it triggers window.after and then goes below as it is a graphical interface,
        # and doesn't wait for the function.
        global current_card
        canvas.itemconfig(card_image, image=card_back_image)
        canvas.itemconfig(title, text="English", fill="white")
        canvas.itemconfig(word, text=current_card["English"], fill="white")


# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)


# Components
# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)

title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=1, column=1, columnspan=2)

# Buttons
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=guessed_wrong)
wrong_button.grid(row=2, column=1)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=next_card)
right_button.grid(row=2, column=2)

# Called here so that first card is the card below.
next_card()

# Mainloop
window.mainloop()
