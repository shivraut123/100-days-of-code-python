from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("green yellow")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(120)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(120)
# timmy_the_turtle.forward(100)
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# import turtle
# tim = turtle.Turtle()

# from turtle import Turtle
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()

import turtle as t # aliasing import
import random
timmy = t.Turtle()

# colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "chocolate", "pink" , "lightblue", "maroon", "khaki"]
directions = [0, 90, 180, 270]

# Challenge 3 - Drawing different shapes
# for color in colors:
#     timmy.color(color)
# for color in colors:
#     timmy.color(color)
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#
#     for i in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)

# for drawing pentagon
# num_sides = 5
# for _ in range(num_sides):
#     angle = 360 / num_sides
#     timmy.forward(100)
#     timmy.right(angle)


# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Generate RGB Colors
t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# Challenge 4 - Generate a random walk
# timmy.pensize(15)
# timmy.speed("fastest")
# for _ in range(100):
#     t.colormode(255)
#
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# Draw a Spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy.speed("fastest")

def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
draw_spirograph(5)

# for _ in range(100):
    # timmy.color(random_color())
screen = Screen()
screen.exitonclick()

