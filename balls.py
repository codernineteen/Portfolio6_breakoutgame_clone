from turtle import Turtle
import bricks
bricks = bricks.Bricks()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(10)
        self.shape('circle')
        self.shapesize(0.75)
        self.color('#393e46')
        self.penup()
        self.goto(0,-136)
        self.seth(45)
        self.direction = 45
        self.dx = 3
        self.dy = 3

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def change_direction_x(self):
        self.dx *= -1

    def change_direction_y(self):
        self.dy *= -1