from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)
game_on = True
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up_r, "Up")
screen.onkey(r_paddle.go_down_r, "Down")
screen.onkey(l_paddle.go_up_l, "w")
screen.onkey(l_paddle.go_down_l, "s")
sleep_time = 0.1


while game_on:
    time.sleep(sleep_time)
    screen.update()
    ball.ball_move()
    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        sleep_time *= 0.8
        ball.paddle_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        sleep_time *= 0.8
        ball.paddle_bounce()

    if ball.xcor() > 360:
        scoreboard.add_left_score()
        scoreboard.update_scoreboard()
        sleep_time = 0.1
        ball.reset_position()

    if ball.xcor() < -360:
        scoreboard.add_right_score()
        scoreboard.update_scoreboard()
        sleep_time = 0.1
        ball.reset_position()


screen.exitonclick()
