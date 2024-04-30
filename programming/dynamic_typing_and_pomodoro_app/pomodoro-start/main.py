import math
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# NOTE: If we start 2 times, it will start 2 timer which will overlap, thus we will need to reset twice.
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)  # Stops the current timer.
    canvas.itemconfig(timer_value, text="00:00")
    timer_heading.config(text="TIMER")
    tick_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_time():
    global reps
    reps += 1

    work_sec = 60 * WORK_MIN  # 60 sec * 25 = 25 min.
    short_break = 60 * SHORT_BREAK_MIN
    long_break = 60 * LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break)
        timer_heading.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        # NOTE*** As this is GUI, it will trigger and leave and wont wait for whole function to be over
        print("Will execute timer_heading BREAK just after triggering count_down. Wont wait for func to complete")
        timer_heading.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_heading.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# NOTE :** Recursion can be used to execute a thing a number of time.
# after - Executes a cmd after a time delay. Build in tkinter method
def count_down(count: int) -> None:  # ***Recursion. Calls itself count amount of time, thus count*1000ms amt of delay.
    sec = count % 60
    if sec < 10:  # Checking if a int and setting to a string.
        sec = f"0{sec}"
    minutes = math.floor(count / 60)  # count // 60, meaning if math.floor(4.88) = 4
    if minutes < 10:  # Checking if int and setting it to a string.
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_value, text=f"{minutes}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # At a time only one window.after will be running.
    else:
        # Countdown completes here, note in start_time func when it triggers count_down for the first time,
        # it immediately triggers the next line.
        if reps % 2 != 0:  # When count = 0 and reps is odd means work time just done
            checkmarks = "✔" * ((reps+1) // 2)
            tick_mark.config(text=checkmarks)
        start_time()  # When timer reaches zero calling start_time to get to the next stage.

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)  # By default it will take min size of canvas, thus adding padding.

# def say_somwthing(a, b, c):
#     print(a, b, c)
# window.after(1000, say_somwthing, 3,5,8) # 1000 in ms , say_somwthing is a function. "Hello" is arg to the func.

# Canvas Widget: Layer things one on top of the other.
canvas = Canvas(width=200, height=224, bg=YELLOW,
                highlightthickness=0)  # Will need to fill this canvas with image and so almost the size of the image.
# Canvas is a blank slate; we put images, text, etc. on top of it. highlightthickness is border.
tomato_photo = PhotoImage(file="tomato.png")  # Create an image object.
canvas.create_image(100, 112, image=tomato_photo)  # Putting image on top of canvas. *args are position inside
# canvas.

# Assigning a variable to canvas.create_text so can be used later, it can refer to this particular canvas we wanna change.
timer_value = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# Labels
timer_heading = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))  # 'fg' is foreground color,
# which is text color. font=(FONT_NAME, 25) - font can also be a tuple of 2 if style is not given.
timer_heading.grid(row=1, column=2)

tick_mark = Label(fg=GREEN, bg=YELLOW, pady=20, font=(FONT_NAME, 25, "bold"))
# copy ✔ and paste here. NOTE: **In windows use windows + v for emojis and symbols.
tick_mark.grid(row=4, column=2)

# Buttons
start_button = Button(text="START", fg=RED, font=(FONT_NAME, 10, "italic"), highlightthickness=0, command=start_time)
start_button.grid(row=3, column=1)

reset_button = Button(text="RESET", fg=RED, font=(FONT_NAME, 10, "italic"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=3)

# count_down(5)  # Here as now canvas is defined.

# NOTE ** : we think about a command line program, we were to get our console to do something, print hello, well,
# it's only going to do something when you actually give it an instruction.
# It doesn't really need to keep an eye out for what you might do in between.
# But a graphical user interface is a little bit different.It needs to keep watching the screen to see whether
# if a user clicks on a button. So it's basically going to refresh and keep listening for events.
# And the moment when it does, it's got to react to that event.
# In this case, we tend to call these types of GUI programs event-driven.
#
# And the way that it's driven is through our main loop. So when we set up our window and we start off the main loop,
# it's basically looping through and every millisecond it's checking to see did something happen.
# So that means if we have another loop in our program, it actually won't be able to reach the main loop.
# And in this case, when you actually try to run it, nothing happens. Our program doesn't even launch.

# count = 5  # Counter for 5 sec # THIS THUS DOESN'T WORK
# while count > 0:
#     time.sleep(1)  # 1 sec
#     count -= 1
#     canvas.itemconfig(timer_value, text=f"{count}")


window.mainloop()
