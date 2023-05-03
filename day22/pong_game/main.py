from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard

screen= Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
game_on = True

score = Scoreboard()
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
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_ball(1)
    elif ball.xcor() > 380:
        score.l_point()
        ball.reset_ball(-1)

    if score.l_score == 11 or score.r_score == 11:
        game_on = False
        







screen.exitonclick()