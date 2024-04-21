# https://docs.python.org/3/library/turtle.html
# This is preloaded with every download of Python

from turtle import *  # To import all the things from turtle module we use * . This is one of the external

timmy = Turtle()  # C - shows to represent class , timmy is object , parenthesis () is added to construct an
# object as constructor is also a function with the same name as class name. We have fetched a class Turtle from
# module turtle

print(timmy)  # <turtle.Turtle object at 0x000001586693E330> Turtle object from turtle module saved at
# 0x000001586693E330 location in memory.
timmy.shape('turtle')
my_screen = Screen()  # Another object created
print(my_screen.canvwidth)  # Accessing the attribute/properties of an object , from object my_screen get this
# attribute. Attribute s shown by 'f'
timmy.color('green')  # Methods denoted by 'm'
timmy.forward(100)

for steps in range(10):
    for c in ('blue', 'red', 'green'):
        timmy.color(c)  # Function/Methods for turtle object
        timmy.forward(steps)
        timmy.right(30)

my_screen.exitonclick()  # Accessing a method/function tied to this object or of this object

# We can change the object's attributes, object and class attributes are different. Same as object and class methods
# are different.
# object's attributes can be modified.
