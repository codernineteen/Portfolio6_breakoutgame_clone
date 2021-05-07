from turtle import Turtle
X_COR = 0
Y_COR = -150


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(10)
        self.penup()
        self.shape("square")
        self.color("#766161")
        self.setpos(x=X_COR, y=Y_COR)
        self.shapesize(stretch_wid=0.5,stretch_len=1.5)

    def move_left(self):
        self.setx(self.xcor()+10)

    def move_right(self):
        self.setx(self.xcor()-10)
