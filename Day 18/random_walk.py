import random
import turtle
from turtle import Turtle, Screen
tim = Turtle()
angles = [0, 90, 180, 270]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b,)
    return color


tim.hideturtle()
tim.pensize(10)
tim.speed(10)
for move in range(200):
    angle = random.choice(angles)
    tim.color(random_color())
    tim.forward(20)
    tim.right(angle)

screen = Screen()
screen.exitonclick()
