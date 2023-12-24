from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()
screen.listen()  # Start listening command for the screen, doesn't matter where you put it, it works.


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def counter_clockwise():
    tim.setheading(tim.heading() + 10)  # Increase the current value by 1


def clockwise():
    tim.setheading(tim.heading() - 10)  # Decrease the current value by 1


def clear():
    screen.resetscreen()  # Reset all Turtles on the Screen to their initial state.
    # tim.home()  # Move turtle to the origin – coordinates (0,0) - not needed


# NOTE: onkey function takes a function with no arguments. See docs.
# Screen is able to detect bcuz it is listening.
# when any of the following key is detected by the screen object, corresponding function is triggered.
screen.onkey(key="w", fun=move_forward)  # How to pass functions to other functions
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
