# TODO: Structure - Sticks, Ball, Scorecard, Screen (with line in middle)
# Structure is the objects and variables used in a page.

# NOTE: In turtle module, if Screen or Turtle object 'exists' then it is displayed.
from paddle import Paddle
from ball import Ball
from screen import ScreenOfGame
from scoreboard import Scoreboard
import time

# 1. TODO: Create Screen
# Screen object gets created here and Exists. When this class gets initiated Screen class is created.
screen = ScreenOfGame()

# 2. TODO: Create and move a paddle
right_paddle = Paddle(x_axis=350)
# 3. TODO: Create another paddle
left_paddle = Paddle(x_axis=-350)

screen.my_screen.onkey(fun=right_paddle.move_up, key="Up")
screen.my_screen.onkey(fun=right_paddle.move_down, key="Down")

screen.my_screen.onkey(fun=left_paddle.move_up, key="w")
screen.my_screen.onkey(fun=left_paddle.move_down, key="s")

# 4. TODO: Create a ball and make it move
ball = Ball()

# 8. TODO: Keep Score
scoreboard = Scoreboard()

# Game
game_is_on = True
time_of_delay = 0.1
while game_is_on:
    # As we have moved the paddle up, the next update will show that updated paddle location (new location)
    screen.my_screen.update()  # Keep refreshing the screen continuously, now it will capture all the moving of paddles
    time.sleep(time_of_delay)  # To introduce delay
    ball.move_ball()
    # 5. TODO: Detect collision with wall and bounce
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_on_wall()

    # 6. TODO: Detect collision with paddle
    # To include edge case also (meaning distance between ball center and paddle center ~50 during edge collision)
    if ((ball.xcor() > 320 and ball.distance(right_paddle) < 50) or
            (ball.xcor() < -320 and ball.distance(left_paddle) < 50)):
        ball.bounce_on_paddle()
        # Increase speed each time it hits the paddle
        time_of_delay -= 0.01

    # 7. TODO: Detect when paddle misses the ball
    if ball.xcor() > 380:
        ball.recenter()
        ball.bounce_on_paddle()
        time_of_delay = 0.1
        scoreboard.increase_left_score()

    if ball.xcor() < -380:
        ball.recenter()
        ball.bounce_on_paddle()
        time_of_delay = 0.1
        scoreboard.increase_right_score()


screen.my_screen.exitonclick()
