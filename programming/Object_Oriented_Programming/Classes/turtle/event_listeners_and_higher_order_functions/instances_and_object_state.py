# Multiple instances of the same class
from turtle import Turtle, Screen
import random

# We can create multiple objects tim, tommy from the same class Turtle.
# Each object will function completely independent of each other,
# So they are each a separate instance, at any time they can have different attributes.
# As each object at a given time can have a diff set of attributes or performing diff functions - this is
# known as 'state' of the object
# tim = Turtle(shape="turtle")
# tommy = Turtle()
screen = Screen()
screen.setup(width=500, height=400)  # Setting screen size
# In screen height = 400, so y-axis goes from 200 to -200
# In screen width = 500, so x-axis goes from 250 to -250
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False
user_choice = screen.textinput(title="Turtle Race", prompt="Which color will win?")
# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-100)  # Move turtle to a coordinate.

y_axis = -100
list_of_turtles = []  # When we need to create multiple objects and work with them, put them in a list.
# Add the first object and you can work on it.
# NOTE: ** Creating multiple objects and operating on them.
for i in range(6):
    list_of_turtles.append(Turtle(shape="turtle"))  # creating a new Turtle object and storing object in a list
    turtle_is = list_of_turtles[i]  # using object just stored in a list
    turtle_is.color(colors[i])  # putting each with a diff color from 'colors' list
    turtle_is.penup()  # permanently up
    turtle_is.goto(x=-230,y=y_axis)
    y_axis += 30  # placing the next turtle above a bit.

# This works too, as each time a new Turtle object is created ,
# then 'that' same object is stored in a variable 'tim'
# Now that object is assigned a color and taken to a position
# y_axis = -100
# So for each for loop a new object is created , object is created first and then assigned a variable.
# Also when object1 is created and taken to y_axis = -100, then it is its state ,
# so when object2 is created , object1 state doesnt change and have a different state.
# for i in range(6):
#     tim = Turtle("turtle")
#     tim.color(colors[i])
#     tim.penup()
#     tim.goto(x=-230, y=y_axis)
#     y_axis += 30

if user_choice:  # NOTE: To check if user_choice exists.
    is_race_on = True

who_won = -1
while is_race_on:  # Keep moving all turtles forward again and again.
    for i in range(6):
        turtle_is = list_of_turtles[i]  # Current turtle
        turtle_is.forward(random.randint(1, 10))  # While race is on current turtle in the list moves
        # random steps forward
        # xcor gives current x-coordinate of the turtle after it has moved forward
        if turtle_is.xcor() > 250:  # Check if the current turtle crossed finish line which is x = 250, when any of
            # the turtle crosses, game ends.
            who_won = i  # Storing the index of turtle who won, color index and turtle index are correspondingly.
            is_race_on = False  # end the race
            break  #

if user_choice == colors[who_won]:  # color index and turtle index are correspondingly.
    print(f"You Won, The winner is {colors[who_won]}")
else:
    print(f"You Lose, The winner is {colors[who_won]}")

# The state of color attribute of tim is green and so forth.
# tim.shape("turtle")
# tim.color("green")
# tim.forward(100)


screen.exitonclick()
