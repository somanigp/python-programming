# Instead of initialing attributes of food with a Turtle object like we did for snake class. We use inheritance and get
# food to be a subclass of turtle. NOTE: snake and food are Turtle classes, as their body/or they are made of Turtle.
# Only fact that snake requires 3 Turtle objects that's why it didn't inherit.
# This piece of food is a Turtle object. So a food object will have all the qualities of Turtle object plus more.
from turtle import Turtle  # Imports should always be on top.
from random import randint
FOOD_COLOR = "#C6A969"


class Food(Turtle):

    # Food class will try to render itself as a small circle on screen randomly and so forth.
    def __init__(self):
        super().__init__()
        self.shape("circle")  # The 'self' -> subclass of Turtle. So can use all its methods and attributes
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # stretch the circle to 10x10 (reducing it)
        self.color(FOOD_COLOR)
        self.speed("fastest")  # Don't have to see the animation being created
        # NOTE: Each time a new Food item is created when a snake eats one. One food item is not moving
        # from place to place.
        # self.goto(x=randint(-280, 280), y=randint(-280, 280))  # At random place should spawn on the map
        # Changing the way: the same food goes to another random location
        self.refresh()

    def refresh(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 280))



