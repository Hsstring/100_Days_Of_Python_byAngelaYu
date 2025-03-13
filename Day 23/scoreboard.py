from turtle import Turtle
FONT = ("Courier", 24, "normal")


class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.update_level_board()

    def update_level_board(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
