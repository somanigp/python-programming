import random
import turtle as tur
import colorgram  # Package to extract color from an image.

# Python Tuples - ordered and immutable, cant remove or change after creation

tuple_one = (1, 2, 3)
print(tuple_one[0])

# Change tuples, convert to list -> make changes -> revert back.
list_one = list(tuple_one)
list_one[0] = 10
tuple_one = tuple(list_one)
print(tuple_one)

# Colors: (r, g, b)
tim = tur.Turtle()
tur.colormode(255)  # Setting on pacakge name, and not on object. Also set this so Turtle objects can have pencolor in
# rgb


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b  # This is also a tuple.


tim.speed("fastest")
# angle = 1
# for _ in range(100):
#     tim.color(random_color())
#     tim.circle(65)  # 50 radius
#     tim.right(angle)
#     angle += 1


def draw_sprirograph(size_of_gap: int):  # accept only integers instead of any
    for _ in range(int(360/size_of_gap)):  # So that it always makes a complete circle only. circle(360 degree)/
        # gaps(size between 2 circles)
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)  # The Current Heading increased by 10.


# draw_sprirograph(5)

# colors = colorgram.extract('./damien-hirst-spot-painting-for-sale.jpg', 30)  # Use an image path. ./ -> current directory
colors = colorgram.extract("C:\\Users\\soman\\OneDrive\\Desktop\\Govind's Library\\Coding\\python\\python-programming\\programming\\Object_Oriented_Programming\\Classes\\turtle\\turtle_advance\\damien-hirst-spot-painting-for-sale.jpg", 30)
# This is for the current directory
# print(colors)
# first_color = colors[0]
# rgb = first_color.rgb
# print(rgb)
list_of_colors_in_tuple_rgb = []
for color in colors:
    list_of_colors_in_tuple_rgb.append(color.rgb)
list_of_colors_in_tuple_rgb.pop(0)
list_of_colors_in_tuple_rgb.pop(0)

# for _ in range(10):
#     tim.pencolor(random.choice(list_of_colors_in_tuple_rgb))
#     tim.forward(10)
tim.shape("circle")
tim.pensize(20)
tim.teleport(-260, -200)  # Teleport to desire location and start from there
facing = "right"  # Created something we can toggle to control facing.
for i in range(10):  # Double loop to get row and column
    for j in range(10):
        tim.pencolor(random.choice(list_of_colors_in_tuple_rgb))
        tim.forward(1)  # For a dot
        tim.penup()
        if j < 9:  # last spacing isn't needed
            tim.forward(50)
            tim.pendown()
    if i < 9:
        if facing == "right":  # Decide if it was going right to left. Then now it should turn such that it turns
            # left to right.
            tim.left(90)  # Going a row above
            tim.forward(50)
            tim.left(90)
            tim.pendown()  # First dot of new row
            facing = "left"
        else:
            tim.right(90)
            tim.forward(50)
            tim.right(90)
            tim.pendown()
            facing = "right"

# Better Solution
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)  # Heading is the direction turtle faces, right is 0.
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:  # NOTE: Best way to divide 100 in 10 by 10. Select range 100 and do this.
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)

scree_object = tur.Screen()
scree_object.exitonclick()
