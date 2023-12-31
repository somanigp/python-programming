import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


def level_up_speed():
    global MOVE_DISTANCE
    MOVE_DISTANCE = MOVE_DISTANCE + MOVE_INCREMENT


class CarManager:
    def __init__(self):
        self.car_collection = []
        self.generate_car()

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=290, y=random.randint(-250, 250))
            new_car.setheading(180)  # First set heading and then reshape. Thus stretch height
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            self.car_collection.append(new_car)

    def move_cars_forward(self):
        for car in self.car_collection:
            car.forward(MOVE_DISTANCE)
