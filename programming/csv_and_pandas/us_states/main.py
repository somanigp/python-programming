import turtle
from turtle import Screen
from name import Name
from scoreboard import Scoreboard
import pandas as pd

data = pd.read_csv("50_states.csv")
# df = data[data.state == "alaska".title()]
# print(int(df.x))  # Calling int on a single element Series is deprecated and will raise a TypeError in the future.
# Use int(ser.iloc[0]) instead

screen = Screen()
screen.title("Guess the States!!")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.bgpic(image)


# def get_mouse_click_coor(x, y):  # to get state coordinates
#     print(x, y)
#
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()

# screen.addshape(image)  # add a custom shape to replace "circle", "square", etc.
# turtle.shape(image)

scoreboard = Scoreboard()

all_states = data.state.to_list()

game_on = True
while game_on:
    user_input = screen.textinput(title=f"{scoreboard.correct_guesses}/{scoreboard.total_guesses} States Correct",
                                  prompt="Whats another states name")
    scoreboard.increase_guess()
    if user_input.lower() == "exit":
        game_on = False

    df = data[data.state == user_input.title()]  # if not such thing found then empty df is returned
    # df.state.item()  # The first element of Series or Index. ie "Alaska", etc
    if not df.empty:
        all_states.pop(all_states.index(user_input.title()))
        x_cor = df.x.to_list()
        y_cor = df.y.to_list()
        scoreboard.increase_correct_guess()
        name = Name(user_input, x_cor[0], y_cor[0])
        name.update()

    if scoreboard.is_over():
        game_on = False


screen.exitonclick()

states_to_learn = "states_to_learn.csv"
dict_to_convert = {
    "states": all_states
}
df_to_convert = pd.DataFrame(dict_to_convert)
df_to_convert.to_csv(states_to_learn)

# new_data = pd.DataFrame(all_states)  # 1 column df as made from a list
# new_data.to_csv(states_to_learn)  # NOTE: col name won't be mentioned
