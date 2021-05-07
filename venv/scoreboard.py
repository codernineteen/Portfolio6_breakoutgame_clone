FONT = ("Courier", 20, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(-60,270)
        self.write("SCORE: ", align="left", font=FONT)
        self.goto(30,270)
        self.write(f"{self.score}", align="left", font=FONT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.goto(-60,240)
        self.write("SCORE: ", align="left", font=FONT)
        self.goto(30,240)
        self.write(f"{self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)