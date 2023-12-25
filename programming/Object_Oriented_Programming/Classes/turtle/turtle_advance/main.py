# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors
import turtle
# Different ways to Import Modules.
# 1.    Basic Import: import turtle
# 2.    from ... import ... : from turtle import Turtle
# 3.    from turtle import * # Import all, not used much, as it makes it difficult to understand where are methods and
# classes coming from
# **4.  Alias modules: import turtle as t # t is alias name, used as tim = t.Turtle()
# **5.  There are some modules you just cant import as they are not packaged with a python standard library, then
# Installing Modules come in. Install from PyPi. in Interpreter Settings.

# This module helps draw graphics onto the screen
from turtle import Turtle, Screen  # One module/package can have many classes to import
import heroes as h  # Gives a suggestion to install the package.
import random
hero_name = h.gen()
# print(hero_name)

# turtle.colormode(255)  # Can you package_name like this when you have from turtle import Turtle, Screen
timmy_the_turtle = Turtle()  # Created a Turtle object, and will work with this object
timmy_the_turtle.shape("turtle")  # method to change the shape of the object, to change its shape attribute
timmy_the_turtle.color("red")
timmy_the_turtle.pencolor("black")  # border
# timmy_the_turtle.forward(100)

# NOTE:
# Colors can be represented as color(colorstring), color((r,g,b)), color(r,g,b). Basically CSS name, hex code, or
# RGB values.
# This package is using pencolor method to set the color which relies on Tk color specification string.
# Tk -> tkinter which is the tk interface, which is one of the ways to use Python to create GUI (Graphical User
# Interface)
# So turtle module relies on tkinter to create graphics under the hood.

# Challenges : Used docs for this.
# for _ in range(4):  # Square # We just want to repeat it 4 times, so used '_'.
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)  # 90 degree angle input

# for i in range(50):  # Dashed Line
#     if i % 2 != 0: # To start the dashed line with a black line
#         timmy_the_turtle.pencolor("white")  # pencolor is color of ink it leaves behind
#     else:
#         timmy_the_turtle.pencolor("black")
#     timmy_the_turtle.forward(10)

# for _ in range(15):  # Dashed Line
#     timmy_the_turtle.forward(10)  # NOTE: When it shows (self,distance) -> it means it only takes one argument
#     timmy_the_turtle.penup()  # Stops writing as pen is up
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# The {:02x} is a string formatting specifier in Python that is used for formatting hexadecimal numbers.
# 02: Specifies the minimum width of the formatted string. And x: Indicates the format type. In this case,
# it specifies that the number should be formatted as a lowercase hexadecimal value.
# {:02x} formats an integer as a lowercase hexadecimal string.
# number = 10
# hex_string = "{:02x}".format(number)
# print(hex_string)  # Output: "0a"


def generate_random_color():
    """Returns a hex code formatted random color"""
    # Generate random values for R, G, B components - RGB representation is not in hex code.
    red = random.randint(0, 255)  # randint includes 255 also.
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # Create hexadecimal color representation
    # RRGGBB format , eg : #696969 , here RR,GG,BB are all in hexa decimal.
    color_hex = "#{:02x}{:02x}{:02x}".format(red, green, blue)  # Use python console to try things out
    return color_hex


def draw_shape(sides, turtle_object: Turtle):  # turtle_object can only be of type/class Turtle
    random_color = generate_random_color()
    turtle_object.pencolor(random_color)
    angle = 360 / sides  # Outer angle of each side.
    for _ in range(sides):  # for no_of_sides=3 , range[0,1,2] , so len(range) = 3
        turtle_object.forward(50)  # can directly use timmy_the_turtle.forward(50), but not good practice.
        turtle_object.left(angle)  # 180-60 or 360/3, that is turn by outer angle.


# no_of_sides = 3
# while no_of_sides < 10:
#     draw_shape(no_of_sides, timmy_the_turtle)
#     no_of_sides += 1

# Both of below options work. ***
# dic = {"forward": timmy_the_turtle.forward(50)}
# x = dic["forward"]
# x

# dic = {"forward": timmy_the_turtle.forward}
# x = dic["forward"]
# x(50)

# Random Walk - Used in maths and coding, in various places to model real life situations. Like liquid movement, etc.
# https://en.wikipedia.org/wiki/Random_walk
def right_movement(turtle_object, distance):
    turtle_object.right(90)
    turtle_object.forward(distance)


def left_movement(turtle_object, distance):
    turtle_object.left(90)
    turtle_object.forward(distance)


def forward_movement(turtle_object, distance):
    turtle_object.forward(distance)


def backward_movement(turtle_object, distance):
    turtle_object.backward(distance)


directions = ["right", "left", "forward", "backward"]
dict_of_directions = {
    "right": right_movement,  # No need to add parenthesis as it is a function as an argument here.
    "left": left_movement,
    "forward": forward_movement,
    "backward": backward_movement
}


def random_walk(dist, turtle_object, no_of_times):
    """Random Walk Function"""
    while no_of_times > 0:
        random_color = generate_random_color()
        turtle_object.pencolor(random_color)
        # NOTE: func becomes right_movement, etc. functions and thus can take parameter.
        direction = random.choice(directions)
        func = dict_of_directions[direction]
        func(turtle_object, dist)
        no_of_times -= 1


timmy_the_turtle.pensize(7)  # Setting size/width of strokes
timmy_the_turtle.speed(10)  # Setting speed
random_walk(20, timmy_the_turtle, 10)

# As the screen doesn't stay on, we need to use the Screen function which returns the singleton screen object if none
# exists for us to work with
my_screen = Screen()
my_screen.exitonclick()  # The Screen will only go away on click
