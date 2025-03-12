import turtle
import random
import colorgram
from turtle import Turtle, Screen
tim = Turtle()
turtle.colormode(255)
tim.hideturtle()
tim.speed(15)

# using Hirst colors:
rgb_colors = []
colors = colorgram.extract("FLumequine.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))
hirst_colors = [(241, 228, 89), (24, 24, 61), (183, 73, 38), (144, 17, 31), (39, 29, 21), (214, 145, 85), (124, 159, 216), (204, 73, 115), (68, 26, 35), (55, 92, 138), (37, 45, 126), (23, 33, 23), (161, 21, 14), (142, 57, 80), (71, 78, 32), (67, 113, 74), (100, 98, 192), (141, 178, 161), (207, 77, 62), (144, 213, 191), (98, 168, 76), (192, 141, 156), (49, 85, 26), (156, 210, 221), (225, 172, 184), (175, 185, 221)]
turtle.bgcolor("misty rose")


def one_line():
    for dot in range(10):
        tim.color(random.choice(hirst_colors))
        tim.pendown()
        tim.dot(15)
        tim.penup()
        tim.forward(30)
        tim.pendown()


y_cor = -100
x_cor = -100
for i in range(10):
    tim.penup()
    tim.goto(x_cor, y_cor)
    one_line()
    y_cor += 30

screen = Screen()
screen.exitonclick()


