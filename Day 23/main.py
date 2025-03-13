import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import LevelBoard
STARTING_POSITION = (0, -280)

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.listen()
screen.tracer(0)


player = Player()
screen.onkey(player.move, "Up")
car_manager = CarManager()

level = LevelBoard()

cars = []
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.moving()

    # Detect the collision with the top wall
    if player.crossed():
        level.increase_level()
        player.goto(STARTING_POSITION)
        car_manager.level_up()

    # Detect the collisions with the cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            level.game_over()
            game_is_on = False

screen.mainloop()
screen.exitonclick()
