from turtle import Turtle
# Defining constants
SNAKE_COLOR = "#4F6F52"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        # NOTE: Calling this function during the initialization of object. Below function is executed when
        # function is called.
        self.initialize_body()  # Initialize body with 3 Turtle objects.
        self.head = self.snake_body[0]

    def initialize_body(self):
        """Method to create starting snake body, adding 3 Turtles"""
        x_axis = 0
        y_axis = 0
        for i in range(3):  # Creating 3 parts of the initial snake body
            self.snake_body.append(Turtle("square"))
            snake_part = self.snake_body[i]
            snake_part.penup()
            snake_part.color(SNAKE_COLOR)
            # snake_part.speed(0)  # Setting the speed. 3 for slow, 1 for slowest, 0 fastest and 10 fast.
            snake_part.goto(x=x_axis, y=y_axis)  # NOTE **: Setting the x,y coordinates it irrespective of
            # Screen been there or not, these are the attributes of Turtle class which we can set on any Turtle object,
            # anywhere. And when the screen is available to the object, it will show there.
            x_axis -= 20  # The length of each square is 20. So each should be 20 units behind the next.
            # See image attached.

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color(SNAKE_COLOR)
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extend(self):
        """Add a new snake_part to the snake"""
        # As move() is called at this point, it won't give any errors.
        self.add_segment(self.snake_body[-1].position())  # -1 : index of last element, position() - gives x,y co-or.

    def reset(self):
        for snake in self.snake_body:
            snake.goto(x=1000, y=1000)
        self.snake_body.clear()  # Clear a list in python, note the objects don't get deleted; they just get removed
        # or ejected from the list, thus need to relocate the object outside the screen before ejecting them.
        self.initialize_body()  # Initialize body with 3 Turtle objects.
        self.head = self.snake_body[0]  # resetting the head

    def move(self):
        """Method to move snake forward by 20 units, only once."""
        # Starting from the end and moving each part forward. Last part to second last and so on.
        # Tail follows the head.
        for snake_part_num in range(len(self.snake_body) - 1, 0, -1):
            # Positions were fixed during initialization and when adding parts
            x_cor = self.snake_body[snake_part_num - 1].xcor()
            y_cor = self.snake_body[snake_part_num - 1].ycor()
            self.snake_body[snake_part_num].goto(x=x_cor, y=y_cor)
        # Then moving the head forward
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        """Heads moves right, so rest of snake will follow later"""
        if int(self.head.heading()) == LEFT:  # If it is facing left, then snake cant directly turn right
            # in opp. direction
            return  # returns nothing and the method ends.
        self.head.setheading(RIGHT)

    def up(self):
        """Heads moves up, so rest of snake will follow later"""
        if int(self.head.heading()) == DOWN:
            return
        # Only need to change the angle of the head of the snake and rest will follow, as tail is following
        # head when it is moving,
        # The snake doesn't need to stop moving, now head will move upwards
        self.head.setheading(UP)

    def left(self):
        """Heads moves left, so rest of snake will follow later"""
        if int(self.head.heading()) != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """Heads moves down, so rest of snake will follow later"""
        if int(self.head.heading()) == UP:
            return
        self.head.setheading(DOWN)
