import turtle as t
import random
tim = t.Turtle()
colors = ["DarkSlateBlue", "teal", "tomato", "sandy brown", "dark turquoise", "salmon", "magenta"]

def draw_shape(num_sides):
    tim.color(random.choice(colors))
    angle = 360/num_sides
    for move in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
