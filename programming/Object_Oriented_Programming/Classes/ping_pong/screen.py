from turtle import Screen


class ScreenOfGame:
    def __init__(self):
        # Note my_screen variable (attribute here) stores the actual Screen object, so will need to make changes to
        # that attribute to change Screen object properties.
        # This class will also create a screen object, modify it and give it to user. If user wants to do further change
        # it will need to access the object through my_screen attribute.
        self.my_screen = Screen()
        self.my_screen.setup(width=800, height=600)
        self.my_screen.bgcolor("black")
        self.my_screen.title("!!Ping Pong!!")
        self.my_screen.listen()
        self.my_screen.tracer(0)
