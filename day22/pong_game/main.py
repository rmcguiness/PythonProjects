from turtle import Screen
import time
from paddle import Paddle
from ball import Ball

screen= Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
game_on = True

ball = Ball()
paddleR = Paddle()
paddleL = Paddle("LEFT")

screen.listen()
screen.onkeypress(paddleR.move_up, "Up")
screen.onkeypress(paddleR.move_down, "Down")

screen.onkeypress(paddleL.move_up, "w")
screen.onkeypress(paddleL.move_down, "s")

while game_on:
    time.sleep(.01)
    screen.update()
    ball.move()
    ball.detect_collision(paddleL=paddleL, paddleR=paddleR)
    if not ball.in_play():
        game_on = False






screen.exitonclick()