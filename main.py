import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

score = Scoreboard()
screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
pong = Ball()

screen.listen()

screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down, "Down")
screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(pong.speedy)
    screen.update()
    pong.move()
    # collision with top n bottom walls
    if pong.ycor() > 280 or pong.ycor() < - 280:
        pong.bounce()
    # collision with paddles
    if pong.distance(r_pad) < 50 and pong.xcor() > 320 or pong.distance(l_pad) < 50 and pong.xcor() < -320:
        pong.pad_bounce()
        pong.speed("fast")
    # Right_paddle misses
    if pong.xcor() > 380:
        pong.reset_position()
        score.l_point()

    # Left_paddle misses
    if pong.xcor() < -380:
        pong.reset_position()
        score.r_point()























screen.exitonclick()