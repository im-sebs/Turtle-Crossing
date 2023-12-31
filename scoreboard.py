from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.update_score_board()
        self.hideturtle()

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
