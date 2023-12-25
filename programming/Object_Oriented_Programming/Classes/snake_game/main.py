# To solve any complex problem, the first step is to divide/break it into small problems
# TODO:  Create a snake body ( 3 squares on the screen lined up next to each other )
# TODO:  How to move the snake forward ( it only moves forward and we just change direction.
# TODO:  How to control the snake using keyboard
# TODO:  Detect collision with food
# TODO:  Create scoreboard
# TODO:  When game should end ( collision with wall )
# TODO:  When game should end ( snake collided with its own tale )

from turtle import Turtle, Screen
import time
from snake import Snake  # Importing snake class
# time.sleep(delay_in_secs) # Adds delay

SCREEN_COLOR = "#D2E3C8"
# SNAKE_COLOR = "#4F6F52"
FOOD_COLOR = ""

# Screen Setup
my_screen = Screen()
my_screen.setup(width=600, height=600)  # Size of screen
my_screen.bgcolor(SCREEN_COLOR)  # set background for the screen, refer here for color hex code: https://colorhunt.co/
my_screen.title("Welcome to the Snake Game!!")  # Title of the screen, GUI that comes up
my_screen.tracer(0)  # Turn turtle animation on(1)/off(0). Here using function to do only this. Here 0 -> off.
# From now, we will us update to perform a TurtleScreen update. To be used when tracer is turned off.
# Update shows the 'then' state of the screen. So we move the turtle by continuously showing different states
# of the turtle.

# NOTE: All parts related to snake behavior and appearance, move it to a separate class.
# snake object creation
snake = Snake()

# Enable Listener
my_screen.listen()

# Bindings: Function to Arrow Keys
# Only need to change the angle of the head of the snake and rest will follow, as tail is following
# head when it is moving
# The snake doesn't need to stop moving, only head will change direction.
my_screen.onkey(fun=snake.up, key="Up")  # 'up' is a function passed without a parenthesis, as its passed as arg.
my_screen.onkey(fun=snake.down, key="Down")
my_screen.onkey(fun=snake.left, key="Left")
my_screen.onkey(fun=snake.right, key="Right")


# Creating initial snake - 3 Turtle("square") object. Each is 20x20.
# x_axis = 0
# y_axis = 0
# snake = []
# for i in range(3):  # Creating 3 parts of the initial snake body
#     snake.append(Turtle("square"))
#     snake_part = snake[i]
#     snake_part.penup()
#     snake_part.color(SNAKE_COLOR)
#     # snake_part.speed(0)  # Setting the speed. 3 for slow, 1 for slowest, 0 fastest and 10 fast.
#     snake_part.goto(x=x_axis, y=y_axis)
#     x_axis -= 20  # The length of each square is 20. So each should be 20 units behind the next. See image attached.

# my_screen.update()  # Showing 1st state/ 1st image -> initial position of turtle. -> First step in while loop,
# so not needed here.

# Make sure the snake continuously moves forward
game_on = True

# Make it work as TVs, GIF -> show image by image. So that way it looks like the whole snake is moving together.
# Also note, we don't have to move all the segments forward - then will be impossible to turn.
# We need to only move head (1st segment forward), the rest should take place (go to the position) of the segment
# in front of them. Like how actual snake moves

# Initialize element
# new_position = tuple(snake[0].pos())  # Position of snake's head (1st element). And converting it to tuple
# print(tuple(position))  # (0,0)

# NOTE: My Logic
# while game_on:
#     my_screen.update()  # Image after moving all the snake parts forward - this will be rendered.
#     time.sleep(0.3)  # Delay is needed here, or else noting shows on screen, as the processing speed is very fast,
#     # using tracer and update increases image rendering (Can be used to accelerate the drawing of complex graphics.)
#     for i in range(len(snake)):
#         # snake[i].forward(1)  # see gaps on the screen if we increase it above 1. This is bcuz we see each piece
#         # move to a new location and then the next piece moves.
#         if i == 0:
#             # Heads current position, which 2nd part will replace
#             new_position = tuple(snake[i].pos())  # setting position to head's location before it moves so
#             # All 3 don't overlap on each other. Also note head doesn't have to worry about position as it will
#             # always move forward and not dependent on pos of any part.
#
#             # Move the head forward always
#             snake[i].forward(20)  # Move head forward by 20. And show the image after moving all the parts.
#         else:
#             # The 2nd snake_part will take this position of head
#             x_axis, y_axis = new_position
#             # storing the 2nd snake_part location to later pass to 3rd
#             old_position_of_current_part = tuple(snake[i].pos())
#             # Moving the 2nd part to head's location
#             snake[i].goto(x=x_axis, y=y_axis)
#             # old_position_of_current_part will be the new_position of the next snake_part.
#             new_position = old_position_of_current_part
#           # Repeat it till all the tail (body except head) also moves forward and takes place of the part ahead of it.

# Move the snake forward. - Tail follows the head.
while game_on:
    # Delay for 0.1 sec and refresh the screen
    my_screen.update()
    time.sleep(0.1)
    snake.move()  # Method to move snake forward by 20 units, only once


my_screen.exitonclick()  # NOTE: Only exits when no more command to execute on turtle.
