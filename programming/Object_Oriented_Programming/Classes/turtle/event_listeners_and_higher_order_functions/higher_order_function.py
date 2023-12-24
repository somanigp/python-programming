# Using Frameworks or Libraries: Many Python libraries and frameworks have built-in functionality for event handling
# and listeners.
# Tkinter, PyQt or PySide (Qt), Django/Flask
# Event Listeners: A way to listen to what a user does, like if a user taps a specific key on a keyboard. Each library
# has its own methods for us to implement this.

# listen: Allows the turtle Screen to start listening and waiting for events that the user might trigger, like key,
# presses, etc.
from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()


def move_forward():
    tim.forward(10)

# Start listening.
my_screen.listen()  # The screen object needs to start listening
# After it starts listening, we need to bind a function which gets triggered when we press a key in keyboard.
# We bind a keystroke to an event with help of event listener.

# NOTE: When using methods you didn't create use keyword arguments instead of positional
# onkey -> expects a function with NO Arguments and a key
my_screen.onkey(key="space", fun=move_forward)  # NOTE: When a function is passed as an argument, so something that
# Is going to be passed into another function, we don't add the parentheses at the end.
# ** The parentheses trigger the function to happen there and then.
# We want it to trigger the function when event takes place.

# Function as input :
# When we pass the function as an input we only pass the name and not the parenthesis at the end.

def hello_func():
    print("Hello")
def add(n1,n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2


# Higher Order Function : A function which can take other functions as input.
def calculate(n1, n2, func, hello_func_replaced): # This is a higher order function
    # A function is passed in place of func and called through func and whatever parameters it need.
    print(func(n1,n2))  # func becomes add/subtract depending on input
    hello_func_replaced()  # hello_func is passed for this.


calculate(1,2, add, hello_func)  # Here we are passing add function, thus with no ().
# Even when functions are passed in dictionaries or list , they are passed without a parenthesis


# The screen objects will detect which key is pressed and accordingly act.
my_screen.exitonclick()

