from turtle import Turtle

color_list = ["#72147e", "#f21170", "#fa9905", "#ff5200"]
class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(100)
        self.hideturtle()
        self.reshape()
        self.count = 0
        self.brick_list = []
        for i in color_list:
            self.goto(x=-126,y=210 - self.count)
            self.move_right(i, 210 - self.count)
            self.count += 15

    def reshape(self):
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=1.5)
        self.penup()

    def move_right(self, c, ycor):
        for i in range(8):
            current_xcor = self.xcor()+35
            self.setx(current_xcor)
            a_brick = Turtle()
            a_brick.speed(100)
            a_brick.color(c)
            a_brick.shape('square')
            a_brick.shapesize(stretch_wid=0.5, stretch_len=1.5)
            a_brick.penup()
            a_brick.goto(current_xcor-35,ycor)
            self.brick_list.append(a_brick)


