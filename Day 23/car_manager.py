import random
import time
from turtle import Turtle
COLORS = ["IndianRed1", "lightCoral", "HotPink4", "IndianRed", "grey60", "maroon", "magenta", "orchid4"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setposition(300, random.randint(-240, 280))
            self.cars.append(new_car)
        
    def moving(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
