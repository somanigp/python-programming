import time
from turtle import Screen
from player import Player
from car_manager import CarManager, level_up_speed  # NOTE: class and filename convention
from scoreboard import Scoreboard

# Setting Screen
screen = Screen()  # NOTE: You can return any data type or object.
screen.setup(width=600, height=600)
screen.bgcolor("#F8FAE5")
screen.title("The Turtle Crossing!!")
screen.tracer(0)
screen.listen()

# Player
player = Player()
screen.onkey(fun=player.move_forward, key="Up")

# Scorecard
scoreboard = Scoreboard()

# Car_Manager
car_manager = CarManager()

game_is_on = True
delay_time = 0.1
while game_is_on:
    time.sleep(delay_time)
    screen.update()
    car_manager.generate_car()

    # Move the cars forward after generation.
    car_manager.move_cars_forward()

    # Level Up
    if player.reached_finish_line():  # returns True or False
        level_up_speed()
        player.restart_position()
        scoreboard.increase_sore()

    # Collision with a car and Game Over
    for car in car_manager.car_collection:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
