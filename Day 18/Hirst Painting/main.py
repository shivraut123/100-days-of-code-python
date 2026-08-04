# This module is for extracting colors
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
import turtle as turtle_module
from turtle import Screen
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(234, 251, 243), (248, 236, 35), (191, 12, 27), (226, 160, 58), (239, 245, 252), (239, 227, 4), (17, 152, 18), (15, 218, 92), (28, 36, 154), (25, 91, 179), (198, 14, 9), (237, 45, 155), (209, 83, 18), (61, 14, 9), (101, 7, 33), (12, 97, 63), (239, 149, 5), (61, 205, 229), (79, 209, 156), (194, 38, 74), (104, 231, 199), (9, 227, 237), (211, 131, 149), (43, 83, 226), (16, 23, 87), (5, 68, 42), (237, 161, 187), (70, 232, 241)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()


