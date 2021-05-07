from turtle import *
import paddle
import bricks
import balls
import scoreboard

screen = Screen()
paddle = paddle.Paddle()
bricks = bricks.Bricks()
balls = balls.Ball()
scoreboard = scoreboard.Scoreboard()

screen.bgcolor("#e1f1dd")
screen.setup(width=310, height=560)
screen.title("Breakout Game - by Yechan")
screen.listen()

screen.onkeypress(paddle.move_left, "Right")
screen.onkeypress(paddle.move_right, "Left")

breaker = Turtle()
breaker.hideturtle()
breaker.penup()
breaker.shape('square')
breaker.shapesize(stretch_wid=0.5, stretch_len=1.5)
breaker.color("#e1f1dd")

frame = Turtle()
frame.hideturtle()
frame.penup()
frame.goto(-155,220)
frame.pendown()
frame.forward(310)

game_is_on = True

while game_is_on:

    for item in bricks.brick_list:
        if balls.distance(item) < 15:
            balls.change_direction_y()
            bricks.brick_list.remove(item)
            breaker.goto(item.pos())
            breaker.stamp()
            scoreboard.score_up()

        elif balls.distance(item) == 20:
            balls.change_direction_x()
            bricks.brick_list.remove(item)
            breaker.goto(item.pos())
            breaker.stamp()
            scoreboard.score_up()

    if balls.xcor() > 133 or balls.xcor() < -133:
        balls.change_direction_x()

    if balls.distance(paddle) < 18:
        balls.change_direction_y()

    if balls.ycor() > 215:
        balls.change_direction_y()

    if balls.ycor() < -280:
        scoreboard.game_over()

    if scoreboard.score == 32:
        screen.bye()


    balls.move()
screen.exitonclick()
