import turtle
import random
from turtle import Turtle, Screen
tim = Turtle()
turtle.colormode(255)
tim.hideturtle()
tim.speed(15)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b,)
    return color


for c in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.right(5)

screen = Screen()
screen.exitonclick()
